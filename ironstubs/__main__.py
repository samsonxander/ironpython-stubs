""" Stub Generator for IronPython

Extended script based on script developed by Gary Edwards at:
gitlab.com/reje/revit-python-stubs

This is uses a slightly modify version of generator3,
github.com/JetBrains/intellij-community/blob/master/python/helpers/generator3.py

Iterates through a list of targeted assemblies and generates stub directories
for the namespaces using pycharm's generator3.

Note:
    Some files ended up too large for Jedi to handle and would cause
    memory errors and crashes - 1mb+ in a single files was enough to
    cause problems. To fix this, there is a separate module that creates
    a compressed version of the stubs, but it also split large file
    into separate files to deal with jedi.
    These directories will show up in the stubs as (X_parts)


MIT LICENSE
https://github.com/gtalarico/ironpython-stubs
Gui Talarico
"""

import sys
import os
import re
import json
import time
from pprint import pprint

from utils.docopt import docopt
from utils.logger import logger
from utils.helper import Timer
from default_settings import PATHS, BUILTINS, ASSEMBLIES
from make_stubs import make

__version__ = '1.0.0'
__doc__ = """
    IronPython-Stubs | {version}

    IronPython Stubs Generator

    Usage:
      ironstubs
      ironstubs make (<assembly-name>|--all) [--directory=<dir>] [--overwrite] [--no-json]

    Examples:
      ipy -m ironstubs RhinoCommon

    Options:
        --all                         Process all Assemblies in the default_settings.py
        --directory=<dir>             Path of Output Directory [default: {out_dir}]
        --overwrite             Force Overwrite if stub already exists [default: False].
        --no-json                     Don't write json file [default: False].
        -h, --help                    Show this screen.

    """.format(out_dir='stubs', version=__version__)

arguments = docopt(__doc__, version=__version__)

# OPTIONS
option_assembly = arguments['<assembly-name>']
option_all = arguments['--all']
option_output_dir = arguments['--directory']
option_overwrite = arguments['--overwrite']
option_no_json = not arguments['--no-json']


PROJECT_DIR = os.getcwd()  # Must execute from project dir
PKG_DIR = os.path.dirname(__file__)
PATHS, BUILTINS, ASSEMBLIES
[sys.path.append(p) for p in PATHS] # Add Paths
release_dir = os.path.join(PKG_DIR, 'release', option_output_dir)
# logger.info(arguments)

if arguments['make']:
    timer = Timer()
    make(release_dir, assemblies=[option_assembly],
        builtins=None, overwrite=option_overwrite)
    print('Done: {} seconds'.format(timer.stop()))

# if arguments['make_all']:
    # make(option_output_dir, assemblies=None, builtins=None, overwrite=False):


