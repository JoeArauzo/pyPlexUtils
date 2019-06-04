# -*- coding: utf-8 -*-


"""pyPlexUtils.pyPlexUtils: provides entry point main()."""


__version__ = "0.0.1"


import click
from .myfunctions import initclogger
from pathlib import Path
from datetime import datetime
import sh
import sys
import re
from .myfunctions import pathwoconflict
import os


@click.command()
@click.argument('file')
@click.option('--backupchapters', '-b', is_flag=True, 
              help="Backup chapters as xml file.")
def main(file, backupchapters):
    """
    This command-line tool inspects the metadata of a Matroska (MKV) media file
    for chapters and clears the names assigned to each chapter.  This is to
    ensure interoperability with Plex Media Server (https://www.plex.tv) which
    requires MKV chapter names to be unnamed.

    Matroska tools (https://mkvtoolnix.download/) needs to already be installed
    and accessible from the shell PATH in order for this tool to run.
    """
    
    
    # Initialize logging and begin
    logger = initclogger(__name__)
    logger.info(f"Executing clearmkvcnames version {__version__}.")

    # Exit if mkvtoolnix is not accessible
    if (not sh.which('mkvextract')) or (not sh.which('mkvpropedit')):
        sys.exit("MKVTOOLNIX is not accessible.  Please install.")

    # Exit if file does not exist
    mkvfile = Path(file).resolve()
    if not mkvfile.is_file():
        sys.exit("The file specified does not exist.")
    
    # Export MKV chapters as temporary xml
    tmpxmlfile = datetime.today().strftime('%Y%m%dT%H%M%S') + '.xml'
    tmpxmlfile = mkvfile.parent / tmpxmlfile
    try:
        logger.info(f"Inspecting '{mkvfile.name}' for chapters.")
        sh.mkvextract(mkvfile, 'chapters', tmpxmlfile)
    except sh.ErrorReturnCode_2:
        logger.error(f"The file '{mkvfile.name}' could not be opened for " +
                     "reading.  Not a valid Matroska file.")
        sys.exit(1)
    except sh.ErrorReturnCode:
        logger.error("An unknown error occurred when executing mkvextract.")
        sys.exit(1)

    # Search temporary xml for chapter name matches
    xmlfileobj = open(tmpxmlfile, 'r')
    xmltext = xmlfileobj.read()
    xmlfileobj.close()
    matches = re.findall("(?<=<ChapterString>).+(?=</ChapterString>)", xmltext)
    namedchptqty = len(matches)
    logger.info(f"{namedchptqty} chapters found.")

    # Create backup xml if matches exist and --backup-chapters option is set
    if namedchptqty and backupchapters:
        bakxmlfile = mkvfile.stem + ' chapters.xml'
        bakxmlfile = mkvfile.parent / bakxmlfile
        bakxmlfile = pathwoconflict(bakxmlfile)
        xmlfileobj = open(bakxmlfile, 'w+')
        xmlfileobj.write(xmltext)
        xmlfileobj.close()
        logger.info(f"Created backup of chapters in '{bakxmlfile.name}'.")

    # Clear chapter names if matches exist
    if namedchptqty:
        xmltext = re.sub('(?<=<ChapterString>).+(?=</ChapterString>)', '',
                         xmltext)
        xmlfileobj = open(tmpxmlfile, 'w+')
        xmlfileobj.write(xmltext)
        xmlfileobj.close()
        try:
            sh.mkvpropedit(mkvfile, '--chapters', tmpxmlfile)
            logger.info(f"{namedchptqty} chapters have been successfully " + 
                        "cleared.")
        except sh.ErrorReturnCode_2:
            logger.error(f"The file '{mkvfile.name}' could not be opened " +
                        "for writing.  Not a valid Matroska file.")
            sys.exit(1)
        except sh.ErrorReturnCode:
            logger.error("An unknown error occurred when executing " +
                         "mkvpropedit.")
            sys.exit(1)
    else:
        logger.info("No chapters to clear.")
    
    # Clean up
    os.remove(tmpxmlfile)