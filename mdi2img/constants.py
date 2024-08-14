##
# EPITECH PROJECT, 2024
# MDI2IMG (Workspace)
# File description:
# constants.py
##

import os
from typing import Union
import display_tty as DTY

SUCCESS = 0
ERROR = 1
ERR = ERROR


class Constants:
    """_summary_
    This is the class that will store general methods and variables that will be used over different classes.
    """

    def __init__(self, binary_name: str = "MDI2TIF.EXE") -> None:
        self.env = os.environ
        self.binary_name = binary_name
        self.in_directory = f"{os.getcwd()}/in"
        self.out_directory = f"{os.getcwd()}/out"
        self.dttyi = DTY.Disp(
            toml_content=DTY.TOML_CONF,
            save_to_file=False,
            file_name="",
            file_descriptor=None,
            debug=False,
            logger=None
        )
        self.temporary_folder = self._get_temp_folder(self.env)
        self.temporary_img_folder = f"{self.temporary_folder}/mdi_to_img_temp"
        self._create_temp_if_not_present()
        self.binary_path = self._find_mdi2tiff_binary(self.binary_name)

    def _get_temp_folder(self, env: dict[str, str]) -> str:
        """_summary_
        Check the computer environement to see if the wished key is present.

        Returns:
            str: _description_: The value of the research.
        """
        if "TEMP" in env:
            return env["TEMP"]
        if "TMP" in env:
            return env["TMP"]
        return os.getcwd()

    def _find_mdi2tiff_binary(self, binary_name: str = "MDI2TIF.EXE") -> Union[str, None]:
        """
        Search for the mdi2tiff binary in the module's directory.
        :param binary_name: The name of the binary to locate
        :return:
            str: Full path to the mdi2tiff binary if found, None otherwise.
        """

        current_script_directory = os.path.dirname(os.path.abspath(__file__))
        binary_path = os.path.join(
            current_script_directory, "bin", binary_name)
        if os.path.exists(binary_path) is True:
            return binary_path
        return None

    def _create_temp_if_not_present(self) -> None:
        """_summary_
        Create the temporary folder if it does not exist.
        """
        if os.path.exists(self.temporary_img_folder) is False:
            self.pinfo("Temporary export location does not exist. Creating.")
            try:
                os.makedirs(self.temporary_img_folder, exist_ok=True)
                msg = "Temporary export folder created in: "
                msg += f"'{self.temporary_img_folder}'."
                self.psuccess(msg)
            except os.error as e:
                msg = "Error creating temporary export location ('"
                msg += f"{self.temporary_img_folder}'): {e}"
                self.pcritical(msg)

    def perror(self, string: str = "") -> None:
        """_summary_
        This is a function that will output an error on the terminal.

        Args:
            string (str, optional): _description_. Defaults to "".
        """
        self.dttyi.logger.error("(mdi2img) %s", string)

    def pwarning(self, string: str = "") -> None:
        """_summary_
        This is a function that will output a warning on the terminal.

        Args:
            string (str, optional): _description_. Defaults to "".
        """
        self.dttyi.logger.warning("(mdi2img) %s", string)

    def pcritical(self, string: str = "") -> None:
        """_summary_
        This is a function that will output a critical error on the terminal.

        Args:
            string (str, optional): _description_. Defaults to "".
        """
        self.dttyi.logger.critical("(mdi2img) %s", string)

    def psuccess(self, string: str = "") -> None:
        """_summary_
        This is a function that will output a success message on the terminal.

        Args:
            string (str, optional): _description_. Defaults to "".
        """
        self.dttyi.logger.success("(mdi2img) %s", string)

    def pinfo(self, string: str = "") -> None:
        """_summary_
        This is a function that will output an information message on the terminal.

        Args:
            string (str, optional): _description_. Defaults to "".
        """
        self.dttyi.logger.info("(mdi2img) %s", string)

    def err_item_not_found(self, directory: bool = True,  item_type: str = "input", path: str = '', critical: bool = False, additional_text: str = "") -> None:
        """_summary_
        This is a function that will output an error message when a directory is not found.

        Args:
            directory (bool, optional): _description_: Is the item a directory. Defaults to True.
            item_type (str, optional): _description_: The type of the item.
            path (str, optional): _description_: The path of the directory.
            critical (bool, optional): _description_ Is the message of critical importance. Defaults to True.
        """
        dir_str = "directory"
        if directory is False:
            dir_str = "file"
        msg = f"The {item_type} {dir_str} ('{path}') was not found!"
        msg += f"{additional_text}"
        if critical is True:
            msg += "\n Aborting operation(s)!"
            self.pcritical(msg)
        else:
            self.pwarning(msg)

    def err_binary_path_not_found(self) -> None:
        """_summary_

        Args:
            critical (bool, optional): _description_ Is the message of critical importance. Defaults to True.
        """
        msg = f"Binary path: '{self.binary_path}' was not found."
        msg += "\nAborting operations."
        self.pcritical(msg)
