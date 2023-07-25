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


from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist

class ParDef(BaseModel):
    """
    ParDef
    """
    cmdscript: Optional[StrictBool] = None
    description: Optional[StrictStr] = None
    filter: Optional[StrictStr] = None
    var_if: Optional[conlist(StrictStr)] = Field(None, alias="if")
    ifnot: Optional[conlist(StrictStr)] = None
    max: Optional[Any] = None
    min: Optional[Any] = None
    mvalues: Optional[conlist(StrictStr)] = None
    name: Optional[StrictStr] = None
    positional: Optional[StrictBool] = None
    required: Optional[StrictBool] = None
    size: Optional[StrictStr] = None
    step: Optional[StrictStr] = None
    target: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    value: Optional[Any] = None
    values: Optional[conlist(StrictStr)] = None
    variable: Optional[StrictBool] = None
    __properties = ["cmdscript", "description", "filter", "if", "ifnot", "max", "min", "mvalues", "name", "positional", "required", "size", "step", "target", "type", "value", "values", "variable"]

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
    def from_json(cls, json_str: str) -> ParDef:
        """Create an instance of ParDef from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if max (nullable) is None
        # and __fields_set__ contains the field
        if self.max is None and "max" in self.__fields_set__:
            _dict['max'] = None

        # set to None if min (nullable) is None
        # and __fields_set__ contains the field
        if self.min is None and "min" in self.__fields_set__:
            _dict['min'] = None

        # set to None if value (nullable) is None
        # and __fields_set__ contains the field
        if self.value is None and "value" in self.__fields_set__:
            _dict['value'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ParDef:
        """Create an instance of ParDef from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ParDef.parse_obj(obj)

        _obj = ParDef.parse_obj({
            "cmdscript": obj.get("cmdscript"),
            "description": obj.get("description"),
            "filter": obj.get("filter"),
            "var_if": obj.get("if"),
            "ifnot": obj.get("ifnot"),
            "max": obj.get("max"),
            "min": obj.get("min"),
            "mvalues": obj.get("mvalues"),
            "name": obj.get("name"),
            "positional": obj.get("positional"),
            "required": obj.get("required"),
            "size": obj.get("size"),
            "step": obj.get("step"),
            "target": obj.get("target"),
            "type": obj.get("type"),
            "value": obj.get("value"),
            "values": obj.get("values"),
            "variable": obj.get("variable")
        })
        return _obj

