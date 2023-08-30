package com.algolia.utils;

import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.time.LocalDate;
import java.time.OffsetDateTime;
import java.util.Collection;
import java.util.Date;
import java.util.List;
import java.util.stream.Collectors;

public class StringUtils {

  private StringUtils() {
    // Empty.
  }

  /**
   * Escape the given string to be used as URL query value.
   *
   * @param str String to be escaped
   * @return Escaped string
   */
  public static String escape(String str) {
    try {
      return URLEncoder.encode(str, "utf8").replaceAll("\\+", "%20");
    } catch (UnsupportedEncodingException e) {
      return str;
    }
  }

  public static String pathFormat(String template, boolean escapeValues, Object... values) {
    int i = 0;
    while (template.contains("{") && i < values.length) {
      String value = String.valueOf(values[i]);
      String string = escapeValues ? escape(value) : value;
      template = template.replaceFirst("\\{[^}]+}", string);
      i++;
    }
    if (template.contains("{")) {
      throw new IllegalArgumentException("Not enough replacement values for all placeholders.");
    }
    if (i < values.length) {
      throw new IllegalArgumentException("More replacement values provided than placeholders.");
    }
    return template;
  }

  public static String paramToString(Object value) {
    if (value instanceof Date || value instanceof OffsetDateTime || value instanceof LocalDate) {
      throw new UnsupportedOperationException("Date must come as string (already serialized)");
    }
    if (value instanceof Collection) {
      List<String> strings = ((Collection<?>) value).stream().map(String::valueOf).collect(Collectors.toList());
      return String.join(",", strings);
    }

    return String.valueOf(value);
  }
}
