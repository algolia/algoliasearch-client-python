package com.algolia.codegen;

import com.algolia.codegen.exceptions.*;
import com.fasterxml.jackson.databind.JsonNode;
import io.swagger.v3.oas.models.Operation;
import io.swagger.v3.oas.models.servers.Server;
import java.util.List;
import java.util.Map;
import org.openapitools.codegen.CodegenOperation;
import org.openapitools.codegen.SupportingFile;
import org.openapitools.codegen.languages.TypeScriptNodeClientCodegen;
import org.openapitools.codegen.model.ModelMap;
import org.openapitools.codegen.model.ModelsMap;
import org.openapitools.codegen.model.OperationsMap;

public class AlgoliaJavaScriptGenerator extends TypeScriptNodeClientCodegen {

  private String CLIENT;
  private boolean isAlgoliasearchClient;
  private static JsonNode cacheOpenApiToolsConfig;

  @Override
  public String getName() {
    return "algolia-javascript";
  }

  @Override
  public void processOpts() {
    super.processOpts();

    CLIENT = Utils.camelize((String) additionalProperties.get("client"));
    isAlgoliasearchClient = CLIENT.equals("algoliasearch");

    // generator specific options
    setSupportsES6(true);
    setModelPropertyNaming("original");
    setApiPackage("src");

    // Generation notice, added on every generated files
    Utils.setGenerationBanner(additionalProperties);

    languageSpecificPrimitives.add("Record");
    instantiationTypes.put("map", "Record");
    // clear all supported files to avoid unwanted ones
    supportingFiles.clear();

    // Files common to both generations
    supportingFiles.add(new SupportingFile("rollup.mustache", "", "rollup.config.js"));
    supportingFiles.add(new SupportingFile("package.mustache", "", "package.json"));
    supportingFiles.add(new SupportingFile("tsconfig.mustache", "", "tsconfig.json"));

    // root export files
    supportingFiles.add(new SupportingFile("index.mustache", "", "index.js"));
    supportingFiles.add(new SupportingFile("index.d.mustache", "", "index.d.ts"));

    // `client` related files, `algoliasearch` have it's own logic below
    if (!isAlgoliasearchClient) {
      // models
      supportingFiles.add(new SupportingFile("client/model/clientMethodProps.mustache", "model", "clientMethodProps.ts"));
      supportingFiles.add(new SupportingFile("client/model/modelBarrel.mustache", "model", "index.ts"));

      // builds
      supportingFiles.add(new SupportingFile("client/builds/browser.mustache", "builds", "browser.ts"));
      supportingFiles.add(new SupportingFile("client/builds/node.mustache", "builds", "node.ts"));
    }
    // `algoliasearch` related files
    else {
      // `algoliasearch` builds
      supportingFiles.add(new SupportingFile("algoliasearch/builds/browser.mustache", "builds", "browser.ts"));
      supportingFiles.add(new SupportingFile("algoliasearch/builds/node.mustache", "builds", "node.ts"));
      supportingFiles.add(new SupportingFile("algoliasearch/builds/models.mustache", "builds", "models.ts"));

      // `lite` builds
      supportingFiles.add(new SupportingFile("client/builds/browser.mustache", "lite/builds", "browser.ts"));
      supportingFiles.add(new SupportingFile("client/builds/node.mustache", "lite/builds", "node.ts"));

      // `lite` models
      supportingFiles.add(new SupportingFile("client/model/clientMethodProps.mustache", "lite/model", "clientMethodProps.ts"));
      supportingFiles.add(new SupportingFile("client/model/modelBarrel.mustache", "lite/model", "index.ts"));

      // `lite root export files
      supportingFiles.add(new SupportingFile("algoliasearch/lite.mustache", "", "lite.js"));
      supportingFiles.add(new SupportingFile("algoliasearch/lite.d.mustache", "", "lite.d.ts"));
      supportingFiles.add(new SupportingFile("algoliasearch/lite.tsconfig.mustache", "", "lite/tsconfig.json"));
    }
  }

  @Override
  public String apiFileFolder() {
    String fileFolder = super.apiFileFolder();

    if (!isAlgoliasearchClient) {
      return fileFolder;
    }

    return fileFolder.replace("src", "lite/src");
  }

  @Override
  public String modelFileFolder() {
    String fileFolder = super.modelFileFolder();

    if (!isAlgoliasearchClient) {
      return fileFolder;
    }

    return fileFolder.replace("model", "lite/model");
  }

  @Override
  public CodegenOperation fromOperation(String path, String httpMethod, Operation operation, List<Server> servers) {
    return Utils.specifyCustomRequest(super.fromOperation(path, httpMethod, operation, servers));
  }

  /** Get the packageName from the output field in the `config/openapitools.json` file */
  public String getPackageName(String client) throws ConfigException {
    if (cacheOpenApiToolsConfig == null) {
      cacheOpenApiToolsConfig = Utils.readJsonFile("config/openapitools.json");
    }

    String output = cacheOpenApiToolsConfig
      .get("generator-cli")
      .get("generators")
      .get("javascript-" + (String) additionalProperties.get("client"))
      .get("output")
      .asText();

    return output.substring(output.lastIndexOf("/") + 1);
  }

