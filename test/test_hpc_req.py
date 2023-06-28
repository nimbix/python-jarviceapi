# coding: utf-8

"""
    Jarvice API

    The JARVICE API allows full control on running jobs as well as managing applications via PushToCompute™.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@nimbix.net
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import openapi_client
from openapi_client.models.hpc_req import HpcReq  # noqa: E501
from openapi_client.rest import ApiException

class TestHpcReq(unittest.TestCase):
    """HpcReq unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test HpcReq
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HpcReq`
        """
        model = openapi_client.models.hpc_req.HpcReq()  # noqa: E501
        if include_optional :
            return HpcReq(
                hpc_envs = {
                    'key' : ''
                    }, 
                hpc_job_env_config = '', 
                hpc_job_script = '', 
                hpc_job_shell = '', 
                hpc_queue = '', 
                hpc_resources = {
                    'key' : ''
                    }, 
                hpc_umask = 56
            )
        else :
            return HpcReq(
        )
        """

    def testHpcReq(self):
        """Test HpcReq"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
