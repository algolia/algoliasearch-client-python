package com.algolia.codegen;

import com.algolia.codegen.exceptions.*;
import io.swagger.v3.oas.models.Operation;
import io.swagger.v3.oas.models.servers.Server;
import java.io.File;
import java.util.List;
import org.openapitools.codegen.CodegenOperation;
import org.openapitools.codegen.SupportingFile;
import org.openapitools.codegen.languages.GoClientCodegen;

public class AlgoliaGoGenerator extends GoClientCodegen {

  @Override
  public String getName() {
    return "algolia-go";
  }

  @Override
  public void processOpts() {
    String client = (String) additionalProperties.get("client");
    additionalProperties.put("enumClassPrefix", true);

    String outputFolder = "algolia" + File.separator + client;
    setOutputDir(getOutputDir() + File.separator + outputFolder);

    super.processOpts();

    // Generation notice, added on every generated files
    Utils.setGenerationBanner(additionalProperties);

    apiTestTemplateFiles.clear();
    modelTestTemplateFiles.clear();
    apiDocTemplateFiles.clear();
    modelDocTemplateFiles.clear();

    supportingFiles.clear();
    supportingFiles.add(new SupportingFile("configuration.mustache", "", "configuration.go"));
    supportingFiles.add(new SupportingFile("client.mustache", "", "client.go"));
    supportingFiles.add(new SupportingFile("response.mustache", "", "response.go"));
    supportingFiles.add(new SupportingFile("utils.mustache", "", "utils.go"));

    try {
      Utils.generateServer(client, additionalProperties);
      additionalProperties.put("packageVersion", Utils.getClientConfigField("go", "packageVersion"));
    } catch (GeneratorException e) {
      e.printStackTrace();
      System.exit(1);
    }
  }

  @Override
  public CodegenOperation fromOperation(String path, String httpMethod, Operation operation, List<Server> servers) {
    return Utils.specifyCustomRequest(super.fromOperation(path, httpMethod, operation, servers));
  }
}
