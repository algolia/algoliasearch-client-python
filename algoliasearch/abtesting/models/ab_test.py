# coding: utf-8

"""
Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
"""

from __future__ import annotations

from json import loads
from sys import version_info
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict

if version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


from algoliasearch.abtesting.models.ab_test_configuration import ABTestConfiguration
from algoliasearch.abtesting.models.status import Status
from algoliasearch.abtesting.models.variant import Variant

_ALIASES = {
    "ab_test_id": "abTestID",
    "click_significance": "clickSignificance",
    "conversion_significance": "conversionSignificance",
    "add_to_cart_significance": "addToCartSignificance",
    "purchase_significance": "purchaseSignificance",
    "revenue_significance": "revenueSignificance",
    "updated_at": "updatedAt",
    "created_at": "createdAt",
    "end_at": "endAt",
    "name": "name",
    "status": "status",
    "variants": "variants",
    "configuration": "configuration",
}


def _alias_generator(name: str) -> str:
    return _ALIASES.get(name, name)


class ABTest(BaseModel):
    """
    ABTest
    """

    ab_test_id: int
    """ Unique A/B test identifier. """
    click_significance: Optional[float] = None
    conversion_significance: Optional[float] = None
    add_to_cart_significance: Optional[float] = None
    purchase_significance: Optional[float] = None
    revenue_significance: Optional[Dict[str, float]] = None
    updated_at: str
    """ Date and time when the A/B test was last updated, in RFC 3339 format. """
    created_at: str
    """ Date and time when the A/B test was created, in RFC 3339 format. """
    end_at: str
    """ End date and time of the A/B test, in RFC 3339 format. """
    name: str
    """ A/B test name. """
    status: Status
    variants: List[Variant]
    """ A/B test variants.  The first variant is your _control_ index, typically your production index. The second variant is an index with changed settings that you want to test against the control.  """
    configuration: Optional[ABTestConfiguration] = None

    model_config = ConfigDict(
        strict=False,
        use_enum_values=True,
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        alias_generator=_alias_generator,
        extra="allow",
    )

    def to_json(self) -> str:
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ABTest from a JSON string"""
        return cls.from_dict(loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias."""
        return self.model_dump(
            by_alias=True,
            exclude_none=True,
            exclude_unset=True,
        )

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ABTest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        obj["status"] = obj.get("status")
        obj["variants"] = (
            [Variant.from_dict(_item) for _item in obj["variants"]]
            if obj.get("variants") is not None
            else None
        )
        obj["configuration"] = (
            ABTestConfiguration.from_dict(obj["configuration"])
            if obj.get("configuration") is not None
            else None
        )

        return cls.model_validate(obj)
