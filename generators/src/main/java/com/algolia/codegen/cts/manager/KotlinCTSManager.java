package com.algolia.codegen.cts.manager;

import com.algolia.codegen.Utils;
import com.algolia.codegen.exceptions.GeneratorException;
import java.util.List;
import java.util.Map;
import org.openapitools.codegen.SupportingFile;

public class KotlinCTSManager implements CTSManager {

  private final String client;

  public KotlinCTSManager(String client) {
    this.client = client;
  }

  @Override
  public void addSupportingFiles(List<SupportingFile> supportingFiles) {
    // NO-OP
  }

  @Override
  public void addDataToBundle(Map<String, Object> bundle) throws GeneratorException {
    bundle.put("packageVersion", Utils.getClientConfigField("kotlin", "packageVersion"));
    bundle.put("import", Utils.camelize(this.client).toLowerCase());
  }
}
