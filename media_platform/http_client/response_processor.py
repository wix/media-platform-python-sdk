import requests
from typing import Type

from media_platform.exception.bad_gateway_exception import BadGatewayException
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

        if 200 <= response.status_code <= 299:
            return ResponseProcessor._handle_success(response, payload_type)
        else:
            ResponseProcessor._handle_error(response)

    @classmethod
    def _handle_success(cls, response, payload_type):
        # type: (requests.Response, Type[Deserializable] or [Type[Deserializable]]) -> object or None
        try:
            rest_result = RestResult.deserialize(response.json())
            rest_result.raise_for_code()

            if rest_result.payload is None:
                return None

            if payload_type is None:
                raise MediaPlatformException('Unexpected payload (expected None)')

            return payload_type.deserialize(rest_result.payload)

        except (ValueError, KeyError) as e:
            raise MediaPlatformException('Bad response format', e)

    @classmethod
    def _handle_error(cls, response):
        try:
            rest_result = RestResult.deserialize(response.json())
            message = rest_result.message
        except (ValueError, KeyError):
            message = response.content

        status_code = response.status_code

        if status_code == 401:
            raise UnauthorizedException(message)

        if status_code == 403:
            raise ForbiddenException(message)

        if status_code == 404:
            raise NotFoundException(message)

        if status_code == 409:
            raise ConflictException(message)

        if status_code == 502:
            raise BadGatewayException(message)

        raise MediaPlatformException(message)
