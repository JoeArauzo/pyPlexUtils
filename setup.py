import re
from setuptools import setup

pkg_version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('pyPlexUtils/pyPlexUtils.py').read(),
    re.M
    ).group(1)

    
setup(
        name='pyPlexUtils',
        version=pkg_version,
        description='Includes useful command-line tools for managing media files for use with Plex Media Server.',
        url='git@github.com:JoeArauzo/python-test-package.git',
        author='Joe Arauzo',
        author_email='joe@arauzo.net',
        license='GPLv3+',
        packages=['pyPlexUtils'],
        install_requires=['Click','sh'],
        entry_points = {
                "console_scripts": ['clear-mkvchptnames = pyPlexUtils.pyPlexUtils:clear_mkvchptnames']
                },
        zip_safe=False
)
