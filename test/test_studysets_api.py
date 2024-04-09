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
from neurostore_sdk.api.studysets_api import StudysetsApi  # noqa: E501
from neurostore_sdk.rest import ApiException


class TestStudysetsApi(unittest.TestCase):
    """StudysetsApi unit test stubs"""

    def setUp(self):
        self.api = neurostore_sdk.api.studysets_api.StudysetsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_studysets_get(self):
        """Test case for studysets_get

        GET a list of studysets  # noqa: E501
        """
        pass

    def test_studysets_id_delete(self):
        """Test case for studysets_id_delete

        DELETE a studyset  # noqa: E501
        """
        pass

    def test_studysets_id_get(self):
        """Test case for studysets_id_get

        GET a studyset  # noqa: E501
        """
        pass

    def test_studysets_id_put(self):
        """Test case for studysets_id_put

        PUT/update a studyset  # noqa: E501
        """
        pass

    def test_studysets_post(self):
        """Test case for studysets_post

        POST/create a studyset  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
