package com.algolia.utils;

import com.algolia.exceptions.AlgoliaRuntimeException;

public class Parameters {

  private Parameters() {
    // Empty.
  }

  public static void requireNonNull(Object param, String error) {
    if (param == null) {
      throw new AlgoliaRuntimeException(error);
    }
  }
}
