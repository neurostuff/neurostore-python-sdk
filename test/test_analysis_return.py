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
from neurostore_sdk.models.analysis_return import AnalysisReturn  # noqa: E501
from neurostore_sdk.rest import ApiException

class TestAnalysisReturn(unittest.TestCase):
    """AnalysisReturn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AnalysisReturn
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AnalysisReturn`
        """
        model = neurostore_sdk.models.analysis_return.AnalysisReturn()  # noqa: E501
        if include_optional :
            return AnalysisReturn(
                name = '"houses>faces"', 
                description = 'This analysis represents a contrast of houses versus faces.', 
                weights = [
                    1
                    ], 
                created_at = '2021-01-16T20:50:38.009318Z', 
                updated_at = '', 
                id = '38jobTomPDqt', 
                public = True, 
                user = '', 
                username = '', 
                study = '', 
                images = None, 
                points = None, 
                conditions = None, 
                entities = [
                    neurostore_sdk.models.entity.entity(
                        label = '', 
                        level = '', 
                        analysis = '', )
                    ], 
                order = 56
            )
        else :
            return AnalysisReturn(
        )
        """

    def testAnalysisReturn(self):
        """Test AnalysisReturn"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
