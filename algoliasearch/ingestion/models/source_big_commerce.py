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


from algoliasearch.ingestion.models.big_commerce_channel import BigCommerceChannel
from algoliasearch.ingestion.models.big_commerce_metafield import BigCommerceMetafield

_ALIASES = {
    "store_hash": "storeHash",
    "channel": "channel",
    "custom_fields": "customFields",
    "product_metafields": "productMetafields",
    "variant_metafields": "variantMetafields",
}


def _alias_generator(name: str) -> str:
    return _ALIASES.get(name, name)


class SourceBigCommerce(BaseModel):
    """
    SourceBigCommerce
    """

    store_hash: str
    """ Store hash identifying your BigCommerce store. """
    channel: Optional[BigCommerceChannel] = None
    custom_fields: Optional[List[str]] = None
    product_metafields: Optional[List[BigCommerceMetafield]] = None
    variant_metafields: Optional[List[BigCommerceMetafield]] = None

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
        """Create an instance of SourceBigCommerce from a JSON string"""
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
        """Create an instance of SourceBigCommerce from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        obj["channel"] = (
            BigCommerceChannel.from_dict(obj["channel"])
            if obj.get("channel") is not None
            else None
        )
        obj["productMetafields"] = (
            [
                BigCommerceMetafield.from_dict(_item)
                for _item in obj["productMetafields"]
            ]
            if obj.get("productMetafields") is not None
            else None
        )
        obj["variantMetafields"] = (
            [
                BigCommerceMetafield.from_dict(_item)
                for _item in obj["variantMetafields"]
            ]
            if obj.get("variantMetafields") is not None
            else None
        )

        return cls.model_validate(obj)
