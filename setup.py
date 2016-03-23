from setuptools import setup

setup(
    name='icalc',
    version='0.1',
    py_modules=['icalc'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        icalc=main:cli
    ''',
)
