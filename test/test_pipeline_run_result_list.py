# coding: utf-8

"""
    neurostore api

    Create studysets for meta-analysis  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: jamesdkent21@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import neurostore_sdk
from neurostore_sdk.models.pipeline_run_result_list import PipelineRunResultList  # noqa: E501
from neurostore_sdk.rest import ApiException

class TestPipelineRunResultList(unittest.TestCase):
    """PipelineRunResultList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PipelineRunResultList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PipelineRunResultList`
        """
        model = neurostore_sdk.models.pipeline_run_result_list.PipelineRunResultList()  # noqa: E501
        if include_optional :
            return PipelineRunResultList(
                results = [
                    neurostore_sdk.models.pipeline_run_result.pipeline-run-result(
                        id = '', 
                        pipeline_run_id = '', 
                        data = neurostore_sdk.models.data.data(), )
                    ], 
                metadata = neurostore_sdk.models.metadata.metadata(
                    total_count = 56, 
                    unique_count = 56, )
            )
        else :
            return PipelineRunResultList(
        )
        """

    def testPipelineRunResultList(self):
        """Test PipelineRunResultList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()