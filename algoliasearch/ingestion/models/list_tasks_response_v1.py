# coding: utf-8

"""
Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
"""

from __future__ import annotations

from json import loads
from sys import version_info
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

if version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


from algoliasearch.ingestion.models.pagination import Pagination
from algoliasearch.ingestion.models.task_v1 import TaskV1


class ListTasksResponseV1(BaseModel):
    """
    Configured tasks and pagination information.
    """

    tasks: List[TaskV1] = Field(alias="tasks")
    pagination: Pagination = Field(alias="pagination")

    model_config = ConfigDict(
        use_enum_values=True,
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_json(self) -> str:
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ListTasksResponseV1 from a JSON string"""
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
        """Create an instance of ListTasksResponseV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        obj["tasks"] = (
            [TaskV1.from_dict(_item) for _item in obj["tasks"]]
            if obj.get("tasks") is not None
            else None
        )
        obj["pagination"] = (
            Pagination.from_dict(obj["pagination"])
            if obj.get("pagination") is not None
            else None
        )

        return cls.model_validate(obj)
