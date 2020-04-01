import logging

from typing import Optional

from media_platform.lang.serialization import Deserializable, Serializable

from media_platform.service.live_service.stream_error_info import StreamErrorInfo


class StreamParamsOutOfRangeErrorInfo(StreamErrorInfo):
    def __init__(self, enforced_stream_params, actual_params):
        # type: (EnforcedStreamParams, Params) -> None
        self.enforced_stream_params = enforced_stream_params
        self.actual_params = actual_params

    def serialize(self):
        # type: () -> dict
        return {
            'enforcedStreamParams': self.enforced_stream_params.serialize,
            'actualParams': self.actual_params.serialize
        }

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> StreamParamsOutOfRangeErrorInfo
        return cls(EnforcedStreamParams.deserialize(data['enforcedStreamParams']),
                   Params.deserialize(data['actualParams']))


class StreamParamsOutOfRange(Exception):
    def __init__(self, message, error_info):
        # type: (str, StreamParamsOutOfRangeErrorInfo) -> None
        super(StreamParamsOutOfRange, self).__init__(message)
        self.error_info = error_info


class Params(Serializable, Deserializable):
    def __init__(self, width=None, height=None, bitrate=None):
        self.width = width
        self.height = height
        self.bitrate = bitrate

    def serialize(self):
        # type: () -> dict
        data = {}
        if self.width:
            data['width'] = self.width

        if self.height:
            data['height'] = self.height

        if self.bitrate:
            data['bitrate'] = self.bitrate

        return data

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> Params
        return cls(data.get('width'), data.get('height'), data.get('bitrate'))

    def __lt__(self, other):
        # type: (Params) -> bool
        if not isinstance(other, Params):
            return NotImplemented

        if self.width and other.width and self.width < other.width:
            return True

        if self.height and other.height and self.height < other.height:
            return True

        if self.bitrate and other.bitrate and self.bitrate < other.bitrate:
            return True

        return False

    def __eq__(self, other):
        # type: (Params) -> bool
        if not isinstance(other, Params):
            return NotImplemented

        return self.width == other.width and self.height == other.height and self.bitrate == other.bitrate

    def __repr__(self):
        return str(self.serialize())


# noinspection PyAbstractClass
class Enforceable(Serializable):
    name = None

    def is_valid(self, params):
        # type: (Params) -> bool
        raise NotImplementedError()

    def __repr__(self):
        return str(self.serialize())


class ParamsRange(Enforceable):
    name = 'range'

    def __init__(self, min_values=None, max_values=None):
        # type: (Optional[Params], Optional[Params]) -> None
        self.min_values = min_values
        self.max_values = max_values

    def is_valid(self, params):
        # type: (Params) -> bool
        if self.min_values and params < self.min_values:
            return False

        if self.max_values and params > self.max_values:
            return False

        return True

    def serialize(self):
        # type: () -> dict
        data = {}
        if self.min_values:
            data['minValues'] = self.min_values.serialize()

        if self.max_values:
            data['maxValues'] = self.max_values.serialize()

        return data

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> ParamsRange

        min_values_data = data.get('minValues')
        max_values_data = data.get('maxValues')
        min_values = Params.deserialize(min_values_data) if min_values_data else None
        max_values = Params.deserialize(max_values_data) if max_values_data else None

        return cls(min_values, max_values)


class ParamsOptions(Enforceable):
    name = 'options'

    def __init__(self, options):
        # type: (list[Params]) -> None
        self.options = options

    def is_valid(self, params):
        # type: (Params) -> bool
        return params in self.options

    def serialize(self):
        # type: () -> list[dict]
        return [o.serialize() for o in self.options]

    @classmethod
    def deserialize(cls, data):
        # type: (list[dict]) -> ParamsOptions
        return cls([Params.deserialize(d) for d in data])


class EnforcedStreamParams(Serializable):
    def __init__(self, params_range=None, params_options=None):
        # type: (ParamsRange, ParamsOptions) -> None
        if params_range and params_options:
            raise ValueError('Either range or options must be specified, not both')

        self.params_range = params_range
        self.params_options = params_options

    def enforce(self, params):
        # type: (Params) -> None
        transposed_params = Params(params.height, params.width, params.bitrate)

        for enforceable in [self.params_range, self.params_options]:
            if enforceable:
                if not enforceable.is_valid(params) and not enforceable.is_valid(transposed_params):
                    error_info = StreamParamsOutOfRangeErrorInfo(self, params)
                    raise StreamParamsOutOfRange('%s not in %s %s' % (params, enforceable.name, enforceable),
                                                 error_info)

                logging.debug('%s satisfies enforcement %s: %s' % (params, enforceable.name, enforceable))

    def serialize(self):
        # type: () -> dict
        data = {}
        if self.params_range:
            data['paramsRange'] = self.params_range.serialize()

        if self.params_options:
            data['paramsOptions'] = self.params_options.serialize()

        return data

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> EnforcedStreamParams
        data = data or {}
        params_range_data = data.get('paramsRange')
        params_options_data = data.get('paramsOptions')
        params_range = ParamsRange.deserialize(params_range_data) if params_range_data else None
        params_options = ParamsOptions.deserialize(params_options_data) if params_options_data else None

        return cls(params_range, params_options)

    def __repr__(self):
        return str(self.serialize())
