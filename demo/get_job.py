import json
from sys import argv

import media_platform

project_id = 'wixmp-405ab6221bcf4063702691d7'

client = media_platform.Client(
    domain=project_id + '.appspot.com',
    app_id='a323f50fabab45308ba52e860d81cb50',
    shared_secret='2c34a6f7f7c07a14e3ce42c7bbc16cb9'
)

job_ids = argv[1:]
for job_id in job_ids:
    print('Getting job %s' % job_id)
    job = client.job_service.job_request(). \
                set_id(job_id). \
                execute()

    print(json.dumps(job.serialize(), indent=4))
    print('')
