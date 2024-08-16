"""_summary_
    This is a file that will contain the code required to launch a pre-processor for the program
    This is also where input arguments will be managed
"""

import os
import sys
from sys import argv
from display_tty import IDISP

from .mdi2tiff import MDIToTiff
from . import constants as CONST
from .change_image_format import AVAILABLE_FORMATS, AVAILABLE_FORMATS_HELP


class Main:
    """_summary_
    This is the main class of the program
    """

    def __init__(self, success: int = CONST.SUCCESS, error: int = CONST.ERROR, show: bool = True, debug: bool = False) -> None:
        self.argv = argv[1:]
        self.argc = len(self.argv)
        self.success = success
        self.error = error
        self.binary_name = ""
        self.debug = debug
        self.show = show
        self.src = ""
        self.dest = ""
        self.available_formats = AVAILABLE_FORMATS
        self.dest_found = False
        self.output_format = "default"
        self._check_args()
        self.const = CONST.Constants(self.binary_name, self.output_format)
        if self.dest_found is False:
            self.dest = self.const.temporary_img_folder
        self.const.debug = self.debug
        self.mdi_to_tiff_initialised = MDIToTiff(
            self.const,
            self.success,
            self.error
        )

    def _check_output_format(self, output: str) -> str:
        """_summary_
        Check the output format provided by the user and return it if correct.

        Args:
            output (str): _description_: The output provided by the user.

        Returns:
            str: _description_: The format after the check.
        """
        data = output.lower()
        if data in self.available_formats:
            return data
        else:
            IDISP.logger.warning(
                "(mdi2img) The format '%s' is not supported, using the default format.",
                f"{data}"
            )
            return self.output_format

    def _disp_version(self) -> None:
        """_summary_
        Display the version of the program
        """
        print(f"The version of this program is: {CONST.__version__}")

    def _help_section(self) -> None:
        """_summary_
        Display the help section of the program
        """
        print("USAGE:")
        msg = f"\t{argv[0]} <<-h>|<-v>|<SRC>> [DEST]"
        msg += "[--debug] [--no-show] [--format=<format>]"
        print(msg)
        print()
        print("KEEP IN MIND:")
        print("When exporting/viewing/saving images, the default output format is tiff.")
        print("Use the --format flag to change the export format.")
        msg = "When no destination is specified, "
        msg += f"the default one is '{CONST.TMP_IMG_FOLDER}'"
        print(msg)
        print()
        print("ARGUMENTS:")
        print(
            "\tINFO: '<argument>' --> required, '[argument]' --> optional '|' --> one or the other"
        )
        print("\t<SRC>            \tMust be either:")
        print("\t<-h>|<--help>    \tDisplay this help section and exit.")
        print("\t<-v>|<--version> \tDisplay the program's version and exit.")
        print("\t                 \t- a path to an mdi file")
        print("\t                 \t- a path to a folder containing mdi files")
        print("\t[DEST]           \tMust be either:")
        print("\t                 \t- the name of the output file")
        print("\t                 \t- the name of the output folder")
        print(
            "[--debug|-d]         \tThis option will display additional information about what the program is doing."
        )
        print(
            "[--no-show|-ns]      \tThis option will instruct the program not to display the images once they were converted"
        )
        print(
            "[--format=<format>]  \tThis option allows you to change the default output format (tiff)"
        )
        print("ABOUT:")
        print(f"This program was created by {CONST.__author__}")
        self._disp_version()
        print()
        question = "Do you wish to see a list of the "
        question += f"{len(self.available_formats)} "
        question += "available formats [(y)es/(N)o]: "
        if input(question).lower() in ("y", "yes", "yas", "ye", "ys"):
            print("The available formats are:")
            index = 1
            for i in self.available_formats:
                print(f"\t{index}. '{i}': {AVAILABLE_FORMATS_HELP[i]}")
                index += 1

    def _check_args(self) -> None:
        """_summary_
        Check the arguments passed to the program
        """
        src_found = False
        self.dest_found = False
        if self.argc == 0:
            self._help_section()
            sys.exit(self.error)
        if self.argv[0].lower() in ("-h", "--help"):
            self._help_section()
            sys.exit(self.success)
        if self.argv[0].lower() in ("-v", "--version"):
            self._disp_version()
            sys.exit(self.success)
        for i in self.argv:
            arg = i.lower()
            is_path = os.path.exists(i)
            if is_path is True and src_found is False:
                self.src = i
                src_found = True
                continue
            if is_path is True and src_found is True and self.dest_found is False:
                self.dest = i
                self.dest_found = True
                continue
            if is_path is True and self.dest_found is True:
                IDISP.logger.warning(
                    "(mdi2img) Argument '%s' was not expected, ignoring it.",
                    f"{i}"
                )
                continue
            if arg in ("--debug", "-d"):
                self.debug = True
                continue
            if arg in ("--no-show", "-ns"):
                self.show = True
                continue
            if arg.startswith("--format"):
                self.output_format = self._check_output_format(
                    arg.split("=")[1])
        if src_found is False:
            IDISP.logger.critical(
                "(mdi2img) No source path provided, aborting!"
            )
            sys.exit(self.error)

    def main(self) -> int:
        """_summary_
        This is the main function of this class.

        Returns:
            int: _description_: The return status of the call
        """
        return self.success
