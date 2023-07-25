# coding: utf-8

"""
    Jarvice API

    The JARVICE API allows full control on running jobs as well as managing applications via PushToCompute™.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@nimbix.net
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "jarviceapi-client"
VERSION = "1.0.11"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3",
    "python-dateutil",
    "pydantic >= 1.10.5, < 2",
    "aenum"
]

setup(
    name=NAME,
    version=VERSION,
    description="Jarvice API",
    author="Nimbix",
    author_email="support@nimbix.net",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Jarvice API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Proprietary",
    long_description_content_type='text/markdown',
    long_description="""\
    The JARVICE API allows full control on running jobs as well as managing applications via PushToCompute™.  # noqa: E501
    """
)
