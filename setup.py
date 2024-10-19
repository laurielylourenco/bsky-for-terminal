from setuptools import setup, find_packages

setup(
    name='bsky-for-terminal',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'atproto',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'bsky=bskyterminal.script:main',
        ],
    },
)
