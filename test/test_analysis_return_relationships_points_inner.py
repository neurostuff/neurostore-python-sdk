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
from neurostore_sdk.models.analysis_return_relationships_points_inner import AnalysisReturnRelationshipsPointsInner  # noqa: E501
from neurostore_sdk.rest import ApiException

class TestAnalysisReturnRelationshipsPointsInner(unittest.TestCase):
    """AnalysisReturnRelationshipsPointsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AnalysisReturnRelationshipsPointsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AnalysisReturnRelationshipsPointsInner`
        """
        model = neurostore_sdk.models.analysis_return_relationships_points_inner.AnalysisReturnRelationshipsPointsInner()  # noqa: E501
        if include_optional :
            return AnalysisReturnRelationshipsPointsInner(
                coordinates = [
                    63
                    ], 
                space = 'MNI', 
                kind = '', 
                label_id = '', 
                created_at = '2021-01-16T20:50:38.009318Z', 
                updated_at = '', 
                id = '38jobTomPDqt', 
                public = True, 
                user = '', 
                image = '', 
                value = None, 
                x = 1.337, 
                y = 1.337, 
                z = 1.337, 
                entities = [
                    null
                    ], 
                analysis = ''
            )
        else :
            return AnalysisReturnRelationshipsPointsInner(
        )
        """

    def testAnalysisReturnRelationshipsPointsInner(self):
        """Test AnalysisReturnRelationshipsPointsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
