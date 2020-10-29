from __future__ import annotations

from media_platform.job.job_type import JobType
from media_platform.job.specification import Specification
from media_platform.service.destination import Destination
from media_platform.job.job import Job
from media_platform.service.file_service.external_authorization import ExternalAuthorization


class ImportFileSpecification(Specification):
    def __init__(self, source_url: str, destination: Destination, external_authorization: ExternalAuthorization = None):
        self.source_url = source_url
        self.destination = destination
        self.external_authorization = external_authorization

    def serialize(self) -> dict:
        return {
            'sourceUrl': self.source_url,
            'destination': self.destination.serialize(),
            'externalAuthorization': self.external_authorization.serialize() if self.external_authorization else None
        }

    @classmethod
    def deserialize(cls, data: dict) -> ImportFileSpecification:
        destination = Destination.deserialize(data['destination'])

        external_authorization_data = data.get('externalAuthorization')
        external_authorization = None
        if external_authorization_data:
            external_authorization = ExternalAuthorization.deserialize(external_authorization_data)

        return ImportFileSpecification(data['sourceUrl'], destination, external_authorization)


class ImportFileJob(Job):
    type = JobType.import_file
    specification_type = ImportFileSpecification
