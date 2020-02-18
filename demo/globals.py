import os
import uuid

import media_platform

demo_path = '/python-demo/' + str(uuid.uuid4())
resources_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + '/resources')

project_id = 'wixmp-410a67650b2f46baa5d003c6'

client = media_platform.Client(
    domain=project_id + '.appspot.com',
    app_id='48fa9aa3e9d342a3a33e66af08cd7fe3',
    shared_secret='fad475d88786ab720b04f059ac674b0e'
)
