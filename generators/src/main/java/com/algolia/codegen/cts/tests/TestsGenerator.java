package com.algolia.codegen.cts.tests;

import com.algolia.codegen.Utils;
import com.algolia.codegen.exceptions.CTSException;
import io.swagger.v3.core.util.Json;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import org.openapitools.codegen.CodegenModel;
import org.openapitools.codegen.CodegenOperation;
import org.openapitools.codegen.SupportingFile;

public abstract class TestsGenerator {

  protected final String language, client;

  public TestsGenerator(String language, String client) {
    this.language = language;
    this.client = client;
  }

  public abstract boolean available();

  public abstract void addSupportingFiles(List<SupportingFile> supportingFiles, String outputFolder, String extension);

  public abstract void run(Map<String, CodegenModel> models, Map<String, CodegenOperation> operations, Map<String, Object> bundle)
    throws Exception;

  protected <T> Map<String, T> loadCTS(String path, String clientName, Class<T> jsonType) throws Exception {
    if (!available()) {
      throw new CTSException("Templates not found for " + path, true);
    }

    File dir = new File("tests/CTS/" + path + "/" + clientName);
    File commonTestDir = new File("tests/CTS/" + path + "/common");
    if (!dir.exists()) {
      throw new CTSException("CTS not found at " + dir.getAbsolutePath(), true);
    }
    if (!commonTestDir.exists()) {
      throw new CTSException("CTS not found at " + commonTestDir.getAbsolutePath(), true);
    }
    List<File> allTests = new ArrayList<>();
    Collections.addAll(allTests, dir.listFiles());
    Collections.addAll(allTests, commonTestDir.listFiles());

    Map<String, T> cts = new TreeMap<>();

    for (File f : allTests) {
      String json = new String(Files.readAllBytes(Paths.get(f.getAbsolutePath())));
      json = injectVariables(json);
      cts.put(f.getName().replace(".json", ""), Json.mapper().readValue(json, jsonType));
    }
    return cts;
  }

  private String languageCased() {
    switch (language) {
      case "java":
        return "Java";
      case "javascript":
        return "JavaScript";
      case "php":
        return "PHP";
      case "kotlin":
        return "Kotlin";
      default:
        return language;
    }
  }

  private String injectVariables(String json) {
    return json.replace("${{languageCased}}", languageCased()).replace("${{clientPascalCase}}", Utils.capitalize(Utils.camelize(client)));
  }
}
