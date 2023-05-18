# coding: utf-8

# flake8: noqa
"""
    neurostore api

    Create studysets for meta-analysis  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: jamesdkent21@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


# import models into model package
from neurostore_sdk.models.analysis_base import AnalysisBase
from neurostore_sdk.models.analysis_common import AnalysisCommon
from neurostore_sdk.models.analysis_list import AnalysisList
from neurostore_sdk.models.analysis_request import AnalysisRequest
from neurostore_sdk.models.analysis_request_relationships import AnalysisRequestRelationships
from neurostore_sdk.models.analysis_request_relationships_conditions_inner import AnalysisRequestRelationshipsConditionsInner
from neurostore_sdk.models.analysis_request_relationships_images_inner import AnalysisRequestRelationshipsImagesInner
from neurostore_sdk.models.analysis_request_relationships_points_inner import AnalysisRequestRelationshipsPointsInner
from neurostore_sdk.models.analysis_return import AnalysisReturn
from neurostore_sdk.models.analysis_return_relationships import AnalysisReturnRelationships
from neurostore_sdk.models.analysis_return_relationships_conditions_inner import AnalysisReturnRelationshipsConditionsInner
from neurostore_sdk.models.analysis_return_relationships_images_inner import AnalysisReturnRelationshipsImagesInner
from neurostore_sdk.models.analysis_return_relationships_points_inner import AnalysisReturnRelationshipsPointsInner
from neurostore_sdk.models.annotation_base import AnnotationBase
from neurostore_sdk.models.annotation_common import AnnotationCommon
from neurostore_sdk.models.annotation_export import AnnotationExport
from neurostore_sdk.models.annotation_list import AnnotationList
from neurostore_sdk.models.annotation_request import AnnotationRequest
from neurostore_sdk.models.annotation_request_one_of import AnnotationRequestOneOf
from neurostore_sdk.models.annotation_request_relationships import AnnotationRequestRelationships
from neurostore_sdk.models.annotation_request_relationships_notes_inner import AnnotationRequestRelationshipsNotesInner
from neurostore_sdk.models.annotation_return import AnnotationReturn
from neurostore_sdk.models.annotation_return_one_of import AnnotationReturnOneOf
from neurostore_sdk.models.annotation_return_one_of1 import AnnotationReturnOneOf1
from neurostore_sdk.models.annotation_return_relationships import AnnotationReturnRelationships
from neurostore_sdk.models.annotation_return_relationships_notes_inner import AnnotationReturnRelationshipsNotesInner
from neurostore_sdk.models.clone import Clone
from neurostore_sdk.models.condition_base import ConditionBase
from neurostore_sdk.models.condition_list import ConditionList
from neurostore_sdk.models.condition_request import ConditionRequest
from neurostore_sdk.models.condition_return import ConditionReturn
from neurostore_sdk.models.entity import Entity
from neurostore_sdk.models.entity_all_of import EntityAllOf
from neurostore_sdk.models.image_base import ImageBase
from neurostore_sdk.models.image_common import ImageCommon
from neurostore_sdk.models.image_list import ImageList
from neurostore_sdk.models.image_relationships import ImageRelationships
from neurostore_sdk.models.image_request import ImageRequest
from neurostore_sdk.models.image_return import ImageReturn
from neurostore_sdk.models.json_ld import JsonLd
from neurostore_sdk.models.json_ld_context import JsonLdContext
from neurostore_sdk.models.metadata import Metadata
from neurostore_sdk.models.nested_put_attributes import NestedPutAttributes
from neurostore_sdk.models.note_collection_base import NoteCollectionBase
from neurostore_sdk.models.note_collection_request import NoteCollectionRequest
from neurostore_sdk.models.note_collection_return import NoteCollectionReturn
from neurostore_sdk.models.note_collection_return_all_of import NoteCollectionReturnAllOf
from neurostore_sdk.models.point_base import PointBase
from neurostore_sdk.models.point_common import PointCommon
from neurostore_sdk.models.point_list import PointList
from neurostore_sdk.models.point_relationships import PointRelationships
from neurostore_sdk.models.point_relationships_value import PointRelationshipsValue
from neurostore_sdk.models.point_request import PointRequest
from neurostore_sdk.models.point_return import PointReturn
from neurostore_sdk.models.point_value import PointValue
from neurostore_sdk.models.readable_resource_attributes import ReadableResourceAttributes
from neurostore_sdk.models.resource_attributes import ResourceAttributes
from neurostore_sdk.models.study_base import StudyBase
from neurostore_sdk.models.study_list import StudyList
from neurostore_sdk.models.study_request import StudyRequest
from neurostore_sdk.models.study_request_relationships import StudyRequestRelationships
from neurostore_sdk.models.study_request_relationships_analyses_inner import StudyRequestRelationshipsAnalysesInner
from neurostore_sdk.models.study_return import StudyReturn
from neurostore_sdk.models.study_return_all_of import StudyReturnAllOf
from neurostore_sdk.models.study_return_all_of_studysets import StudyReturnAllOfStudysets
from neurostore_sdk.models.study_return_relationships import StudyReturnRelationships
from neurostore_sdk.models.study_return_relationships_analyses_inner import StudyReturnRelationshipsAnalysesInner
from neurostore_sdk.models.studyset_base import StudysetBase
from neurostore_sdk.models.studyset_list import StudysetList
from neurostore_sdk.models.studyset_request import StudysetRequest
from neurostore_sdk.models.studyset_request_relationships import StudysetRequestRelationships
from neurostore_sdk.models.studyset_request_relationships_studies_inner import StudysetRequestRelationshipsStudiesInner
from neurostore_sdk.models.studyset_return import StudysetReturn
from neurostore_sdk.models.studyset_return_relationships import StudysetReturnRelationships
from neurostore_sdk.models.studyset_return_relationships_studies_inner import StudysetReturnRelationshipsStudiesInner
from neurostore_sdk.models.studysets_id_get404_response import StudysetsIdGet404Response
from neurostore_sdk.models.studysets_id_put422_response import StudysetsIdPut422Response
from neurostore_sdk.models.user import User
from neurostore_sdk.models.user_list import UserList
from neurostore_sdk.models.user_resource_attributes import UserResourceAttributes
from neurostore_sdk.models.userless_resource_attributes import UserlessResourceAttributes
from neurostore_sdk.models.writeable_resource_attributes import WriteableResourceAttributes
