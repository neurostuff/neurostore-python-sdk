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
from neurostore_sdk.model.metadata import Metadata
from neurostore_sdk.model.studyset_return import StudysetReturn
globals()['Metadata'] = Metadata
globals()['StudysetReturn'] = StudysetReturn
from neurostore_sdk.model.studyset_list import StudysetList


class TestStudysetList(unittest.TestCase):
    """StudysetList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStudysetList(self):
        """Test StudysetList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = StudysetList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
