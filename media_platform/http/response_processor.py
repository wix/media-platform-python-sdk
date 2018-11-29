from requests import Response

from media_platform.exception.forbidden_exception import ForbiddenException
from media_platform.exception.media_platform_exception import MediaPlatformException
from media_platform.exception.not_found_exception import NotFoundException
from media_platform.exception.unauthorized_exception import UnauthorizedException
from media_platform.lang.serializable import Serializable
from media_platform.service.rest_result import RestResult


class ResponseProcessor(object):

    @staticmethod
    def process(response, payload_type=None):
        # type: (Response, Serializable) -> Serializable or None

        # sort of a process chain todo: make proper chain
        return ResponseProcessor._handle_response(
            ResponseProcessor._raise_for_status(response),
            payload_type)

    @staticmethod
    def _handle_response(response, payload_type=None):
        # type: (Response, Serializable) -> Serializable or None

        try:
            rest_result = RestResult.deserialize(response.json())
        except ValueError as e:
            raise MediaPlatformException(e)

        if rest_result.code != 0:
            # todo: code -> exception mapper (Alon, have fun :))
            raise MediaPlatformException()

        if payload_type and rest_result.payload is not None:
            return payload_type.deserialize(rest_result.payload)
        else:
            return None

    @staticmethod
    def _raise_for_status(response):
        # type: (Response) -> Response

        status_code = response.status_code

        if status_code == 401:
            raise UnauthorizedException()

        if status_code == 403:
            raise ForbiddenException()

        if status_code == 404:
            raise NotFoundException()

        if status_code < 200 or status_code > 299:
            raise MediaPlatformException()

        return response
