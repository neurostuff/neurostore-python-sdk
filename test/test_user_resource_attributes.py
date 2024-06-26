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
from neurostore_sdk.models.user_resource_attributes import UserResourceAttributes  # noqa: E501
from neurostore_sdk.rest import ApiException

class TestUserResourceAttributes(unittest.TestCase):
    """UserResourceAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserResourceAttributes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserResourceAttributes`
        """
        model = neurostore_sdk.models.user_resource_attributes.UserResourceAttributes()  # noqa: E501
        if include_optional :
            return UserResourceAttributes(
                user = '', 
                username = ''
            )
        else :
            return UserResourceAttributes(
        )
        """

    def testUserResourceAttributes(self):
        """Test UserResourceAttributes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
