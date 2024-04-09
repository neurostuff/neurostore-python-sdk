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
import datetime

import neurostore_sdk
from neurostore_sdk.models.note_collection_base import NoteCollectionBase  # noqa: E501
from neurostore_sdk.rest import ApiException

class TestNoteCollectionBase(unittest.TestCase):
    """NoteCollectionBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NoteCollectionBase
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NoteCollectionBase`
        """
        model = neurostore_sdk.models.note_collection_base.NoteCollectionBase()  # noqa: E501
        if include_optional :
            return NoteCollectionBase(
                note = neurostore_sdk.models.note.note()
            )
        else :
            return NoteCollectionBase(
        )
        """

    def testNoteCollectionBase(self):
        """Test NoteCollectionBase"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
