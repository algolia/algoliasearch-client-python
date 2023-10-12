package com.algolia.client.configuration.internal

import io.ktor.client.plugins.api.*
import io.ktor.client.request.*
import io.ktor.content.*
import io.ktor.http.content.ByteArrayContent
import java.io.ByteArrayOutputStream
import java.util.zip.GZIPOutputStream

/**
 * Plugin to gzip encode body (text) requests.
 */
internal val GzipCompression: ClientPlugin<Unit> = createClientPlugin("GzipCompression") {
  on(Send) { request ->
    val body = request.body
    if (body is TextContent) {
      val encoded = ByteArrayOutputStream().use { bos ->
        GZIPOutputStream(bos).bufferedWriter().use { gzip -> gzip.write(body.text) }
        bos.toByteArray()
      }
      val content = ByteArrayContent(encoded, contentType = body.contentType)
      request.header("Content-Encoding", "gzip")
      request.setBody(content)
    }
    proceed(request)
  }
}
