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

from neurostore_sdk.models.userless_resource_attributes import UserlessResourceAttributes

class TestUserlessResourceAttributes(unittest.TestCase):
    """UserlessResourceAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserlessResourceAttributes:
        """Test UserlessResourceAttributes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserlessResourceAttributes`
        """
        model = UserlessResourceAttributes()
        if include_optional:
            return UserlessResourceAttributes(
                created_at = '2021-01-16T20:50:38.009318Z',
                updated_at = '',
                id = '38jobTomPDqt',
                public = True
            )
        else:
            return UserlessResourceAttributes(
        )
        """

    def testUserlessResourceAttributes(self):
        """Test UserlessResourceAttributes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
