package com.algolia.config;

import com.fasterxml.jackson.core.type.TypeReference;
import java.io.Closeable;

/**
 * Represents a mechanism for executing HTTP requests and deserializing responses. It provides
 * methods for making requests and returning the desired object representation. Implementations of
 * this interface should ensure proper resource management.
 */
public interface Requester extends Closeable {
  /**
   * Executes an HTTP request and deserializes the response into a specified Java type.
   *
   * @param <T> The type of the returned object.
   * @param httpRequest The HTTP request to be executed.
   * @param requestOptions Optional request options.
   * @param returnType The class of the response.
   * @param innerType The inner class type if the response is a container type.
   * @return The deserialized response.
   */
  <T> T execute(HttpRequest httpRequest, RequestOptions requestOptions, Class<?> returnType, Class<?> innerType);

  /**
   * Executes an HTTP request and deserializes the response into a specified type reference.
   *
   * @param <T> The type of the returned object.
   * @param httpRequest The HTTP request to be executed.
   * @param requestOptions Optional request options.
   * @param returnType The type reference of the response.
   * @return The deserialized response.
   */
  <T> T execute(HttpRequest httpRequest, RequestOptions requestOptions, TypeReference<?> returnType);
}
