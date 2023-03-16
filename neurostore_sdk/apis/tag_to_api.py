import typing_extensions

from neurostore_sdk.apis.tags import TagValues
from neurostore_sdk.apis.tags.analyses_api import AnalysesApi
from neurostore_sdk.apis.tags.studysets_api import StudysetsApi
from neurostore_sdk.apis.tags.images_api import ImagesApi
from neurostore_sdk.apis.tags.points_api import PointsApi
from neurostore_sdk.apis.tags.studies_api import StudiesApi
from neurostore_sdk.apis.tags.conditions_api import ConditionsApi
from neurostore_sdk.apis.tags.user_api import UserApi
from neurostore_sdk.apis.tags.annotations_api import AnnotationsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ANALYSES: AnalysesApi,
        TagValues.STUDYSETS: StudysetsApi,
        TagValues.IMAGES: ImagesApi,
        TagValues.POINTS: PointsApi,
        TagValues.STUDIES: StudiesApi,
        TagValues.CONDITIONS: ConditionsApi,
        TagValues.USER: UserApi,
        TagValues.ANNOTATIONS: AnnotationsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ANALYSES: AnalysesApi,
        TagValues.STUDYSETS: StudysetsApi,
        TagValues.IMAGES: ImagesApi,
        TagValues.POINTS: PointsApi,
        TagValues.STUDIES: StudiesApi,
        TagValues.CONDITIONS: ConditionsApi,
        TagValues.USER: UserApi,
        TagValues.ANNOTATIONS: AnnotationsApi,
    }
)
