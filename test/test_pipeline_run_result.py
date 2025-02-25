# coding: utf-8

"""
    neurostore api

    Create studysets for meta-analysis

    The version of the OpenAPI document: 1.0
    Contact: jamesdkent21@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from neurostore_sdk.models.pipeline_run_result import PipelineRunResult

class TestPipelineRunResult(unittest.TestCase):
    """PipelineRunResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PipelineRunResult:
        """Test PipelineRunResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PipelineRunResult`
        """
        model = PipelineRunResult()
        if include_optional:
            return PipelineRunResult(
                id = '',
                pipeline_run_id = '',
                data = None
            )
        else:
            return PipelineRunResult(
        )
        """

    def testPipelineRunResult(self):
        """Test PipelineRunResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
