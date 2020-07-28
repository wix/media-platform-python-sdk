from unittest import TestCase

from media_platform.service.flow_control_service.flow_state import FlowState


class TestFlowState(TestCase):
    maxDiff = None

    def test_serialization(self):
        state_data = {
            'invocation': {
                'sources': [],
                'entryPoints': ['import'],
                'callback': None,
                'errorStrategy': 'stopOnError',
                'operationCallbackStatusFilter': []
            },
            'operations': {
                'import': {
                    'callback': None,
                    'status': 'success',
                    'deleteSources': None,
                    'jobs': [
                        'g_1'
                    ],
                    'specification': {
                        'destination': {
                            'directory': None,
                            'path': '/imports/video.mp4',
                            'acl': 'public',
                            'lifecycle': None,
                            'bucket': None
                        },
                        'externalAuthorization': None,
                        'sourceUrl': 'https://fish.com/dag.gadol'
                    },
                    'results': [
                        {
                            'mimeType': 'video/mp4',
                            'hash': None,
                            'id': '1354324',
                            'path': '/imports/video.mp4',
                            'acl': 'public',
                            'type': '-',
                            'size': 4151438,
                            'lifecycle': None,
                            'dateUpdated': '2018-01-11T13:15:57Z',
                            'dateCreated': '2018-01-11T13:15:57Z',
                        }
                    ],
                    'extraResults': {},
                    'sources': [],
                    'successors': [],
                    'type': 'file.import'
                },
            },
            'id': '49eca277747047c5833f15a0eed137b9',
            'status': 'success',
            'error': None
        }

        flow_state = FlowState.deserialize(state_data)

        self.assertEquals(flow_state.serialize(), state_data)
