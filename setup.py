from setuptools import setup, find_packages

PACKAGE_NAME = 'wix_media_platform'
PACKAGE_VERSION = '1.42.0'

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
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(include=('media_platform', 'media_platform.*',)),
    install_requires=[
        'python-jose[cryptography]',
        'requests',
        'requests-toolbelt',
        'furl',
    ],
    tests_require=[
        'PyHamcrest',
        'mockito',
        'httpretty'
    ]
)
