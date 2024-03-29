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

import neurostore_sdk
from neurostore_sdk.api.conditions_api import ConditionsApi  # noqa: E501
from neurostore_sdk.rest import ApiException


class TestConditionsApi(unittest.TestCase):
    """ConditionsApi unit test stubs"""

    def setUp(self):
        self.api = neurostore_sdk.api.conditions_api.ConditionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_conditions_get(self):
        """Test case for conditions_get

        GET Conditions  # noqa: E501
        """
        pass

    def test_conditions_id_delete(self):
        """Test case for conditions_id_delete

        DELETE a condition  # noqa: E501
        """
        pass

    def test_conditions_id_get(self):
        """Test case for conditions_id_get

        GET a condition  # noqa: E501
        """
        pass

    def test_conditions_id_put(self):
        """Test case for conditions_id_put

        PUT/update a condition  # noqa: E501
        """
        pass

    def test_conditions_post(self):
        """Test case for conditions_post

        POST/Create a condition  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
