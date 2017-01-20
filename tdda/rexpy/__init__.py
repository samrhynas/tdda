"""
rexpy: Easier regular expression generation

Rexpy infers regular expressions on a line-by-line basis from text data
examples.

To run the rexpy tool:

    python -m tdda.rexpy.rexpy [inputfile]

For details, including API use:

    >>> import tdda.rexpy.rexpy
    >>> help(tdda.rexpy.rexpy)

To copy examples to a specified directory:

    python -m tdda.constraints.examples mydirectory

"""

from tdda.rexpy.rexpy import *