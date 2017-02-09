"""
This is a separated module meant to go along with the main module. It contains functions related to initializing our
logging for the main script.
"""

# Note that importing is lazy -- things are imported only when they need to be,
# and if the module/package is already imported, it won't be re-imported.

# logging is a builtin Python module that contains methods for logging what's happening in your script.
# Writing logs is a good way to let the script user know what's happening, and is generally a good idea.
# In general, you should be reasonably verbose, but don't drown people in logs (or comments). Just enough to let
# the person running the script know what's going on.
import logging
import sys  # This is a module that lets you reference and do things to the system you're operating on.


def initialize_logger():
    # Do a basic configuration of runtime logging, where the minimum warning level is INFO, and
    # logs are printed to stdout -- when data are sent to stdout, they are printed to the console
    # window.
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logging.info('Logging initialized.')
    # Note that if you don't use the 'return' statement, then by default functions return the value None

