"""
File in charge of locating the binary in charge of converting mdi file to tiff file
"""

import os


def find_mdi2tiff_binary(binary_name: str = "MDI2TIF.EXE") -> str | None:
    """
    Search for the mdi2tiff binary in the module's directory.
    :param binary_name: The name of the binary to locate
    :return:
        str: Full path to the mdi2tiff binary if found, None otherwise.
    """

    current_script_directory = os.path.dirname(os.path.abspath(__file__))
    binary_path = os.path.join(current_script_directory, "bin", binary_name)
    if os.path.exists(binary_path) is True:
        return binary_path
    return None
