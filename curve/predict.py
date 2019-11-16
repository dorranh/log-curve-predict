"""
Base module for utilities for log-curve-predict models.
"""

import os
import fnmatch
import numpy as np
import pandas as pd


def read_all_synthetic_curves(curve_dir, null_value="-999.00000000"):
    """Quick and dirty method for parsing the synthetic data files created for the hackathon"""
    data_files = fnmatch.filter(os.listdir(curve_dir), "*\/\d+$")
    curves = {}
    for data_file in data_files:
        data_file_path = os.path.join(curve_dir, data_file)
        curve, well_num = data_file.split("_")
        with open(data_file_path, 'r') as f:
            l = [line.strip() for line in f.readlines()]
        x, y = l[0].split(",")
        x = float(x.strip())
        y = float(y.strip())
        data = np.genfromtxt(l[1:], missing_values=null_value, autostrip=True, delimiter=",", usemask=True)
        df = pd.DataFrame(data, columns=["depth", curve])
        df["x"] = x
        df["y"] = y
        if well_num not in curves:
            curves[well_num] = df
        else:
            curves[well_num][curve] = df[curve]
    return curves

