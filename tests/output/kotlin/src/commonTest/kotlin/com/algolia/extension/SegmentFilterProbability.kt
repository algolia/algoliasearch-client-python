package com.algolia.extension

import com.algolia.client.model.predict.SegmentFilterProbability
import com.algolia.utils.toNumberType

internal fun SegmentFilterProbability(
  lt: Number? = null,
  lte: Number? = null,
  gt: Number? = null,
  gte: Number? = null,
): SegmentFilterProbability = SegmentFilterProbability(
  lt = lt?.toNumberType(),
  lte = lte?.toNumberType(),
  gt = gt?.toNumberType(),
  gte = gte?.toNumberType(),
)
