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
from neurostore_sdk.models.annotation_return_one_of1 import AnnotationReturnOneOf1  # noqa: E501
from neurostore_sdk.rest import ApiException

class TestAnnotationReturnOneOf1(unittest.TestCase):
    """AnnotationReturnOneOf1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AnnotationReturnOneOf1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AnnotationReturnOneOf1`
        """
        model = neurostore_sdk.models.annotation_return_one_of1.AnnotationReturnOneOf1()  # noqa: E501
        if include_optional :
            return AnnotationReturnOneOf1(
                name = 'Examination of left versus right finger tapping', 
                description = 'This annotation tracks whether the analysis of interest for all included studies are left handed/right handed, or bimanual taps.', 
                metadata = neurostore_sdk.models.metadata.metadata(), 
                note_keys = {include=boolean}, 
                created_at = '2021-01-16T20:50:38.009318Z', 
                updated_at = '', 
                id = '38jobTomPDqt', 
                public = True, 
                user = '', 
                username = '', 
                source = '', 
                source_id = '', 
                source_updated_at = '', 
                notes = None, 
                studyset = ''
            )
        else :
            return AnnotationReturnOneOf1(
        )
        """

    def testAnnotationReturnOneOf1(self):
        """Test AnnotationReturnOneOf1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
