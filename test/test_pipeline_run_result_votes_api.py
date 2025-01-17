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

import neurostore_sdk
from neurostore_sdk.api.pipeline_run_result_votes_api import PipelineRunResultVotesApi  # noqa: E501
from neurostore_sdk.rest import ApiException


class TestPipelineRunResultVotesApi(unittest.TestCase):
    """PipelineRunResultVotesApi unit test stubs"""

    def setUp(self):
        self.api = neurostore_sdk.api.pipeline_run_result_votes_api.PipelineRunResultVotesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_pipeline_run_result_votes_get(self):
        """Test case for pipeline_run_result_votes_get

        GET a list of pipeline run result votes  # noqa: E501
        """
        pass

    def test_pipeline_run_result_votes_pipeline_run_result_vote_id_delete(self):
        """Test case for pipeline_run_result_votes_pipeline_run_result_vote_id_delete

        DELETE a pipeline run result vote by ID  # noqa: E501
        """
        pass

    def test_pipeline_run_result_votes_pipeline_run_result_vote_id_get(self):
        """Test case for pipeline_run_result_votes_pipeline_run_result_vote_id_get

        GET a pipeline run result vote by ID  # noqa: E501
        """
        pass

    def test_pipeline_run_result_votes_pipeline_run_result_vote_id_put(self):
        """Test case for pipeline_run_result_votes_pipeline_run_result_vote_id_put

        PUT/update a pipeline run result vote by ID  # noqa: E501
        """
        pass

    def test_pipeline_run_result_votes_post(self):
        """Test case for pipeline_run_result_votes_post

        POST/create a pipeline run result vote  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()