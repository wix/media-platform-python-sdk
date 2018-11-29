from setuptools import setup, find_packages


setup(
    name='media-platform-python-sdk',
    version='1.0.0',
    description='Wix Media Platform python SDK',
    author='Elad Laufer',
    author_email='elad@wix.com',
    url='https://console.wixmp.com/',
    package_dir={'': 'media_platform'},
    packages=find_packages(where='media_platform'),
    install_requires=[
        'python-jose==3.0.1',
        'requests==2.20.1',
    ],
    tests_require=[
        'PyHamcrest==1.9.0',
        'mockito==1.1.1',
        'httpretty==0.9.6'
    ]
)
