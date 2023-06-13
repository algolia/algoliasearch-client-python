package com.algolia.codegen.cts.manager;

import com.algolia.codegen.Utils;
import com.algolia.codegen.exceptions.GeneratorException;
import java.util.List;
import java.util.Map;
import org.apache.commons.lang3.StringUtils;
import org.openapitools.codegen.SupportingFile;

public class DartCTSManager implements CTSManager {

  private final String clientName;

  public DartCTSManager(String clientName) {
    this.clientName = clientName;
  }

  @Override
  public void addSupportingFiles(List<SupportingFile> supportingFiles) {
    // NO-OP
  }

  @Override
  public void addDataToBundle(Map<String, Object> bundle) throws GeneratorException {
    bundle.put("packageVersion", Utils.getClientConfigField("dart", "packageVersion"));
    if (clientName.equals("algoliasearch")) {
      bundle.put("import", "package:algoliasearch/algoliasearch_lite.dart");
      bundle.put("client", "SearchClient");
    } else {
      String packageName = "algolia_client_" + StringUtils.lowerCase(clientName);
      bundle.put("import", "package:" + packageName + "/" + packageName + ".dart");
      bundle.put("client", StringUtils.capitalize(clientName) + "Client");
    }
  }
}
