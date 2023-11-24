package com.algolia.codegen;

import com.algolia.codegen.exceptions.*;
import java.util.*;
import org.openapitools.codegen.*;
import org.openapitools.codegen.CodegenConstants;
import org.openapitools.codegen.languages.PythonClientCodegen;

public class AlgoliaPythonGenerator extends PythonClientCodegen {

  @Override
  public String getName() {
    return "algolia-python";
  }

  @Override
  public void processOpts() {
    String client = (String) additionalProperties.get("client");

    additionalProperties.put("isSearchClient", client.equals("search"));
    additionalProperties.put("packageVersion", Utils.getClientConfigField("python", "packageVersion"));
    additionalProperties.put(CodegenConstants.EXCLUDE_TESTS, true);

    setApiNameSuffix(Utils.API_SUFFIX);

    setPackageName(Utils.toSnakeCase(client));
    setApiPackage("api");
    setModelPackage("models");

    super.processOpts();

    // // Generation notice, added on every generated files
    Utils.setGenerationBanner(additionalProperties);

    // Prevent all useless file to generate
    apiDocTemplateFiles.clear();
    modelDocTemplateFiles.clear();
    apiTestTemplateFiles.clear();
    modelTestTemplateFiles.clear();

    // Remove some files we don't want to output or change their paths
    supportingFiles.removeIf(file ->
      file.getTemplateFile().equals("git_push.sh.mustache") ||
      file.getTemplateFile().equals("requirements.mustache") ||
      file.getTemplateFile().equals("test-requirements.mustache") ||
      file.getTemplateFile().equals("tox.mustache") ||
      file.getTemplateFile().equals("setup_cfg.mustache") ||
      file.getTemplateFile().equals("setup.mustache") ||
      file.getTemplateFile().equals("pyproject.mustache") ||
      file.getTemplateFile().equals("py.typed.mustache") ||
      file.getTemplateFile().equals("rest.mustache") ||
      file.getTemplateFile().equals("README.mustache") ||
      file.getTemplateFile().equals("api_test.mustache") ||
      file.getTemplateFile().equals("model_test.mustache") ||
      file.getTemplateFile().equals("github-workflow.mustache") ||
      file.getTemplateFile().equals("travis.mustache") ||
      file.getTemplateFile().equals("gitlab-ci.mustache")
    );

    // repository
    supportingFiles.add(new SupportingFile("pyproject.mustache", "../", "pyproject.toml"));

    try {
      Utils.generateServer(client, additionalProperties);
    } catch (GeneratorException e) {
      e.printStackTrace();
      System.exit(1);
    }
  }
}
