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
from neurostore_sdk.models.base_studies_post200_response import BaseStudiesPost200Response  # noqa: E501
from neurostore_sdk.rest import ApiException

class TestBaseStudiesPost200Response(unittest.TestCase):
    """BaseStudiesPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BaseStudiesPost200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BaseStudiesPost200Response`
        """
        model = neurostore_sdk.models.base_studies_post200_response.BaseStudiesPost200Response()  # noqa: E501
        if include_optional :
            return BaseStudiesPost200Response(
                metadata = neurostore_sdk.models.metadata.metadata(), 
                versions = None, 
                name = '', 
                description = '', 
                publication = '', 
                doi = '', 
                pmid = '', 
                authors = '', 
                year = 56, 
                level = '', 
                created_at = '2021-01-16T20:50:38.009318Z', 
                updated_at = '', 
                id = '38jobTomPDqt', 
                public = True, 
                user = ''
            )
        else :
            return BaseStudiesPost200Response(
        )
        """

    def testBaseStudiesPost200Response(self):
        """Test BaseStudiesPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
