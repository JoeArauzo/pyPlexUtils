import re
from setuptools import setup

pkg_version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('pyPlexUtils/pyPlexUtils.py').read(),
    re.M
    ).group(1)


with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

    
setup(
        name='pyPlexUtils',
        version=pkg_version,
        python_requires='>=3.6',
        description='Includes useful command-line tools for managing media files for use with Plex Media Server.',
        long_description=long_descr,
        url='git@github.com:JoeArauzo/pyPlexUtils.git',
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
