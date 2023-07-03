from setuptools import setup, find_packages

setup(
    name='gptd-client',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gptd-client=gptd_client.client:main',
        ],
    },
)

