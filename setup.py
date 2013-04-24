from setuptools import setup, find_packages
import os

version = '0.1'

setup(
    name='collective.geo.geoserver',
    version=version,
    description="Content for visualize a geoserver layer,",
    long_description=(
        open("README.rst").read() + "\n" + open(
            os.path.join("docs", "HISTORY.txt")).read()
    ),

    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet",
        "Topic :: Scientific/Engineering :: GIS",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='Zope Plone GIS KML Geoserver',
    author='Federico Cippino Guizzardi',
    author_email='cippinofg@gmail.com',
    url='https://github.com/collective/collective.geo.geoserver',
    license='gpl',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['collective', 'collective.geo'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'BeautifulSoup',
        'collective.geo.kml',
        'zope.component'
    ],
    extras_require={
        'test': [
            'plone.app.testing',
        ],
    },
    entry_points="""
        [z3c.autoinclude.plugin]
        target = plone
    """,
)
