from globals import demo_path, resources_dir, client, project_id
from media_platform import FileDescriptor

image_path = demo_path + '/image.png'


def image_manipulation_demo():
    upload_image()
    print_manipulated_image_url()


def upload_image():
    # type: () -> FileDescriptor
    print('Uploading image to %s...' % image_path)
    with open(resources_dir + '/image.png', 'rb') as archive:
        return client.file_service.upload_file_v2_request(). \
            set_path(image_path). \
            set_content(archive). \
            execute()


def print_manipulated_image_url():
    print('Manipulated image url: https://img-%s.wixmp.com%s::fit:200_100' % (project_id, image_path))
    print('')
