import typing_extensions

from neurostore_sdk.paths import PathValues
from neurostore_sdk.apis.paths.studysets_ import Studysets
from neurostore_sdk.apis.paths.studysets_id import StudysetsId
from neurostore_sdk.apis.paths.studies_ import Studies
from neurostore_sdk.apis.paths.studies_id import StudiesId
from neurostore_sdk.apis.paths.analyses_ import Analyses
from neurostore_sdk.apis.paths.analyses_id import AnalysesId
from neurostore_sdk.apis.paths.points_ import Points
from neurostore_sdk.apis.paths.points_id import PointsId
from neurostore_sdk.apis.paths.images_ import Images
from neurostore_sdk.apis.paths.images_id import ImagesId
from neurostore_sdk.apis.paths.conditions_ import Conditions
from neurostore_sdk.apis.paths.conditions_id import ConditionsId
from neurostore_sdk.apis.paths.annotations_ import Annotations
from neurostore_sdk.apis.paths.annotations_id import AnnotationsId
from neurostore_sdk.apis.paths.users_ import Users
from neurostore_sdk.apis.paths.users_id import UsersId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.STUDYSETS_: Studysets,
        PathValues.STUDYSETS_ID: StudysetsId,
        PathValues.STUDIES_: Studies,
        PathValues.STUDIES_ID: StudiesId,
        PathValues.ANALYSES_: Analyses,
        PathValues.ANALYSES_ID: AnalysesId,
        PathValues.POINTS_: Points,
        PathValues.POINTS_ID: PointsId,
        PathValues.IMAGES_: Images,
        PathValues.IMAGES_ID: ImagesId,
        PathValues.CONDITIONS_: Conditions,
        PathValues.CONDITIONS_ID: ConditionsId,
        PathValues.ANNOTATIONS_: Annotations,
        PathValues.ANNOTATIONS_ID: AnnotationsId,
        PathValues.USERS_: Users,
        PathValues.USERS_ID: UsersId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.STUDYSETS_: Studysets,
        PathValues.STUDYSETS_ID: StudysetsId,
        PathValues.STUDIES_: Studies,
        PathValues.STUDIES_ID: StudiesId,
        PathValues.ANALYSES_: Analyses,
        PathValues.ANALYSES_ID: AnalysesId,
        PathValues.POINTS_: Points,
        PathValues.POINTS_ID: PointsId,
        PathValues.IMAGES_: Images,
        PathValues.IMAGES_ID: ImagesId,
        PathValues.CONDITIONS_: Conditions,
        PathValues.CONDITIONS_ID: ConditionsId,
        PathValues.ANNOTATIONS_: Annotations,
        PathValues.ANNOTATIONS_ID: AnnotationsId,
        PathValues.USERS_: Users,
        PathValues.USERS_ID: UsersId,
    }
)
