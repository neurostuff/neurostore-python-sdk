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
from neurostore_sdk.model.analysis import Analysis
from neurostore_sdk.model.annotation import Annotation
from neurostore_sdk.model.note_collection_base import NoteCollectionBase
from neurostore_sdk.model.note_collection_relationships import NoteCollectionRelationships
globals()['Analysis'] = Analysis
globals()['Annotation'] = Annotation
globals()['NoteCollectionBase'] = NoteCollectionBase
globals()['NoteCollectionRelationships'] = NoteCollectionRelationships
from neurostore_sdk.model.note_collection import NoteCollection


class TestNoteCollection(unittest.TestCase):
    """NoteCollection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNoteCollection(self):
        """Test NoteCollection"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NoteCollection()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
