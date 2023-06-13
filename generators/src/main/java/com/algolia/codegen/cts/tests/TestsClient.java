package com.algolia.codegen.cts.tests;

import com.algolia.codegen.Utils;
import com.algolia.codegen.exceptions.CTSException;
import java.io.File;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.openapitools.codegen.CodegenModel;
import org.openapitools.codegen.CodegenOperation;
import org.openapitools.codegen.SupportingFile;

public class TestsClient extends TestsGenerator {

  public TestsClient(String language, String client) {
    super(language, client);
  }

  @Override
  public boolean available() {
    // no `lite` client test for now
    if ((language.equals("javascript") || language.equals("dart")) && client.equals("algoliasearch")) {
      return false;
    }

    File templates = new File("templates/" + language + "/tests/client/suite.mustache");
    return templates.exists();
  }

  @Override
  public void addSupportingFiles(List<SupportingFile> supportingFiles, String outputFolder, String extension) {
    if (!available()) {
      return;
    }
    supportingFiles.add(
      new SupportingFile("client/suite.mustache", outputFolder + "/client", Utils.createClientName(client, language) + extension)
    );
  }

  public void run(Map<String, CodegenModel> models, Map<String, CodegenOperation> operations, Map<String, Object> bundle) throws Exception {
    Map<String, ClientTestData[]> cts = loadCTS("client", client, ClientTestData[].class);
    ParametersWithDataType paramsType = new ParametersWithDataType(models, language);

    List<Object> blocks = new ArrayList<>();
    for (Map.Entry<String, ClientTestData[]> blockEntry : cts.entrySet()) {
      Map<String, Object> testObj = new HashMap<>();
      List<Object> tests = new ArrayList<>();
      int testIndex = 0;
      for (ClientTestData test : blockEntry.getValue()) {
        try {
          Map<String, Object> testOut = new HashMap<>();
          List<Object> steps = new ArrayList<>();
          testOut.put("testName", test.testName);
          testOut.put("testIndex", testIndex++);
          testOut.put("autoCreateClient", test.autoCreateClient);
          for (Step step : test.steps) {
            Map<String, Object> stepOut = new HashMap<>();
            CodegenOperation ope = null;
            if (step.type.equals("createClient")) {
              stepOut.put("isCreateClient", true);
            } else if (step.type.equals("variable")) {
              stepOut.put("isVariable", true);
            } else if (step.type.equals("method")) {
              ope = operations.get(step.path);
              if (ope == null) {
                throw new CTSException("Cannot find operation for method: " + step.path, test.testName);
              }
              stepOut.put("returnType", ope.returnType);
              stepOut.put("isMethod", true);
            }

            stepOut.put("object", step.object);
            stepOut.put("path", step.path);
            paramsType.enhanceParameters(step.parameters, stepOut, ope);

            if (step.expected.type != null) {
              switch (step.expected.type) {
                case "userAgent":
                  stepOut.put("testUserAgent", true);
                  break;
                case "host":
                  stepOut.put("testHost", true);
                  break;
                case "timeouts":
                  stepOut.put("testTimeouts", true);
                  break;
                default:
                  stepOut.put("testResult", true);
                  break;
              }
            }
            if (step.expected.error != null) {
              stepOut.put("isError", true);
              stepOut.put("expectedError", step.expected.error);
            } else if (step.expected.match != null) {
              if (step.expected.match instanceof Map) {
                Map<String, Object> match = new HashMap<>();
                paramsType.enhanceParameters((Map<String, Object>) step.expected.match, match);
                stepOut.put("match", match);
              } else {
                stepOut.put("match", step.expected.match);
              }
            }
            steps.add(stepOut);
          }
          testOut.put("steps", steps);
          tests.add(testOut);
        } catch (CTSException e) {
          e.setTestName(test.testName);
          throw e;
        }
      }
      testObj.put("tests", tests);
      testObj.put("testType", blockEntry.getKey());
      blocks.add(testObj);
    }
    bundle.put("blocksClient", blocks);
  }
}
