from globals import demo_path, resources_dir, client
from media_platform import Source, Destination, FileDescriptor
from media_platform.job.extract_archive.extract_archive_job import ExtractArchiveJob
from media_platform.job.extract_archive.extraction_report import ExtractionReport
from wait_for_result import wait_for_result

archive_path = demo_path + '/archive1.zip'
extracted_path = demo_path + '/extracted'
report_path = extracted_path + '/report.csv'


def extract_archive_demo():
    archive_file = upload_archive()

    extraction_job = extract(archive_file)

    wait_for_result(extraction_job)

    print_report()


def upload_archive():
    # type: () -> FileDescriptor
    print('Uploading archive to %s...' % archive_path)
    with open(resources_dir + '/archive.zip', 'rb') as archive:
        return client.file_service.upload_file_v2_request(). \
            set_path(archive_path). \
            set_content(archive). \
            execute()


def extract(archive_file):
    # type: (FileDescriptor) -> ExtractArchiveJob
    print('Extracting archive to %s...' % extracted_path)

    return client.archive_service.extract_archive_request(). \
        set_source(Source(archive_file.path)). \
        set_destination(Destination(directory=extracted_path)). \
        set_report(ExtractionReport(Destination(report_path))). \
        execute()


def print_report():
    print('Successfully extracted. Archive contents:')

    report = client.file_service.download_file_v2_request(). \
        set_path(report_path). \
        execute()

    with report:
        print(report.content)
    print('')
