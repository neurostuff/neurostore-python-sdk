# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from neurostore_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    STUDYSETS_ = "/studysets/"
    STUDYSETS_ID = "/studysets/{id}"
    STUDIES_ = "/studies/"
    STUDIES_ID = "/studies/{id}"
    ANALYSES_ = "/analyses/"
    ANALYSES_ID = "/analyses/{id}"
    POINTS_ = "/points/"
    POINTS_ID = "/points/{id}"
    IMAGES_ = "/images/"
    IMAGES_ID = "/images/{id}"
    CONDITIONS_ = "/conditions/"
    CONDITIONS_ID = "/conditions/{id}"
    ANNOTATIONS_ = "/annotations/"
    ANNOTATIONS_ID = "/annotations/{id}"
    USERS_ = "/users/"
    USERS_ID = "/users/{id}"
