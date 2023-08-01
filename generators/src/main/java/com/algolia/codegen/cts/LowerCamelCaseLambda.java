package com.algolia.codegen.cts;

import static org.apache.commons.lang3.StringUtils.*;

import com.samskivert.mustache.Mustache;
import com.samskivert.mustache.Template;
import java.io.IOException;
import java.io.Writer;
import org.openapitools.codegen.utils.CamelizeOption;
import org.openapitools.codegen.utils.StringUtils;

public class LowerCamelCaseLambda implements Mustache.Lambda {

  @Override
  public void execute(Template.Fragment fragment, Writer writer) throws IOException {
    String text = fragment.execute();
    writer.write(lowerCamelCase(text));
  }

  private String lowerCamelCase(String text) {
    if (isAllUpperCase(text)) {
      return lowerCase(text);
    } else {
      return StringUtils.camelize(text, CamelizeOption.LOWERCASE_FIRST_CHAR);
    }
  }
}
