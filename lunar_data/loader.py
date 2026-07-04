"""
LunaVisionAI

Real Lunar Data Loader

This module is responsible for loading
Chandrayaan-2 DFSAR
OHRC
DEM

Currently:
Only architecture is implemented.

Later:
Real GeoTIFF and IMG support will be added.
"""

from pathlib import Path
import numpy as np

from config import RAW_DATA


class LunarDataLoader:

    def __init__(self):

        self.raw_path = RAW_DATA

    # --------------------------------------

    def check_dataset(self):

        if not self.raw_path.exists():

            raise FileNotFoundError(
                f"Raw Data Folder Not Found:\n{self.raw_path}"
            )

    # --------------------------------------

    def load_data(self):

        """
        Master Function

        Future Version

        Reads

        DFSAR

        OHRC

        DEM

        """

        self.check_dataset()

        lunar_data = {

            "dem": None,

            "radar": None,

            "cpr": None,

            "image": None

        }

        return lunar_data

    # --------------------------------------

    def dataset_info(self):

        self.check_dataset()

        files = list(self.raw_path.rglob("*"))

        print()

        print("========== Lunar Dataset ==========")

        for file in files:

            print(file)

        print()

        return files