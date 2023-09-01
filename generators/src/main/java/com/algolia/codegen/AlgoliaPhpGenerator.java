package com.algolia.codegen;

import com.algolia.codegen.exceptions.*;
import io.swagger.v3.oas.models.Operation;
import io.swagger.v3.oas.models.servers.Server;
import java.util.List;
import org.openapitools.codegen.CodegenOperation;
import org.openapitools.codegen.SupportingFile;
import org.openapitools.codegen.languages.PhpClientCodegen;

public class AlgoliaPhpGenerator extends PhpClientCodegen {

  @Override
  public String getName() {
    return "algolia-php";
  }

  public String getClientName(String client) {
    return Utils.createClientName(client, "php");
  }

  @Override
  public void processOpts() {
    // generator specific options
    String client = (String) additionalProperties.get("client");
    setApiNameSuffix(Utils.API_SUFFIX);
    setParameterNamingConvention("camelCase");
    additionalProperties.put("modelPackage", "Model\\" + getClientName(client));
    additionalProperties.put("invokerPackage", "Algolia\\AlgoliaSearch");
    additionalProperties.put("clientName", getClientName(client));

    super.processOpts();

    // Generation notice, added on every generated files
    Utils.setGenerationBanner(additionalProperties);

    // Remove base template as we want to change its path
    supportingFiles.removeIf(file -> file.getTemplateFile().equals("Configuration.mustache"));
    supportingFiles.removeIf(file -> file.getTemplateFile().equals(".php-cs-fixer.php"));
    supportingFiles.removeIf(file -> file.getTemplateFile().equals(".php-cs-fixer.dist.php"));
    supportingFiles.removeIf(file -> file.getTemplateFile().equals("phpunit.xml.mustache"));

    supportingFiles.add(new SupportingFile("Configuration.mustache", "lib/Configuration", "Configuration.php"));
    supportingFiles.add(new SupportingFile("ConfigWithRegion.mustache", "lib/Configuration", "ConfigWithRegion.php"));

    supportingFiles.add(new SupportingFile("client_config.mustache", "lib/Configuration", getClientName(client) + "Config.php"));
    supportingFiles.add(new SupportingFile("Algolia.mustache", "lib", "Algolia.php"));

    setDefaultGeneratorOptions(client);
    try {
      Utils.generateServer(client, additionalProperties);
      additionalProperties.put("packageVersion", Utils.getClientConfigField("php", "packageVersion"));
    } catch (GeneratorException e) {
      e.printStackTrace();
      System.exit(1);
    }
  }

  @Override
  public CodegenOperation fromOperation(String path, String httpMethod, Operation operation, List<Server> servers) {
    return Utils.specifyCustomRequest(super.fromOperation(path, httpMethod, operation, servers));
  }

  /** Set default generator options */
  public void setDefaultGeneratorOptions(String client) {
    if (client.equals("search") || client.equals("recommend")) {
      additionalProperties.put("useCache", true);
    }
    additionalProperties.put("isSearchClient", client.equals("search"));
    additionalProperties.put("configClassname", getClientName(client) + "Config");
  }

  public String getComposerPackageName() {
    return "algolia/algoliasearch-client-php";
  }
}
