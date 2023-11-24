package com.algolia.codegen;

import com.algolia.codegen.exceptions.*;
import com.fasterxml.jackson.databind.JsonNode;
import com.google.common.collect.Sets;
import io.swagger.v3.core.util.Json;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.net.URL;
import java.util.*;
import org.apache.commons.lang3.StringUtils;
import org.openapitools.codegen.CodegenOperation;
import org.yaml.snakeyaml.Yaml;

public class Utils {

  /** The suffix of our client names. */
  public static final String API_SUFFIX = "Client";

  public static final Set<String> CUSTOM_METHOD = Sets.newHashSet("del", "get", "post", "put");

  private static JsonNode cacheConfig;
  private static JsonNode cacheOpenApiToolsConfig;

  private Utils() {}

  public static String capitalize(String str) {
    return str.substring(0, 1).toUpperCase() + str.substring(1);
  }

  public static String camelize(String kebabStr) {
    String[] parts = kebabStr.split("-");
    String camel = parts[0].toLowerCase();
    for (int i = 1; i < parts.length; i++) {
      camel += capitalize(parts[i]);
    }
    return camel;
  }

  /**
   * Will add the boolean `vendorExtensions.x-is-custom-request` to operations if they should not
   * escape '/' in the path variable
   */
  public static CodegenOperation specifyCustomRequest(CodegenOperation ope) {
    if (CUSTOM_METHOD.contains(ope.operationIdOriginal)) {
      ope.vendorExtensions.put("x-is-custom-request", true);
    }
    return ope;
  }

  /** Returns the client name for the given language */
  public static String createClientName(String client, String language) {
    switch (language) {
      case "javascript":
        return camelize(client);
      case "go":
        return client;
      case "dart":
        return StringUtils.lowerCase(client);
      default:
        return capitalize(camelize(client));
    }
  }

  // testInput -> test-input
  public static String toKebabCase(String camelStr) {
    return camelStr.replaceAll("(.+?)([A-Z]|[0-9])", "$1-$2").toLowerCase(Locale.ROOT);
  }

  // testInput -> test_input
  // test-input -> test_input
  public static String toSnakeCase(String s) {
    return toKebabCase(s).replaceAll("-", "_");
  }

  /** Inject server info into the client to generate the right URL */
  public static void generateServer(String clientKebab, Map<String, Object> additionalProperties) throws ConfigException {
    Yaml yaml = new Yaml();
    try {
      Map<String, Object> spec = yaml.load(new FileInputStream("specs/bundled/" + clientKebab + ".yml"));
      List<Map<String, Object>> servers = (List<Map<String, Object>>) spec.get("servers");

      boolean hasRegionalHost = false;
      boolean fallbackToAliasHost = false;
      String regionalHost = "";
      String hostWithFallback = "";
      Set<String> allowedRegions = new HashSet<>();
      for (Map<String, Object> server : servers) {
        if (!server.containsKey("url")) {
          throw new ConfigException("Invalid server, does not contains 'url'");
        }

        // Determine if the current URL with `region` also have an alias without
        // variables.
        for (Map<String, Object> otherServer : servers) {
          if (server == otherServer) {
            continue;
          }
          String otherUrl = (String) otherServer.getOrDefault("url", "");
          if (otherUrl.replace(".{region}", "").equals(server.get("url"))) {
            URL fallbackURL = new URL(otherUrl.replace(".{region}", ""));
            fallbackToAliasHost = true;
            hostWithFallback = fallbackURL.getHost();
            break;
          }
        }

        if (!server.containsKey("variables")) {
          continue;
        }

        Map<String, Map<String, Object>> variables = (Map<String, Map<String, Object>>) server.get("variables");

        if (!variables.containsKey("region") || !variables.get("region").containsKey("enum")) {
          continue;
        }
        ArrayList<String> regions = (ArrayList<String>) variables.get("region").get("enum");
        hasRegionalHost = true;

        for (String region : regions) {
          allowedRegions.add(region);
        }

        // This is used for hosts like `insights` that uses `.io`
        URL url = new URL((String) server.get("url"));
        regionalHost = url.getHost();
      }
      additionalProperties.put("hostWithFallback", hostWithFallback);
      additionalProperties.put("hasRegionalHost", hasRegionalHost);
      additionalProperties.put("fallbackToAliasHost", fallbackToAliasHost);
      additionalProperties.put("regionalHost", regionalHost);
      additionalProperties.put("allowedRegions", allowedRegions.toArray(new String[0]));
    } catch (Exception e) {
      throw new ConfigException("Couldn't generate servers", e);
    }
  }

  /**
   * Get the current version of the given client from the
   * `clients/algoliasearch-client-javascript/packages/${client}/package.json` file, defaults to
   * 0.0.1 if not found
   */
  public static String getPackageJsonVersion(String client) throws ConfigException {
    try {
      JsonNode packageJson = Utils.readJsonFile("clients/algoliasearch-client-javascript/packages/" + client + "/package.json");
      String value = packageJson.get("version").asText();

      if (value.isEmpty()) {
        return "0.0.1";
      }

      return value;
    } catch (ConfigException e) {
      return "0.0.1";
    }
  }

  /** Get the `field` value in the `config/clients.config.json` file for the given language */
  public static String getClientConfigField(String language, String... fields) throws ConfigException {
    if (fields.length == 0) {
      throw new ConfigException("getClientConfigField requires at least one field");
    }
    if (cacheConfig == null) {
      cacheConfig = readJsonFile("config/clients.config.json");
    }
    JsonNode value = cacheConfig.get(language);
    for (String field : fields) {
      value = value.get(field);
    }
    if (!value.isTextual()) {
      throw new ConfigException(fields[fields.length - 1] + " is not a string");
    }
    return value.asText();
  }

  /** Get the `field` value in the `config/openapitools.json` file for the given language */
  public static String getOpenApiToolsField(String language, String client, String... fields) throws ConfigException {
    if (fields.length == 0) {
      throw new ConfigException("getOpenApiToolsField requires at least one field");
    }
    if (cacheOpenApiToolsConfig == null) {
      cacheOpenApiToolsConfig = readJsonFile("config/openapitools.json");
    }
    JsonNode value = cacheOpenApiToolsConfig
      .get("generator-cli")
      .get("generators")
      .get(language + "-" + client)
      .get("additionalProperties");
    for (String field : fields) {
      value = value.get(field);
    }
    if (!value.isTextual()) {
      throw new ConfigException(fields[fields.length - 1] + " is not a string");
    }
    return value.asText();
  }

  public static JsonNode readJsonFile(String filePath) throws ConfigException {
    try {
      return Json.mapper().readTree(new File(filePath));
    } catch (IOException e) {
      throw new ConfigException("Cannot read json file " + filePath, e);
    }
  }

  /**
   * If more than 2 variant are List<?>, the types are compatible and we cannot create override of
   * the `of` method, so we need to explicitly set the `of` method name, like `ofListofString` and
   * `ofListofList`.
   */
  public static boolean shouldUseExplicitOneOfName(Collection<String> oneOf) {
    return oneOf.stream().filter(type -> type != null && type.startsWith("List")).count() >= 2;
  }

  /**
   * Sets a `generationBanner` variable on the mustache templates, to display the generation banner
   * on generated files.
   */
  public static void setGenerationBanner(Map<String, Object> additionalProperties) {
    additionalProperties.put(
      "generationBanner",
      "Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will" +
      " be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT" +
      " EDIT."
    );
  }

  public static void prettyPrint(Object o) {
    Json.prettyPrint(o);
  }
}