  /** Set default generator options */
  private void setDefaultGeneratorOptions() {
    String apiName = CLIENT + Utils.API_SUFFIX;
    String packageName = getPackageName(CLIENT);

    additionalProperties.put("apiName", apiName);
    additionalProperties.put("capitalizedApiName", Utils.capitalize(apiName));
    additionalProperties.put("algoliaAgent", Utils.capitalize(CLIENT));
    additionalProperties.put("gitRepoId", "algoliasearch-client-javascript");
    additionalProperties.put("isSearchClient", CLIENT.equals("search"));
    additionalProperties.put("isIngestionClient", CLIENT.equals("ingestion"));
    additionalProperties.put("isAlgoliasearchClient", isAlgoliasearchClient);
    additionalProperties.put("packageVersion", Utils.getPackageJsonVersion(packageName));
    additionalProperties.put("packageName", packageName);

    if (isAlgoliasearchClient) {
      // Files used to create the package.json of the algoliasearch package
      additionalProperties.put("analyticsVersion", Utils.getPackageJsonVersion("client-analytics"));
      additionalProperties.put("abtestingVersion", Utils.getPackageJsonVersion("client-abtesting"));
      additionalProperties.put("personalizationVersion", Utils.getPackageJsonVersion("client-personalization"));
      additionalProperties.put("searchVersion", Utils.getPackageJsonVersion("client-search"));

      // Files used to generate the `lite` client
      apiName = "lite" + Utils.API_SUFFIX;
      additionalProperties.put("apiName", apiName);
      additionalProperties.put("capitalizedApiName", Utils.capitalize(apiName));
      additionalProperties.put("algoliaAgent", "Lite");
    }
  }

  @Override
  public Map<String, ModelsMap> postProcessAllModels(Map<String, ModelsMap> objs) {
    Map<String, ModelsMap> models = super.postProcessAllModels(objs);
    GenericPropagator.propagateGenericsToModels(models);
    return models;
  }

  /** Provides an opportunity to inspect and modify operation data before the code is generated. */
  @Override
  public OperationsMap postProcessOperationsWithModels(OperationsMap objs, List<ModelMap> allModels) {
    OperationsMap results = super.postProcessOperationsWithModels(objs, allModels);

    setDefaultGeneratorOptions();
    try {
      Utils.generateServer((String) additionalProperties.get("client"), additionalProperties);
      additionalProperties.put("utilsPackageVersion", Utils.getPackageJsonVersion("client-common"));
      additionalProperties.put("npmNamespace", Utils.getClientConfigField("javascript", "npmNamespace"));
    } catch (GeneratorException e) {
      e.printStackTrace();
      System.exit(1);
    }

    List<CodegenOperation> operations = results.getOperations().getOperation();

    // We read operations and detect if we should wrap parameters under an object.
    // We only wrap if there is a mix between body parameters and other parameters.
    for (CodegenOperation ope : operations) {
      // Nothing to wrap as there is no parameters
      if (!ope.hasParams) {
        continue;
      }

      boolean hasBodyParams = !ope.bodyParams.isEmpty();
      boolean hasHeaderParams = !ope.headerParams.isEmpty();
      boolean hasQueryParams = !ope.queryParams.isEmpty();
      boolean hasPathParams = !ope.pathParams.isEmpty();

      // If there is nothing but body params, we just check if it's a single param
      if (hasBodyParams && !hasHeaderParams && !hasQueryParams && !hasPathParams) {
        // At this point the single parameter is already an object, to avoid double wrapping
        // we skip it
        if (ope.bodyParams.size() == 1 && !ope.bodyParams.get(0).isArray) {
          ope.vendorExtensions.put("x-is-single-body-param", true);
          continue;
        }
      }

      // Any other cases here are wrapped
      ope.vendorExtensions.put("x-create-wrapping-object", true);
    }

    GenericPropagator.propagateGenericsToOperations(results, allModels);

    return results;
  }

  /**
   * The `apiSuffix` option is not supported on the TypeScript client, so we override the names
   * method to use it with our suffix.
   */

  /** The `apiName` is capitalized. */
  @Override
  public String toApiName(String name) {
    if (name.length() == 0) {
      return "Default" + Utils.API_SUFFIX;
    }

    String endClient = isAlgoliasearchClient ? "lite" : CLIENT;

    return Utils.capitalize(endClient + Utils.API_SUFFIX);
  }

  /** The `apiFileName` is in camelCase. */
  @Override
  public String toApiFilename(String name) {
    if (name.length() == 0) {
      return "default" + Utils.API_SUFFIX;
    }

    String endClient = isAlgoliasearchClient ? "lite" : CLIENT;

    return endClient + Utils.API_SUFFIX;
  }

  /** The `apiFileName` is in camelCase. */
  @Override
  public String apiFilename(String templateName, String tag) {
    return super.apiFilename(templateName, toApiFilename(CLIENT));
  }
}
