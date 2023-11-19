"""
File in charge of displaying a converted image
"""

import os
import tkinter as tk
from window_asset_tkinter import WindowAsset as WA


class ViewImage(WA):
    """
    The class in charge of displaying the image
    """

    def __init__(self, success: int = 0, error: int = 1) -> None:
        super(ViewImage, self).__init__()
        self.success = success
        self.error = error

    def view(self, image_path: str) -> int:
        """
        Display an image
        :param image_path: The path to the image to display
        :return: The status of the display (success:int  or error:int)
        """
        if os.path.exists(image_path) is False:
            return False
        root = tk.Tk()
        root.title("MDI2IMG")
        root.geometry("800x600")
        root.resizable(False, False)
        image = tk.PhotoImage(file=image_path)
        label = tk.Label(root, image=image)
        label.pack()
        root.mainloop()
        return True
