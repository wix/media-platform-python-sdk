from demo.globals import demo_path, resources_dir, client, project_id
from media_platform import FileDescriptor

image_path = demo_path + '/image.png'


def image_manipulation_demo():
    image_file = upload_image()
    print_manipulated_image_url(image_file)


def upload_image():
    # type: () -> FileDescriptor
    print('Uploading image to %s...' % image_path)
    with open(resources_dir + '/image.png', 'rb') as image:
        return client.file_service.upload_file_v2_request(). \
            set_path(image_path). \
            set_content(image). \
            execute()


def print_manipulated_image_url(image_file):
    # type: (FileDescriptor) -> None
    print('Manipulated image url: https://images-%s.wixmp.com%s::fit:200_100' % (project_id, image_file.path))
    print('')

if __name__ == '__main__':
    image_manipulation_demo()