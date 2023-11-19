"""
File in charge of converting mdi files to tiff
This extension relies on the windows mdi2tiff program
"""

import os
from .locate_binary import find_mdi2tiff_binary as FMDI2TIFFBIN


class MDIToTiff:
    """ 
    The class in charge of converting an mdi file to a tiff file
        :param success: The exit code of a successful conversion
        :param error: The exit code of a failed conversion
    """

    def __init__(self, binary_name: str = "MDI2TIF.EXE", success: int = 0, error: int = 1) -> None:
        self.success = success
        self.error = error
        self.bin_path = FMDI2TIFFBIN(binary_name)

    def convert(self, input_file: str, output_file: str) -> int:
        """
        Convert an mdi file to a tiff file
        :param input_file: The mdi file to convert
        :param output_file: The tiff file to create
        :return: The status of the convertion (success:int  or error:int)
        """
        if self.bin_path is None:
            return False
        if os.path.exists(input_file) is False:
            return False
        if os.path.exists(output_file) is True:
            return False
        command = f"{self.bin_path} {input_file} {output_file}"
        exit_code = os.system(command)
        if exit_code == self.success:
            return True
        return False

    def convert_all(self, input_directory: str, output_directory: str) -> int:
        """
        Convert all mdi files in a directory to tiff files
        :param input_directory: The directory containing the mdi files to convert
        :param output_directory: The directory where the tiff files will be created
        :return: The status of the convertion (success:int  or error:int)
        """
        if self.bin_path is None:
            return False
        if os.path.exists(input_directory) is False:
            return False
        if os.path.exists(output_directory) is False:
            return False
        for file in os.listdir(input_directory):
            if file.endswith(".mdi"):
                input_file = os.path.join(input_directory, file)
                output_file = os.path.join(
                    output_directory, file.replace(".mdi", ".tiff")
                )
                self.convert(input_file, output_file)
        return True
