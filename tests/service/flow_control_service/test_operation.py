from datetime import datetime
from unittest import TestCase

from media_platform import Destination, Source, FileDescriptor
from media_platform.service.file_descriptor import FileType
from media_platform.service.flow_control_service.component import ComponentType
from media_platform.service.flow_control_service.operation import Operation, OperationStatus
from media_platform.service.flow_control_service.specifications.copy_file_specification import CopyFileSpecification

date = datetime(2011, 11, 11, 11, 11, 11)
operation = Operation(ComponentType.copy_file,
                      ['successor'],
                      CopyFileSpecification(Destination('/destination.txt')),
                      OperationStatus.working,
                      True,
                      [Source('/source.txt')],
                      [FileDescriptor('/destination.txt', 'file-id', FileType.file, 'text/plain', 123,
                                      date_created=date, date_updated=date)],
                      ['job-id'],
                      {'extra-result': 'value'},
                      'error_message',
                      1,
                      'state_id',
                      'component_key')

operation_data = {
    'callback': None,
    'componentKey': 'component_key',
    'deleteSources': True,
    'errorCode': 1,
    'errorMessage': 'error_message',
    'extraResults': {'extra-result': 'value'},
    'jobs': ['job-id'],
    'results': [{'acl': 'public',
                 'dateCreated': '2011-11-11T11:11:11Z',
                 'dateUpdated': '2011-11-11T11:11:11Z',
                 'hash': None,
                 'id': 'file-id',
                 'lifecycle': None,
                 'mimeType': 'text/plain',
                 'path': '/destination.txt',
                 'size': 123,
                 'type': '-'}],
    'sources': [{'fileId': None, 'path': '/source.txt'}],
    'specification': {
        'destination': {
            'acl': 'public',
            'bucket': None,
            'directory': None,
            'lifecycle': None,
            'path': '/destination.txt'
        }
    },
    'stateId': 'state_id',
    'status': 'working',
    'successors': ['successor'],
    'type': 'file.copy'
}


class TestOperation(TestCase):
    def test_serialize(self):
        self.assertEqual(operation_data, operation.serialize())

    def test_deserialize(self):
        deserialized = Operation.deserialize(operation_data)
        self.assertEqual(operation.serialize(), deserialized.serialize())
