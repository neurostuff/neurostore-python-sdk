"""
    neurostore api

    Create studysets for meta-analysis  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: jamesdkent21@gmail.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import neurostore_sdk
from neurostore_sdk.model.condition import Condition
from neurostore_sdk.model.image import Image
from neurostore_sdk.model.point import Point
from neurostore_sdk.model.read_only import ReadOnly
globals()['Condition'] = Condition
globals()['Image'] = Image
globals()['Point'] = Point
globals()['ReadOnly'] = ReadOnly
from neurostore_sdk.model.analysis import Analysis


class TestAnalysis(unittest.TestCase):
    """Analysis unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAnalysis(self):
        """Test Analysis"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Analysis()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
