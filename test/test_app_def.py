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
from jarviceapi_client.models.app_def import AppDef  # noqa: E501
from jarviceapi_client.rest import ApiException

class TestAppDef(unittest.TestCase):
    """AppDef unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AppDef
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppDef`
        """
        model = jarviceapi_client.models.app_def.AppDef()  # noqa: E501
        if include_optional :
            return AppDef(
                appdefversion = 56, 
                author = '', 
                certified = True, 
                classifications = [
                    ''
                    ], 
                commands = {
                    'key' : jarviceapi_client.models.app_def_cmd.AppDefCmd(
                        cmdscript = '', 
                        description = '', 
                        desktop = True, 
                        interactive = True, 
                        machines = [
                            ''
                            ], 
                        mpirun = True, 
                        name = '', 
                        noconnect = True, 
                        noqueue = True, 
                        parameters = {
                            'key' : jarviceapi_client.models.par_def.ParDef(
                                cmdscript = True, 
                                description = '', 
                                filter = '', 
                                if = [
                                    ''
                                    ], 
                                ifnot = [
                                    ''
                                    ], 
                                max = '', 
                                min = '', 
                                mvalues = [
                                    ''
                                    ], 
                                name = '', 
                                positional = True, 
                                required = True, 
                                size = '', 
                                step = '', 
                                target = '', 
                                type = '', 
                                value = jarviceapi_client.models.value.value(), 
                                values = [
                                    ''
                                    ], 
                                variable = True, )
                            }, 
                        path = '', 
                        ports = [
                            ''
                            ], 
                        publicip = True, 
                        scale_max = 56, 
                        url = '', 
                        variables = {
                            'key' : jarviceapi_client.models.variable.Variable(
                                description = '', 
                                inherit = True, 
                                name = '', 
                                required = True, 
                                userowned = True, )
                            }, 
                        verboseinit = True, 
                        walltime = '', 
                        webshell = True, )
                    }, 
                description = '', 
                enablehpc = True, 
                id = '', 
                identity = jarviceapi_client.models.app_def_ident.AppDefIdent(
                    gid = 56, 
                    group = '', 
                    uid = 56, 
                    username = '', ), 
                image = jarviceapi_client.models.app_def_image.AppDefImage(
                    data = '', 
                    type = '', ), 
                licensed = True, 
                machines = [
                    ''
                    ], 
                nae = '', 
                name = '', 
                owner = '', 
                price = '0', 
                public = True, 
                scale_max = 56, 
                team = True, 
                variables = {
                    'key' : jarviceapi_client.models.variable.Variable(
                        description = '', 
                        inherit = True, 
                        name = '', 
                        required = True, 
                        userowned = True, )
                    }, 
                vault_types = [
                    ''
                    ], 
                walltime = ''
            )
        else :
            return AppDef(
        )
        """

    def testAppDef(self):
        """Test AppDef"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()