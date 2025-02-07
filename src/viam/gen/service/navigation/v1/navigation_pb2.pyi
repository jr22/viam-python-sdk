"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
from .... import common
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.struct_pb2
import sys
import typing
if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _MapType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _MapTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_MapType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    MAP_TYPE_UNSPECIFIED: _MapType.ValueType
    MAP_TYPE_NONE: _MapType.ValueType
    MAP_TYPE_GPS: _MapType.ValueType

class MapType(_MapType, metaclass=_MapTypeEnumTypeWrapper):
    """MapType represents the various types of map the navigation service can ingest."""
MAP_TYPE_UNSPECIFIED: MapType.ValueType
MAP_TYPE_NONE: MapType.ValueType
MAP_TYPE_GPS: MapType.ValueType
global___MapType = MapType

class _Mode:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Mode.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    MODE_UNSPECIFIED: _Mode.ValueType
    MODE_MANUAL: _Mode.ValueType
    MODE_WAYPOINT: _Mode.ValueType
    MODE_EXPLORE: _Mode.ValueType

class Mode(_Mode, metaclass=_ModeEnumTypeWrapper):
    ...
MODE_UNSPECIFIED: Mode.ValueType
MODE_MANUAL: Mode.ValueType
MODE_WAYPOINT: Mode.ValueType
MODE_EXPLORE: Mode.ValueType
global___Mode = Mode

@typing_extensions.final
class GetModeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name']) -> None:
        ...
global___GetModeRequest = GetModeRequest

@typing_extensions.final
class GetModeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MODE_FIELD_NUMBER: builtins.int
    mode: global___Mode.ValueType

    def __init__(self, *, mode: global___Mode.ValueType=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['mode', b'mode']) -> None:
        ...
global___GetModeResponse = GetModeResponse

@typing_extensions.final
class SetModeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    MODE_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    mode: global___Mode.ValueType

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., mode: global___Mode.ValueType=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'mode', b'mode', 'name', b'name']) -> None:
        ...
global___SetModeRequest = SetModeRequest

@typing_extensions.final
class SetModeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___SetModeResponse = SetModeResponse

@typing_extensions.final
class Waypoint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    LOCATION_FIELD_NUMBER: builtins.int
    id: builtins.str

    @property
    def location(self) -> common.v1.common_pb2.GeoPoint:
        ...

    def __init__(self, *, id: builtins.str=..., location: common.v1.common_pb2.GeoPoint | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['location', b'location']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['id', b'id', 'location', b'location']) -> None:
        ...
global___Waypoint = Waypoint

@typing_extensions.final
class GetLocationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name']) -> None:
        ...
global___GetLocationRequest = GetLocationRequest

@typing_extensions.final
class GetLocationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LOCATION_FIELD_NUMBER: builtins.int
    COMPASS_HEADING_FIELD_NUMBER: builtins.int

    @property
    def location(self) -> common.v1.common_pb2.GeoPoint:
        ...
    compass_heading: builtins.float
    'A number from [0-360) where 0 is north\n    90 is east, 180 is south, 270 is west\n    '

    def __init__(self, *, location: common.v1.common_pb2.GeoPoint | None=..., compass_heading: builtins.float=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['location', b'location']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['compass_heading', b'compass_heading', 'location', b'location']) -> None:
        ...
global___GetLocationResponse = GetLocationResponse

@typing_extensions.final
class GetWaypointsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name']) -> None:
        ...
global___GetWaypointsRequest = GetWaypointsRequest

@typing_extensions.final
class GetWaypointsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    WAYPOINTS_FIELD_NUMBER: builtins.int

    @property
    def waypoints(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Waypoint]:
        ...

    def __init__(self, *, waypoints: collections.abc.Iterable[global___Waypoint] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['waypoints', b'waypoints']) -> None:
        ...
global___GetWaypointsResponse = GetWaypointsResponse

@typing_extensions.final
class AddWaypointRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    LOCATION_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str

    @property
    def location(self) -> common.v1.common_pb2.GeoPoint:
        ...

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., location: common.v1.common_pb2.GeoPoint | None=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra', 'location', b'location']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'location', b'location', 'name', b'name']) -> None:
        ...
global___AddWaypointRequest = AddWaypointRequest

@typing_extensions.final
class AddWaypointResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___AddWaypointResponse = AddWaypointResponse

@typing_extensions.final
class RemoveWaypointRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    id: builtins.str

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., id: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'id', b'id', 'name', b'name']) -> None:
        ...
global___RemoveWaypointRequest = RemoveWaypointRequest

@typing_extensions.final
class RemoveWaypointResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___RemoveWaypointResponse = RemoveWaypointResponse

@typing_extensions.final
class GetObstaclesRequest(google.protobuf.message.Message):
    """GetObstacles will return the geopoint location and geometry of all
    known obstacles on the navigation map. Obstacles that are detected
    through the vision service will only be returned if this endpoint is called
    when the robot is sensing the obstacle
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name']) -> None:
        ...
global___GetObstaclesRequest = GetObstaclesRequest

@typing_extensions.final
class GetObstaclesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    OBSTACLES_FIELD_NUMBER: builtins.int

    @property
    def obstacles(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[common.v1.common_pb2.GeoObstacle]:
        """List of all known geometries"""

    def __init__(self, *, obstacles: collections.abc.Iterable[common.v1.common_pb2.GeoObstacle] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['obstacles', b'obstacles']) -> None:
        ...
global___GetObstaclesResponse = GetObstaclesResponse

@typing_extensions.final
class Path(google.protobuf.message.Message):
    """A user provided destination and the set of geopoints that
    the robot is expected to take to get there
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DESTINATION_WAYPOINT_ID_FIELD_NUMBER: builtins.int
    GEOPOINTS_FIELD_NUMBER: builtins.int
    destination_waypoint_id: builtins.str
    'The id of the user specified waypoint'

    @property
    def geopoints(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[common.v1.common_pb2.GeoPoint]:
        """List of geopoints that the motion planner output to reach the destination
        The first geopoint is the starting position of the robot for that path
        """

    def __init__(self, *, destination_waypoint_id: builtins.str=..., geopoints: collections.abc.Iterable[common.v1.common_pb2.GeoPoint] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['destination_waypoint_id', b'destination_waypoint_id', 'geopoints', b'geopoints']) -> None:
        ...
global___Path = Path

@typing_extensions.final
class GetPathsRequest(google.protobuf.message.Message):
    """Returns all the paths known to the navigation service"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of the navigation service'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        ...

    def __init__(self, *, name: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name']) -> None:
        ...
global___GetPathsRequest = GetPathsRequest

@typing_extensions.final
class GetPathsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PATHS_FIELD_NUMBER: builtins.int

    @property
    def paths(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Path]:
        ...

    def __init__(self, *, paths: collections.abc.Iterable[global___Path] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['paths', b'paths']) -> None:
        ...
global___GetPathsResponse = GetPathsResponse

@typing_extensions.final
class GetPropertiesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of the navigation service'

    def __init__(self, *, name: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name']) -> None:
        ...
global___GetPropertiesRequest = GetPropertiesRequest

@typing_extensions.final
class GetPropertiesResponse(google.protobuf.message.Message):
    """Returns properties information for the named navigation service"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MAP_TYPE_FIELD_NUMBER: builtins.int
    map_type: global___MapType.ValueType

    def __init__(self, *, map_type: global___MapType.ValueType=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['map_type', b'map_type']) -> None:
        ...
global___GetPropertiesResponse = GetPropertiesResponse