import argparse
from typing import *
import shlex
import pytest
import simple_parsing
from simple_parsing import InconsistentArgumentError, ParseableFromCommandLine


class Setup():
    @classmethod
    def setup(cls: ParseableFromCommandLine, arguments = "", multiple = False) -> str:
        parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        cls.add_arguments(parser, multiple=multiple)
        # BUG: the arguments might have quotes in them, hence we shouldn't necessarily just split() with whitespace..
        splits = shlex.split(arguments)
        args = parser.parse_args(splits)
        return args
    
    @classmethod
    def get_help_text(cls: ParseableFromCommandLine, multiple=False):
        import contextlib
        from io import StringIO
        f = StringIO()
        with contextlib.suppress(SystemExit), contextlib.redirect_stdout(f):
            _ = cls.setup("--help")
        s = f.getvalue()
        return s
