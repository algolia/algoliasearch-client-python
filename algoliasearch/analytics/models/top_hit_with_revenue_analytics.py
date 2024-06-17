# coding: utf-8

"""
Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
"""
from __future__ import annotations

from json import loads
from typing import Annotated, Any, Dict, Optional, Self, Union

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr

from algoliasearch.analytics.models.currencies_value import CurrenciesValue


class TopHitWithRevenueAnalytics(BaseModel):
    """
    TopHitWithRevenueAnalytics
    """

    hit: StrictStr = Field(
        description="Object ID of a record that's returned as a search result."
    )
    count: StrictInt = Field(description="Number of occurrences.")
    click_through_rate: Optional[
        Union[
            Annotated[float, Field(le=1, strict=True, ge=0)],
            Annotated[int, Field(le=1, strict=True, ge=0)],
        ]
    ] = Field(
        description="Click-through rate, calculated as number of tracked searches with at least one click event divided by the number of tracked searches. If null, Algolia didn't receive any search requests with `clickAnalytics` set to true. ",
        alias="clickThroughRate",
    )
    conversion_rate: Optional[
        Union[
            Annotated[float, Field(le=1, strict=True, ge=0)],
            Annotated[int, Field(le=1, strict=True, ge=0)],
        ]
    ] = Field(
        description="Conversion rate, calculated as number of tracked searches with at least one conversion event divided by the number of tracked searches. If null, Algolia didn't receive any search requests with `clickAnalytics` set to true. ",
        alias="conversionRate",
    )
    tracked_hit_count: StrictInt = Field(
        description="Number of tracked searches. Tracked searches are search requests where the `clickAnalytics` parameter is true.",
        alias="trackedHitCount",
    )
    click_count: Annotated[int, Field(strict=True, ge=0)] = Field(
        description="Number of clicks associated with this search.", alias="clickCount"
    )
    conversion_count: Annotated[int, Field(strict=True, ge=0)] = Field(
        description="Number of conversions from this search.", alias="conversionCount"
    )
    add_to_cart_rate: Optional[
        Union[
            Annotated[float, Field(le=1, strict=True, ge=0)],
            Annotated[int, Field(le=1, strict=True, ge=0)],
        ]
    ] = Field(
        description="Add-to-cart rate, calculated as number of tracked searches with at least one add-to-cart event divided by the number of tracked searches. If null, Algolia didn't receive any search requests with `clickAnalytics` set to true. ",
        alias="addToCartRate",
    )
    add_to_cart_count: Annotated[int, Field(strict=True, ge=0)] = Field(
        description="Number of add-to-cart events from this search.",
        alias="addToCartCount",
    )
    purchase_rate: Optional[
        Union[
            Annotated[float, Field(le=1, strict=True, ge=0)],
            Annotated[int, Field(le=1, strict=True, ge=0)],
        ]
    ] = Field(
        description="Purchase rate, calculated as number of tracked searches with at least one purchase event divided by the number of tracked searches. If null, Algolia didn't receive any search requests with `clickAnalytics` set to true. ",
        alias="purchaseRate",
    )
    purchase_count: StrictInt = Field(
        description="Number of purchase events from this search.", alias="purchaseCount"
    )
    currencies: Dict[str, CurrenciesValue] = Field(
        description="Revenue associated with this search, broken-down by currencies."
    )

    model_config = ConfigDict(
        use_enum_values=True, populate_by_name=True, validate_assignment=True
    )

    def to_json(self) -> str:
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TopHitWithRevenueAnalytics from a JSON string"""
        return cls.from_dict(loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={},
            exclude_none=True,
        )
        _field_dict = {}
        if self.currencies:
            for _key in self.currencies:
                if self.currencies[_key]:
                    _field_dict[_key] = self.currencies[_key].to_dict()
            _dict["currencies"] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TopHitWithRevenueAnalytics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "hit": obj.get("hit"),
                "count": obj.get("count"),
                "clickThroughRate": obj.get("clickThroughRate"),
                "conversionRate": obj.get("conversionRate"),
                "trackedHitCount": obj.get("trackedHitCount"),
                "clickCount": obj.get("clickCount"),
                "conversionCount": obj.get("conversionCount"),
                "addToCartRate": obj.get("addToCartRate"),
                "addToCartCount": obj.get("addToCartCount"),
                "purchaseRate": obj.get("purchaseRate"),
                "purchaseCount": obj.get("purchaseCount"),
                "currencies": (
                    dict(
                        (_k, CurrenciesValue.from_dict(_v))
                        for _k, _v in obj.get("currencies").items()
                    )
                    if obj.get("currencies") is not None
                    else None
                ),
            }
        )
        return _obj
