# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from neurostore_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from neurostore_sdk.model.analysis_base import AnalysisBase
from neurostore_sdk.model.analysis_common import AnalysisCommon
from neurostore_sdk.model.analysis_list import AnalysisList
from neurostore_sdk.model.analysis_request import AnalysisRequest
from neurostore_sdk.model.analysis_request_relationships import AnalysisRequestRelationships
from neurostore_sdk.model.analysis_return import AnalysisReturn
from neurostore_sdk.model.analysis_return_relationships import AnalysisReturnRelationships
from neurostore_sdk.model.annotation_base import AnnotationBase
from neurostore_sdk.model.annotation_common import AnnotationCommon
from neurostore_sdk.model.annotation_export import AnnotationExport
from neurostore_sdk.model.annotation_list import AnnotationList
from neurostore_sdk.model.annotation_request import AnnotationRequest
from neurostore_sdk.model.annotation_request_relationships import AnnotationRequestRelationships
from neurostore_sdk.model.annotation_return import AnnotationReturn
from neurostore_sdk.model.annotation_return_relationships import AnnotationReturnRelationships
from neurostore_sdk.model.clone import Clone
from neurostore_sdk.model.condition_base import ConditionBase
from neurostore_sdk.model.condition_list import ConditionList
from neurostore_sdk.model.condition_request import ConditionRequest
from neurostore_sdk.model.condition_return import ConditionReturn
from neurostore_sdk.model.entity import Entity
from neurostore_sdk.model.image_base import ImageBase
from neurostore_sdk.model.image_common import ImageCommon
from neurostore_sdk.model.image_list import ImageList
from neurostore_sdk.model.image_relationships import ImageRelationships
from neurostore_sdk.model.image_request import ImageRequest
from neurostore_sdk.model.image_return import ImageReturn
from neurostore_sdk.model.json_ld import JsonLd
from neurostore_sdk.model.metadata import Metadata
from neurostore_sdk.model.nested_put_attributes import NestedPutAttributes
from neurostore_sdk.model.note_collection_base import NoteCollectionBase
from neurostore_sdk.model.note_collection_request import NoteCollectionRequest
from neurostore_sdk.model.note_collection_return import NoteCollectionReturn
from neurostore_sdk.model.point_base import PointBase
from neurostore_sdk.model.point_common import PointCommon
from neurostore_sdk.model.point_list import PointList
from neurostore_sdk.model.point_relationships import PointRelationships
from neurostore_sdk.model.point_request import PointRequest
from neurostore_sdk.model.point_return import PointReturn
from neurostore_sdk.model.point_value import PointValue
from neurostore_sdk.model.readable_resource_attributes import ReadableResourceAttributes
from neurostore_sdk.model.resource_attributes import ResourceAttributes
from neurostore_sdk.model.study_base import StudyBase
from neurostore_sdk.model.study_list import StudyList
from neurostore_sdk.model.study_request import StudyRequest
from neurostore_sdk.model.study_request_relationships import StudyRequestRelationships
from neurostore_sdk.model.study_return import StudyReturn
from neurostore_sdk.model.study_return_relationships import StudyReturnRelationships
from neurostore_sdk.model.studyset_base import StudysetBase
from neurostore_sdk.model.studyset_list import StudysetList
from neurostore_sdk.model.studyset_request import StudysetRequest
from neurostore_sdk.model.studyset_request_relationships import StudysetRequestRelationships
from neurostore_sdk.model.studyset_return import StudysetReturn
from neurostore_sdk.model.studyset_return_relationships import StudysetReturnRelationships
from neurostore_sdk.model.user import User
from neurostore_sdk.model.user_list import UserList
from neurostore_sdk.model.user_resource_attributes import UserResourceAttributes
from neurostore_sdk.model.userless_resource_attributes import UserlessResourceAttributes
from neurostore_sdk.model.writeable_resource_attributes import WriteableResourceAttributes
