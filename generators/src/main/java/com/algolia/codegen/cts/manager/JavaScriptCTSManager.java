package com.algolia.codegen.cts.manager;

import com.algolia.codegen.Utils;
import com.algolia.codegen.exceptions.GeneratorException;
import com.fasterxml.jackson.databind.JsonNode;
import java.util.*;
import org.openapitools.codegen.SupportingFile;

public class JavaScriptCTSManager implements CTSManager {

  private final String client;

  public JavaScriptCTSManager(String client) {
    this.client = client;
  }

  @Override
  public void addSupportingFiles(List<SupportingFile> supportingFiles) {
    supportingFiles.add(new SupportingFile("package.mustache", "", "package.json"));
  }

  @Override
  public void addDataToBundle(Map<String, Object> bundle) throws GeneratorException {
    String npmNamespace = Utils.getClientConfigField("javascript", "npmNamespace");

    bundle.put("utilsPackageVersion", Utils.getPackageJsonVersion("client-common"));
    bundle.put("npmNamespace", npmNamespace);

    JsonNode openApiToolsConfig = Utils.readJsonFile("config/openapitools.json").get("generator-cli").get("generators");
    Iterator<Map.Entry<String, JsonNode>> fields = openApiToolsConfig.fields();
    List<Map<String, String>> clients = new ArrayList<>();

    while (fields.hasNext()) {
      Map.Entry<String, JsonNode> field = fields.next();

      if (!field.getKey().startsWith("javascript-")) {
        continue;
      }

      Map<String, String> client = new HashMap<>();
      String output = field.getValue().get("output").asText();
      String packageName = output.substring(output.lastIndexOf("/") + 1);

      client.put("packagePath", "link:../../../" + output.replace("#{cwd}/", ""));

      if (!packageName.equals("algoliasearch")) {
        packageName = npmNamespace + "/" + packageName;
      }

      client.put("packageName", packageName);

      clients.add(client);
    }

    String output = openApiToolsConfig.get("javascript-" + client).get("output").asText();
    String clientName = output.substring(output.lastIndexOf('/') + 1);

    bundle.put("packageDependencies", clients);

    if (clientName.equals("algoliasearch")) {
      bundle.put("import", "algoliasearch/lite");
    } else {
      bundle.put("import", npmNamespace + "/" + clientName);
    }
  }
}
