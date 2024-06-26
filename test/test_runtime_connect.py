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

import jarviceapi_client
from jarviceapi_client.models.runtime_connect import RuntimeConnect  # noqa: E501
from jarviceapi_client.rest import ApiException

class TestRuntimeConnect(unittest.TestCase):
    """RuntimeConnect unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RuntimeConnect
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RuntimeConnect`
        """
        model = jarviceapi_client.models.runtime_connect.RuntimeConnect()  # noqa: E501
        if include_optional :
            return RuntimeConnect(
                address = '', 
                password = ''
            )
        else :
            return RuntimeConnect(
        )
        """

    def testRuntimeConnect(self):
        """Test RuntimeConnect"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
