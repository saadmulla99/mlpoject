import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.exception import CustomException
from src.logger import logging
import dill
import shutil
def save_object(file_path,obj):
    try:

        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        if os.path.isdir(file_path):
            shutil.rmtree(file_path)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)