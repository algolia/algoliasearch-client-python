package com.algolia.utils

import io.ktor.http.*

fun String.toPathSegments() = split("/").filter { it.isNotBlank() }.map { it.decodeURLPart() }
