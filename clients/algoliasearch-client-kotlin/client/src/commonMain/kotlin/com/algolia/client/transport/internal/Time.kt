package com.algolia.client.transport.internal

import kotlinx.datetime.Clock

/** Current epoch time in milliseconds */
internal fun currentTimeMillis() = Clock.System.now().toEpochMilliseconds()
