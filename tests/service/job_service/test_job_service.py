import json
import unittest

import httpretty
from hamcrest import assert_that, instance_of, is_
from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.import_file_job import ImportFileJob
from media_platform.job.job import Job, JobStatus
from media_platform.service.job_service.job_service import JobService
from media_platform.service.list_request import OrderBy, OrderDirection
from media_platform.service.rest_result import RestResult


class TestJobService(unittest.TestCase):
    authenticator = AppAuthenticator('app', 'secret')
    authenticated_http_client = AuthenticatedHTTPClient(authenticator)

    job_service = JobService('fish.barrel', authenticated_http_client)

    @httpretty.activate
    def test_job_request(self):
        payload = {
            'status': 'pending',
            'specification': {
                'sourceUrl': 'http://source.url/filename.txt',
                'destination': {
                    'directory': '/fish',
                    'acl': 'public'
                }
            },
            'dateCreated': '2017-05-23T08:34:43Z',
            'sources': [],
            'result': None,
            'id': 'g_1',
            'dateUpdated': '2017-05-23T08:34:43Z',
            'type': 'urn:job:import.file',
            'groupId': '71f0d3fde7f348ea89aa1173299146f8',
            'issuer': 'urn:app:app-id-1'
        }
        response_1 = RestResult(0, 'OK', payload)
        httpretty.register_uri(
            httpretty.GET,
            'https://fish.barrel/_api/jobs/g_1',
            body=json.dumps(response_1.serialize())
        )
        payload = {
            'status': 'pending',
            'specification': {
                'sourceUrl': 'http://source.url/filename.txt',
                'destination': {
                    'directory': '/fish',
                    'acl': 'public'
                }
            },
            'dateCreated': '2017-05-23T08:34:43Z',
            'sources': [],
            'result': None,
            'id': 'g_2',
            'dateUpdated': '2017-05-23T08:34:43Z',
            'type': 'urn:job:import.file',
            'groupId': '71f0d3fde7f348ea89aa1173299146f8',
            'issuer': 'urn:app:app-id-1'
        }
        response_2 = RestResult(0, 'OK', payload)
        httpretty.register_uri(
            httpretty.GET,
            'https://fish.barrel/_api/jobs/g_2',
            body=json.dumps(response_2.serialize())
        )

        request = self.job_service.job_request().set_id('g_1')
        job_1 = request.execute()
        # verify that url rewrite works as intended
        job_2 = request.set_id('g_2').execute()

        assert_that(job_1, instance_of(ImportFileJob))
        assert_that(job_1.id, is_('g_1'))
        assert_that(job_2.id, is_('g_2'))

    @httpretty.activate
    def test_job_request_base_job(self):
        payload = {
            'status': 'pending',
            'specification': {},
            'dateCreated': '2017-05-23T08:34:43Z',
            'sources': [],
            'result': None,
            'id': 'g_1',
            'dateUpdated': '2017-05-23T08:34:43Z',
            'type': 'urn:job:something.fresh',
            'groupId': '71f0d3fde7f348ea89aa1173299146f8',
            'issuer': 'urn:app:app-id-1'
        }
        response_1 = RestResult(0, 'OK', payload)
        httpretty.register_uri(
            httpretty.GET,
            'https://fish.barrel/_api/jobs/1_g',
            body=json.dumps(response_1.serialize())
        )

        job = self.job_service.job_request().set_id('1_g').execute()

        assert_that(job, instance_of(Job))

    @httpretty.activate
    def test_job_group_request(self):
        payload = [{
            'status': 'pending',
            'specification': {},
            'dateCreated': '2017-05-23T08:34:43Z',
            'sources': [],
            'result': None,
            'id': 'g_1',
            'dateUpdated': '2017-05-23T08:34:43Z',
            'type': 'urn:job:something.fresh',
            'groupId': '71f0d3fde7f348ea89aa1173299146f8',
            'issuer': 'urn:app:app-id-1'
        }]
        response = RestResult(0, 'OK', payload)
        httpretty.register_uri(
            httpretty.GET,
            'https://fish.barrel/_api/jobs/groups/g',
            body=json.dumps(response.serialize())
        )

        jobs = self.job_service.job_group_request().set_group_id('g').execute()

        assert_that(jobs[0], instance_of(Job))
        assert_that(jobs[0].id, is_('g_1'))

    @httpretty.activate
    def test_job_list_request(self):
        payload = {
            'nextPageToken': 'next',
            'jobs': [{
                'status': 'pending',
                'specification': {},
                'dateCreated': '2017-05-23T08:34:43Z',
                'sources': [],
                'result': None,
                'id': 'g_1',
                'dateUpdated': '2017-05-23T08:34:43Z',
                'type': 'urn:job:something.fresh',
                'groupId': '71f0d3fde7f348ea89aa1173299146f8',
                'issuer': 'urn:app:app-id-1'
            }]}
        response = RestResult(0, 'OK', payload)
        httpretty.register_uri(
            httpretty.GET,
            'https://fish.barrel/_api/jobs',
            body=json.dumps(response.serialize())
        )

        job_list = self.job_service.job_list_request().set_type('urn:job:fish').set_page_size(3).set_order_by(
            OrderBy.date_updated
        ).set_next_page_token('nnn').set_path('/mmm').set_issuer('urn:me').set_order_direction(
            OrderDirection.descending
        ).set_status(JobStatus.pending).execute()

        assert_that(job_list.jobs[0], instance_of(Job))
        assert_that(job_list.jobs[0].id, is_('g_1'))
        assert_that(httpretty.last_request().querystring, is_({
            'nextPageToken': ['nnn'],
            'orderBy': ['dateUpdated'],
            'pageSize': ['3'],
            'status': ['pending'],
            'path': ['/mmm'],
            'type': ['urn:job:fish'],
            'orderDirection': ['des'],
            'issuer': ['urn:me']
        }))
