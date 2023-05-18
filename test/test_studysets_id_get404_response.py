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
from neurostore_sdk.models.studysets_id_get404_response import StudysetsIdGet404Response  # noqa: E501
from neurostore_sdk.rest import ApiException

class TestStudysetsIdGet404Response(unittest.TestCase):
    """StudysetsIdGet404Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StudysetsIdGet404Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StudysetsIdGet404Response`
        """
        model = neurostore_sdk.models.studysets_id_get404_response.StudysetsIdGet404Response()  # noqa: E501
        if include_optional :
            return StudysetsIdGet404Response(
                detail = '"The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."', 
                status = 404, 
                title = '"Not Found"', 
                type = '"about:blank"'
            )
        else :
            return StudysetsIdGet404Response(
        )
        """

    def testStudysetsIdGet404Response(self):
        """Test StudysetsIdGet404Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()