from setuptools import setup, find_packages
import os

version = '1.0.0a1.dev0'
maintainer = '4teamwork'

tests_require = [
    'ftw.builder',
    'ftw.testing',
    'ftw.testbrowser',
]

extras_require = {
    'tests': tests_require,
}

setup(
    name='ftw.addressblock',
    version=version,
    description='ftw.addressblock',
    long_description=open('README.rst').read() + '\n' + open(
        os.path.join('docs', 'HISTORY.txt')).read(),

    # Get more strings from
    # http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Framework :: Plone',
        'Framework :: Plone :: 4.3.x',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    keywords='ftw addressblock simplelayout',
    author='4teamwork AG',
    author_email='mailto:info@4teamwork.ch',
    maintainer=maintainer,
    url='https://github.com/4teamwork/ftw.addressblock',
    license='GPL2',

    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['ftw', ],
    include_package_data=True,
    zip_safe=False,

    install_requires=[
        'ftw.simplelayout [contenttypes]',
        'ftw.upgrade',
        'Plone',
        'plone.app.dexterity',
        'plone.dexterity',
        'setuptools',
    ],

    tests_require=tests_require,
    extras_require=extras_require,

    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)