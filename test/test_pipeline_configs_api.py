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
from neurostore_sdk.api.pipeline_configs_api import PipelineConfigsApi  # noqa: E501
from neurostore_sdk.rest import ApiException


class TestPipelineConfigsApi(unittest.TestCase):
    """PipelineConfigsApi unit test stubs"""

    def setUp(self):
        self.api = neurostore_sdk.api.pipeline_configs_api.PipelineConfigsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_pipeline_configs_get(self):
        """Test case for pipeline_configs_get

        GET a list of pipeline configs  # noqa: E501
        """
        pass

    def test_pipeline_configs_id_delete(self):
        """Test case for pipeline_configs_id_delete

        DELETE a pipeline config by ID  # noqa: E501
        """
        pass

    def test_pipeline_configs_id_get(self):
        """Test case for pipeline_configs_id_get

        GET a pipeline config by ID  # noqa: E501
        """
        pass

    def test_pipeline_configs_id_put(self):
        """Test case for pipeline_configs_id_put

        PUT/update a pipeline config by ID  # noqa: E501
        """
        pass

    def test_pipeline_configs_post(self):
        """Test case for pipeline_configs_post

        POST/create a pipeline config  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
