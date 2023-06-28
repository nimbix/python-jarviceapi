# coding: utf-8

"""
    Jarvice API

    The JARVICE API allows full control on running jobs as well as managing applications via PushToCompute™.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@nimbix.net
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr

class JobObjVault(BaseModel):
    """
    JobObjVault
    """
    auth: Optional[StrictStr] = None
    domain: Optional[StrictStr] = None
    force: Optional[StrictBool] = None
    var_global: Optional[Dict[str, Any]] = Field(None, alias="global")
    name: Optional[StrictStr] = None
    ro: Optional[StrictBool] = None
    __properties = ["auth", "domain", "force", "global", "name", "ro"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> JobObjVault:
        """Create an instance of JobObjVault from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> JobObjVault:
        """Create an instance of JobObjVault from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return JobObjVault.parse_obj(obj)

        _obj = JobObjVault.parse_obj({
            "auth": obj.get("auth"),
            "domain": obj.get("domain"),
            "force": obj.get("force"),
            "var_global": obj.get("global"),
            "name": obj.get("name"),
            "ro": obj.get("ro")
        })
        return _obj

