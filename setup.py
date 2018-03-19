from setuptools import setup
from setuptools import find_packages


setup(
    name='alphai_calendars',
    version='0.0.3',
    description='Alpha-I Crocubot',
    author='Daniele Murroni',
    author_email='daniele.murroni@alpha-i.co',
    packages=find_packages(exclude=['doc', 'tests*']),
    install_requires=[
        'pandas-market-calendars>=0.6',
    ]
)
