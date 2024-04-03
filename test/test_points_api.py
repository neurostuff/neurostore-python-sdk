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

from neurostore_sdk.api.points_api import PointsApi


class TestPointsApi(unittest.TestCase):
    """PointsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PointsApi()

    def tearDown(self) -> None:
        pass

    def test_points_get(self) -> None:
        """Test case for points_get

        Get Points
        """
        pass

    def test_points_id_delete(self) -> None:
        """Test case for points_id_delete

        DELETE a point
        """
        pass

    def test_points_id_get(self) -> None:
        """Test case for points_id_get

        GET a point
        """
        pass

    def test_points_id_put(self) -> None:
        """Test case for points_id_put

        PUT/update a point
        """
        pass

    def test_points_post(self) -> None:
        """Test case for points_post

        POST Points
        """
        pass


if __name__ == '__main__':
    unittest.main()
