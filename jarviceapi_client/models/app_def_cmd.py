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


from typing import Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, conlist
from jarviceapi_client.models.par_def import ParDef
from jarviceapi_client.models.variable import Variable

class AppDefCmd(BaseModel):
    """
    AppDefCmd
    """
    cmdscript: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    desktop: Optional[StrictBool] = None
    interactive: Optional[StrictBool] = None
    machines: Optional[conlist(StrictStr)] = None
    mpirun: Optional[StrictBool] = None
    name: Optional[StrictStr] = None
    noconnect: Optional[StrictBool] = None
    noqueue: Optional[StrictBool] = None
    parameters: Optional[Dict[str, ParDef]] = None
    path: Optional[StrictStr] = None
    ports: Optional[conlist(StrictStr)] = None
    publicip: Optional[StrictBool] = None
    scale_max: Optional[StrictInt] = None
    url: Optional[StrictStr] = None
    variables: Optional[Dict[str, Variable]] = None
    verboseinit: Optional[StrictBool] = None
    walltime: Optional[StrictStr] = None
    webshell: Optional[StrictBool] = None
    __properties = ["cmdscript", "description", "desktop", "interactive", "machines", "mpirun", "name", "noconnect", "noqueue", "parameters", "path", "ports", "publicip", "scale_max", "url", "variables", "verboseinit", "walltime", "webshell"]

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
    def from_json(cls, json_str: str) -> AppDefCmd:
        """Create an instance of AppDefCmd from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in parameters (dict)
        _field_dict = {}
        if self.parameters:
            for _key in self.parameters:
                if self.parameters[_key]:
                    _field_dict[_key] = self.parameters[_key].to_dict()
            _dict['parameters'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in variables (dict)
        _field_dict = {}
        if self.variables:
            for _key in self.variables:
                if self.variables[_key]:
                    _field_dict[_key] = self.variables[_key].to_dict()
            _dict['variables'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AppDefCmd:
        """Create an instance of AppDefCmd from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AppDefCmd.parse_obj(obj)

        _obj = AppDefCmd.parse_obj({
            "cmdscript": obj.get("cmdscript"),
            "description": obj.get("description"),
            "desktop": obj.get("desktop"),
            "interactive": obj.get("interactive"),
            "machines": obj.get("machines"),
            "mpirun": obj.get("mpirun"),
            "name": obj.get("name"),
            "noconnect": obj.get("noconnect"),
            "noqueue": obj.get("noqueue"),
            "parameters": dict(
                (_k, ParDef.from_dict(_v))
                for _k, _v in obj.get("parameters").items()
            )
            if obj.get("parameters") is not None
            else None,
            "path": obj.get("path"),
            "ports": obj.get("ports"),
            "publicip": obj.get("publicip"),
            "scale_max": obj.get("scale_max"),
            "url": obj.get("url"),
            "variables": dict(
                (_k, Variable.from_dict(_v))
                for _k, _v in obj.get("variables").items()
            )
            if obj.get("variables") is not None
            else None,
            "verboseinit": obj.get("verboseinit"),
            "walltime": obj.get("walltime"),
            "webshell": obj.get("webshell")
        })
        return _obj

