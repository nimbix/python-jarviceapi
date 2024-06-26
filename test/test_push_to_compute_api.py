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

import jarviceapi_client
from jarviceapi_client.api.push_to_compute_api import PushToComputeApi  # noqa: E501
from jarviceapi_client.rest import ApiException


class TestPushToComputeApi(unittest.TestCase):
    """PushToComputeApi unit test stubs"""

    def setUp(self):
        self.api = jarviceapi_client.api.push_to_compute_api.PushToComputeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_build_get(self):
        """Test case for build_get

        Builds a JARVICE application image for a Docker repository. The JARVICE application ID must already exist.  # noqa: E501
        """
        pass

    def test_history_get(self):
        """Test case for history_get

        Retrieve build/pull history for a JARVICE application image.  # noqa: E501
        """
        pass

    def test_pull_get(self):
        """Test case for pull_get

        Pulls a Docker repository into a JARVICE application image. The JARVICE application image must already exist.  # noqa: E501
        """
        pass

    def test_validate_post(self):
        """Test case for validate_post

        Validates an AppDef (application definition).  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
