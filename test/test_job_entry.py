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
from jarviceapi_client.models.job_entry import JobEntry  # noqa: E501
from jarviceapi_client.rest import ApiException

class TestJobEntry(unittest.TestCase):
    """JobEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JobEntry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JobEntry`
        """
        model = jarviceapi_client.models.job_entry.JobEntry()  # noqa: E501
        if include_optional :
            return JobEntry(
                job_address = '', 
                job_after = '', 
                job_api_submission = jarviceapi_client.models.submission.Submission(
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
                        readonly = True, ), ), 
                job_app_discount = 56, 
                job_app_price = 1.337, 
                job_application = '', 
                job_billed = True, 
                job_billing_code = 56, 
                job_command = '', 
                job_dashboard_visible = 56, 
                job_end_time = 56, 
                job_exitcode = 56, 
                job_label = '', 
                job_mc_discount = 56, 
                job_mc_name = '', 
                job_mc_scale = 56, 
                job_name = '', 
                job_nodes = '', 
                job_number = 56, 
                job_owner_username = '', 
                job_payer = '', 
                job_price = 1.337, 
                job_sched_id = 56, 
                job_sched_job_id = '', 
                job_start_time = 56, 
                job_stats = jarviceapi_client.models.job_stats.JobStats(
                    app_cost = 1.337, 
                    compute_cost = 1.337, 
                    compute_time = 56, 
                    job_count = 56, 
                    queue_time = 56, 
                    wall_time = 56, ), 
                job_status = '', 
                job_submit_time = 56, 
                job_substatus = 56, 
                job_substatus_text = '', 
                job_walltime = ''
            )
        else :
            return JobEntry(
        )
        """

    def testJobEntry(self):
        """Test JobEntry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
