"""A module for arbitrary precision numerical types, operations and algorithms"""

class NumericContext(object):
    """A class containing the numeric context of a `Number`. Defaults to IEE 754r binary64 like context."""
    def __init__(self):
        self._local = True #
        self._base = 2
        self._exponent = 11
        self._significand = 52

class Number(object):
    """A user configurable number type and interface for wrapping the numerical routines. All public numerical routines should expect types implementing the `Number` interface. Also the default type. Still pondering defaults.

Probably will make implement this class as necessary and attempt to build on the mpmath module as much as possible. Will focus on developing with local working precision rather than global. Each `Number` has a `_local` attribute that, when set to `True` asserts that the `Number` uses a local context."""
    def __init__(self):
        self.context = NumericContext()

