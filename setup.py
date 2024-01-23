from setuptools import setup, find_packages

setup(
    name='tms-tools',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'tms=tms.__main__:main',
        ],
    },
    author="SQW",
    author_email="sqw_stone@qq.com",
    description="A tool class for uploading to modelscope",
    url="http://iswbm.com/", 
)
