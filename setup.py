from setuptools import find_packages, setup

dependencies = []
setup_requires = ['setuptools_scm']

setup(
    name = "exporter_proxy",
    setup_requires=setup_requires,
    use_scm_version=True,
    url = "https://github.com/mrichar1/exporter_proxy",
    license='LICENSE.md',
    author = "Matthew Richardson",
    author_email = "",
    description='Pure-python reverse proxy for Prometheus exporters with TLS support.',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    data_files = [
        ("share/licenses/exporter_proxy", ["LICENSE"]),
        ("share/doc/exporter_proxy", ["README.md"]),
        ('/usr/lib/systemd/system', ['exporter_proxy@.service'])
    ],
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    scripts = ['exporter_proxy'],
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)


