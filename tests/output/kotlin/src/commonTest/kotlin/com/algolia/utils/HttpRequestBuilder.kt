package com.algolia.utils

import io.ktor.client.plugins.*
import io.ktor.client.request.*

val HttpRequestBuilder.socketTimeout: Long? get() = getCapabilityOrNull(HttpTimeout)?.socketTimeoutMillis

val HttpRequestBuilder.connectTimeout: Long? get() = getCapabilityOrNull(HttpTimeout)?.connectTimeoutMillis
