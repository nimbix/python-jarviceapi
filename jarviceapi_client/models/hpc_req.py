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


from typing import Dict, Optional
from pydantic import BaseModel, StrictInt, StrictStr

class HpcReq(BaseModel):
    """
    HpcReq
    """
    hpc_envs: Optional[Dict[str, StrictStr]] = None
    hpc_job_env_config: Optional[StrictStr] = None
    hpc_job_script: Optional[StrictStr] = None
    hpc_job_shell: Optional[StrictStr] = None
    hpc_queue: Optional[StrictStr] = None
    hpc_resources: Optional[Dict[str, StrictStr]] = None
    hpc_umask: Optional[StrictInt] = None
    __properties = ["hpc_envs", "hpc_job_env_config", "hpc_job_script", "hpc_job_shell", "hpc_queue", "hpc_resources", "hpc_umask"]

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
    def from_json(cls, json_str: str) -> HpcReq:
        """Create an instance of HpcReq from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HpcReq:
        """Create an instance of HpcReq from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HpcReq.parse_obj(obj)

        _obj = HpcReq.parse_obj({
            "hpc_envs": obj.get("hpc_envs"),
            "hpc_job_env_config": obj.get("hpc_job_env_config"),
            "hpc_job_script": obj.get("hpc_job_script"),
            "hpc_job_shell": obj.get("hpc_job_shell"),
            "hpc_queue": obj.get("hpc_queue"),
            "hpc_resources": obj.get("hpc_resources"),
            "hpc_umask": obj.get("hpc_umask")
        })
        return _obj

