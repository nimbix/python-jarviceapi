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
from jarviceapi_client.models.submission import Submission  # noqa: E501
from jarviceapi_client.rest import ApiException

class TestSubmission(unittest.TestCase):
    """Submission unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Submission
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Submission`
        """
        model = jarviceapi_client.models.submission.Submission()  # noqa: E501
        if include_optional :
            return Submission(
                app = '', 
                application = jarviceapi_client.models.application.Application(
                    command = '', 
                    geometry = '', 
                    ipaddr = '', 
                    nosubmit = True, 
                    parameters = jarviceapi_client.models.model_dict.ModelDict(), 
                    walltime = '', ), 
                container = jarviceapi_client.models.container.Container(
                    image = '', 
                    interactive = True, 
                    jobscript = '', 
                    pullsecret = '', ), 
                gen_sshkey = True, 
                hpc = jarviceapi_client.models.hpc_req.HpcReq(
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
                    hpc_umask = 56, ), 
                identity = jarviceapi_client.models.app_def_ident.AppDefIdent(
                    gid = 56, 
                    group = '', 
                    uid = 56, 
                    username = '', ), 
                job_label = '', 
                job_project = '', 
                jobsub = '', 
                licenses = '', 
                machine = jarviceapi_client.models.machine.Machine(
                    nodes = 56, 
                    type = '', ), 
                nopasssubt = True, 
                public_ip = True, 
                queue = '', 
                test_comment = '', 
                user = jarviceapi_client.models.submit_user.SubmitUser(
                    apikey = '', 
                    username = '', ), 
                vault = jarviceapi_client.models.vault.Vault(
                    bucket = '', 
                    confirm = '', 
                    domain = '', 
                    force = True, 
                    name = '', 
                    objects = [
                        ''
                        ], 
                    password = '', 
                    readonly = True, )
            )
        else :
            return Submission(
        )
        """

    def testSubmission(self):
        """Test Submission"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
