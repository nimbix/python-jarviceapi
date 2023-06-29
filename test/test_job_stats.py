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
from jarviceapi_client.models.job_stats import JobStats  # noqa: E501
from jarviceapi_client.rest import ApiException

class TestJobStats(unittest.TestCase):
    """JobStats unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JobStats
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JobStats`
        """
        model = jarviceapi_client.models.job_stats.JobStats()  # noqa: E501
        if include_optional :
            return JobStats(
                app_cost = 1.337, 
                compute_cost = 1.337, 
                compute_time = 56, 
                job_count = 56, 
                queue_time = 56, 
                wall_time = 56
            )
        else :
            return JobStats(
        )
        """

    def testJobStats(self):
        """Test JobStats"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()