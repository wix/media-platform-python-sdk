from setuptools import setup, find_packages

PACKAGE_NAME = 'wix_media_platform'
PACKAGE_VERSION = '1.11.0'

setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description='Wix Media Platform python SDK',
    author='Wix Media Platform',
    author_email='mcloud@wix.com',
    url='https://github.com/wix/media-platform-python-sdk',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages(include=('media_platform', 'media_platform.*',)),
    install_requires=[
        'python-jose==3.0.1',
        'requests==2.20.1',
        'requests-toolbelt==0.8.0',
        'typing==3.6.6'
    ],
    tests_require=[
        'PyHamcrest==1.9.0',
        'mockito==1.1.1',
        'httpretty==0.9.6'
    ]
)
