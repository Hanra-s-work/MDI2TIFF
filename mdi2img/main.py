"""_summary_
    This is a file that will contain the code required to launch a pre-processor for the program
    This is also where input arguments will be managed
"""

import sys
from sys import argv
from .mdi2tiff import MDIToTiff
from . import constants as CONST


class Main:
    """_summary_
    This is the main class of the program
    """

    def __init__(self, success: int = CONST.SUCCESS, error: int = CONST.ERROR) -> None:
        self.argv = argv[1:]
        self.argc = len(self.argv)
        self.success = success
        self.error = error
        self.binary_name = ""
        self._check_args()
        self.const = CONST.Constants(self.binary_name)
        self.mdi_to_tiff_initialised = MDIToTiff(
            self.const,
            self.success,
            self.error
        )

    def _help_section(self) -> None:
        """_summary_
        Display the help section of the program
        """
        print("USAGE:")
        print(
            f"\t{argv[0]} <<-h>|<SRC>> [DEST] [--debug] [--show] [--format=<format>]"
        )
        print("ARGUMENTS:")
        print(
            "\tINFO: '<argument>' --> required, '[argument]' --> optional '|' --> one or the other"
        )
        print("\t<SRC>         \tMust be either:")
        print("\t<-h>, <--help>\tDisplay this help section and exit.")
        print("\t              \t- a path to an mdi file")
        print("\t              \t- a path to a folder containing mdi files")
        print("\t[DEST]        \tMust be either:")
        print("\t              \t- the name of the output file")
        print("\t              \t- the name of the output folder")
        print(
            "[--debug]       \tThis option will display additional information about what the program is doing."
        )
        print(
            "[--show]        \tThis option will display the images once they were converted"
        )
        print(
            "[--format=<format>]\tThis option allows you to change the default output format (tiff)"
        )

    def _check_args(self) -> None:
        """_summary_
        Check the arguments passed to the program
        """
        if self.argc == 0:
            self._help_section()
            sys.exit(self.error)
        if self.argv[0] == "-h":
            self._help_section()
            sys.exit(self.success)

    def main(self) -> int:
        """_summary_
        This is the main function of this class.

        Returns:
            int: _description_: The return status of the call
        """
        return self.success
