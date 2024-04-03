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

from neurostore_sdk.models.annotation_return_relationships import AnnotationReturnRelationships

class TestAnnotationReturnRelationships(unittest.TestCase):
    """AnnotationReturnRelationships unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AnnotationReturnRelationships:
        """Test AnnotationReturnRelationships
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AnnotationReturnRelationships`
        """
        model = AnnotationReturnRelationships()
        if include_optional:
            return AnnotationReturnRelationships(
                notes = None
            )
        else:
            return AnnotationReturnRelationships(
        )
        """

    def testAnnotationReturnRelationships(self):
        """Test AnnotationReturnRelationships"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
