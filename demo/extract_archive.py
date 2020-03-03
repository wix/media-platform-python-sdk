from globals import demo_path, resources_dir, client, project_id
from media_platform import Source, Destination, FileDescriptor
from media_platform.job.extract_archive.extract_archive_job import ExtractArchiveJob
from media_platform.job.extract_archive.extraction_report import ExtractionReport
from media_platform.job.result.extract_archive_result import ExtractArchiveResult
from wait_for_results import wait_for_result

archive_path = demo_path + '/archive1.zip'
extracted_path = demo_path + '/extracted'
report_path = extracted_path + '/report.csv'


def extract_archive_demo():
    archive_file = upload_archive()

    extraction_job = extract_archive(archive_file)

    result = wait_for_result(extraction_job)  # type: ExtractArchiveResult

    print_report(result.report_file_descriptor)



def upload_archive():
    # type: () -> FileDescriptor
    print('Uploading archive to %s...' % archive_path)

    with open(resources_dir + '/archive.zip', 'rb') as archive:
        return client.file_service.upload_file_v2_request(). \
            set_path(archive_path). \
            set_content(archive). \
            execute()


def extract_archive(archive_file):
    # type: (FileDescriptor) -> ExtractArchiveJob
    print('Extracting archive to %s...' % extracted_path)

    return client.archive_service.extract_archive_request(). \
        set_source(Source(archive_file.path)). \
        set_destination(Destination(directory=extracted_path)). \
        set_report(ExtractionReport(Destination(report_path))). \
        execute()


def print_report(report_file):
    # type: (FileDescriptor) -> None
    print('Successfully extracted. Archive contents:')

    report = client.file_service.download_file_v2_request(). \
        set_path(report_file.path). \
        execute()

    with report:
        for path in list(report.iter_lines())[1:]:
            print('https://%s.wixmp.com%s' % (project_id, path))
    print('')

if __name__ == '__main__':
    extract_archive_demo()
