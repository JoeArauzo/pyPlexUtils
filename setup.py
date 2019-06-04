from setuptools import setup

setup(
        name='pyPlexUtils',
        version='0.0.1',
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
