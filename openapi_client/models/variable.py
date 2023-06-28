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


from typing import Optional
from pydantic import BaseModel, StrictBool, StrictStr

class Variable(BaseModel):
    """
    Variable
    """
    description: Optional[StrictStr] = None
    inherit: Optional[StrictBool] = None
    name: Optional[StrictStr] = None
    required: Optional[StrictBool] = None
    userowned: Optional[StrictBool] = None
    __properties = ["description", "inherit", "name", "required", "userowned"]

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
    def from_json(cls, json_str: str) -> Variable:
        """Create an instance of Variable from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Variable:
        """Create an instance of Variable from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Variable.parse_obj(obj)

        _obj = Variable.parse_obj({
            "description": obj.get("description"),
            "inherit": obj.get("inherit"),
            "name": obj.get("name"),
            "required": obj.get("required"),
            "userowned": obj.get("userowned")
        })
        return _obj

