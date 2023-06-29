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
from jarviceapi_client.models.job_obj import JobObj  # noqa: E501
from jarviceapi_client.rest import ApiException

class TestJobObj(unittest.TestCase):
    """JobObj unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JobObj
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JobObj`
        """
        model = jarviceapi_client.models.job_obj.JobObj()  # noqa: E501
        if include_optional :
            return JobObj(
                app = '', 
                app_owner = '', 
                appdefversion = 56, 
                arch = '', 
                cmdargs = [
                    ''
                    ], 
                cmdargtypes = [
                    ''
                    ], 
                cmdscript = '', 
                command_line = '', 
                command_name = '', 
                cores = 56, 
                ctrsecret = '', 
                desktop = True, 
                devices = [
                    ''
                    ], 
                geometry = '', 
                gpus = 56, 
                hpc_envs = {
                    'key' : ''
                    }, 
                identity = jarviceapi_client.models.app_def_ident.AppDefIdent(
                    gid = 56, 
                    group = '', 
                    uid = 56, 
                    username = '', ), 
                interactive = True, 
                ipaddr = '', 
                job_label = '', 
                job_project = '', 
                jobtoken = '', 
                licenses = '', 
                machine = '', 
                memlimit = 56, 
                mpirun = True, 
                nae = '', 
                noconnect = True, 
                nodes = 56, 
                nopasssubt = True, 
                ports = [
                    ''
                    ], 
                privileged = True, 
                properties = [
                    ''
                    ], 
                publicip = True, 
                ram = 56, 
                repo = '', 
                scratch = 56, 
                slave_cores = 56, 
                slave_gpus = 56, 
                slave_properties = [
                    ''
                    ], 
                slave_ram = 56, 
                slave_scratch = 56, 
                slots = 56, 
                sshpriv = '', 
                sshpub = '', 
                upload = jarviceapi_client.models.job_upload.JobUpload(
                    data = '', 
                    size = 56, 
                    target = '', ), 
                url = '', 
                user = '', 
                variables = {
                    'key' : ''
                    }, 
                variabletypes = {
                    'key' : ''
                    }, 
                vault = jarviceapi_client.models.job_obj_vault.JobObjVault(
                    auth = '', 
                    domain = '', 
                    force = True, 
                    global = jarviceapi_client.models.model_dict.ModelDict(), 
                    name = '', 
                    ro = True, ), 
                verboseinit = True, 
                vmemlimit = 56, 
                walltime = '', 
                webshell = True
            )
        else :
            return JobObj(
        )
        """

    def testJobObj(self):
        """Test JobObj"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()