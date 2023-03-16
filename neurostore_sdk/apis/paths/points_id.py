from neurostore_sdk.paths.points_id.get import ApiForget
from neurostore_sdk.paths.points_id.put import ApiForput
from neurostore_sdk.paths.points_id.delete import ApiFordelete


class PointsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
