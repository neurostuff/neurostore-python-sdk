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
from neurostore_sdk.models.image_return import ImageReturn  # noqa: E501
from neurostore_sdk.rest import ApiException

class TestImageReturn(unittest.TestCase):
    """ImageReturn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ImageReturn
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImageReturn`
        """
        model = neurostore_sdk.models.image_return.ImageReturn()  # noqa: E501
        if include_optional :
            return ImageReturn(
                metadata = neurostore_sdk.models.metadata.metadata(), 
                url = 'https://neurovault.org/media/images/4778/Positive_RPEs_zstat.nii.gz', 
                filename = 'Positive_RPEs_zstat.nii.gz', 
                space = 'MNI152NLin2009aAsym', 
                value_type = 'Z', 
                add_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                analysis = '', 
                entities = [
                    neurostore_sdk.models.entity.entity(
                        label = '', 
                        level = '', 
                        analysis = '', )
                    ], 
                analysis_name = '', 
                created_at = '2021-01-16T20:50:38.009318Z', 
                updated_at = '', 
                id = '38jobTomPDqt', 
                public = True, 
                user = '', 
                username = ''
            )
        else :
            return ImageReturn(
        )
        """

    def testImageReturn(self):
        """Test ImageReturn"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
