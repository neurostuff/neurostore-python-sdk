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
from neurostore_sdk.model.study_return import StudyReturn
globals()['Metadata'] = Metadata
globals()['StudyReturn'] = StudyReturn
from neurostore_sdk.model.study_list import StudyList


class TestStudyList(unittest.TestCase):
    """StudyList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStudyList(self):
        """Test StudyList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = StudyList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
