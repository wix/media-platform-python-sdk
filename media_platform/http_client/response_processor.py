import requests

from media_platform.exception.bad_gateway_exception import BadGatewayException
from media_platform.exception.conflict_exception import ConflictException
from media_platform.exception.server_error_exception import ServerErrorException
from media_platform.lang.serialization import Deserializable
from media_platform.exception.forbidden_exception import ForbiddenException
from media_platform.exception.media_platform_exception import MediaPlatformException
from media_platform.exception.not_found_exception import NotFoundException
from media_platform.exception.unauthorized_exception import UnauthorizedException
from media_platform.service.rest_result import RestResult


class ResponseProcessor:

    @staticmethod
    def process(response: requests.Response, payload_type: Deserializable = None) -> object or None:
        if 200 <= response.status_code <= 299:
            return ResponseProcessor._handle_success(response, payload_type)
        else:
            ResponseProcessor._handle_error(response)

    @classmethod
    def _handle_success(cls, response: requests.Response,
                        payload_type: Deserializable or [Deserializable]) -> object or None:
        try:
            rest_result = RestResult.deserialize(response.json())
            rest_result.raise_for_code()

            if rest_result.payload is None:
                return None

            if payload_type is None:
                raise MediaPlatformException('Unexpected payload (expected None)')

            payload = payload_type.deserialize(rest_result.payload)
            payload.seen_by = response.headers.get('X-Seen-By')
            return payload

        except (ValueError, KeyError) as e:
            raise MediaPlatformException('Bad response format', e)

    @classmethod
    def _handle_error(cls, response: requests.Response):
        try:
            rest_result = RestResult.deserialize(response.json())
            message = rest_result.message
        except (ValueError, KeyError):
            message = response.content

        if response.status_code == 401:
            raise UnauthorizedException(message)

        elif response.status_code == 403:
            raise ForbiddenException(message)

        elif response.status_code == 404:
            raise NotFoundException(message)

        elif response.status_code == 409:
            raise ConflictException(message)

        elif response.status_code == 500:
            raise ServerErrorException(message)

        elif response.status_code == 502:
            raise BadGatewayException(message)

        else:
            raise MediaPlatformException(message)
