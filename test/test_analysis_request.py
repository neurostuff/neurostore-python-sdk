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
from neurostore_sdk.model.analysis_base import AnalysisBase
from neurostore_sdk.model.analysis_request_relationships import AnalysisRequestRelationships
from neurostore_sdk.model.condition_request import ConditionRequest
from neurostore_sdk.model.image_request import ImageRequest
from neurostore_sdk.model.point_request import PointRequest
from neurostore_sdk.model.writeable_resource_attributes import WriteableResourceAttributes
globals()['AnalysisBase'] = AnalysisBase
globals()['AnalysisRequestRelationships'] = AnalysisRequestRelationships
globals()['ConditionRequest'] = ConditionRequest
globals()['ImageRequest'] = ImageRequest
globals()['PointRequest'] = PointRequest
globals()['WriteableResourceAttributes'] = WriteableResourceAttributes
from neurostore_sdk.model.analysis_request import AnalysisRequest


class TestAnalysisRequest(unittest.TestCase):
    """AnalysisRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAnalysisRequest(self):
        """Test AnalysisRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AnalysisRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
