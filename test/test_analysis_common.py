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
from neurostore_sdk.models.analysis_common import AnalysisCommon  # noqa: E501
from neurostore_sdk.rest import ApiException

class TestAnalysisCommon(unittest.TestCase):
    """AnalysisCommon unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AnalysisCommon
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AnalysisCommon`
        """
        model = neurostore_sdk.models.analysis_common.AnalysisCommon()  # noqa: E501
        if include_optional :
            return AnalysisCommon(
                study = '', 
                entities = [
                    neurostore_sdk.models.entity.entity(
                        label = '', 
                        level = '', 
                        analysis = '', )
                    ], 
                order = 56
            )
        else :
            return AnalysisCommon(
        )
        """

    def testAnalysisCommon(self):
        """Test AnalysisCommon"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
