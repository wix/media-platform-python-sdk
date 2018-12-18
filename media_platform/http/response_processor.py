import requests
from typing import Type

from media_platform.exception.conflict_exception import ConflictException
from media_platform.lang.serialization import Deserializable
from media_platform.exception.forbidden_exception import ForbiddenException
from media_platform.exception.media_platform_exception import MediaPlatformException
from media_platform.exception.not_found_exception import NotFoundException
from media_platform.exception.unauthorized_exception import UnauthorizedException
from media_platform.service.rest_result import RestResult


class ResponseProcessor(object):

    @staticmethod
    def process(response, payload_type=None):
        # type: (requests.Response, Type[Deserializable]) -> object or None

        ResponseProcessor._raise_for_status(response)
        return ResponseProcessor._handle_response(response, payload_type)

    @staticmethod
    def _handle_response(response, payload_type=None):
        # type: (requests.Response, Type[Deserializable] or [Type[Deserializable]]) -> object or None

        try:
            rest_result = RestResult.deserialize(response.json())
        except ValueError as e:
            raise MediaPlatformException(e)

        rest_result.raise_for_code()

        if rest_result.payload is None:
            return None

        if payload_type is None:
            raise MediaPlatformException(Exception('must supply payload type?'))

        return payload_type.deserialize(rest_result.payload)

    @staticmethod
    def _raise_for_status(response):
        # type: (requests.Response) -> None

        status_code = response.status_code

        if status_code == 401:
            raise UnauthorizedException()

        if status_code == 403:
            raise ForbiddenException()

        if status_code == 404:
            raise NotFoundException()

        if status_code == 409:
            raise ConflictException()

        if status_code < 200 or status_code > 299:
            raise MediaPlatformException()
