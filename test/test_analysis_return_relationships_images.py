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

from neurostore_sdk.models.analysis_return_relationships_images import AnalysisReturnRelationshipsImages

class TestAnalysisReturnRelationshipsImages(unittest.TestCase):
    """AnalysisReturnRelationshipsImages unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AnalysisReturnRelationshipsImages:
        """Test AnalysisReturnRelationshipsImages
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AnalysisReturnRelationshipsImages`
        """
        model = AnalysisReturnRelationshipsImages()
        if include_optional:
            return AnalysisReturnRelationshipsImages(
            )
        else:
            return AnalysisReturnRelationshipsImages(
        )
        """

    def testAnalysisReturnRelationshipsImages(self):
        """Test AnalysisReturnRelationshipsImages"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
