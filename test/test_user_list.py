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

from neurostore_sdk.models.user_list import UserList

class TestUserList(unittest.TestCase):
    """UserList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserList:
        """Test UserList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserList`
        """
        model = UserList()
        if include_optional:
            return UserList(
                results = [
                    neurostore_sdk.models.user.user(
                        name = '', 
                        neuroid = '', )
                    ],
                metadata = neurostore_sdk.models.metadata.metadata(
                    total_count = 56, 
                    unique_count = 56, )
            )
        else:
            return UserList(
        )
        """

    def testUserList(self):
        """Test UserList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
