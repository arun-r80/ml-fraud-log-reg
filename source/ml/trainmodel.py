# -*- coding: utf-8 -*-
"""
Created on Fri May 25 07:24:03 2018

@author: aruramam
"""

import pandas as pd
import numpy as np
import os
import pathlib as pathlib

#################################################################3
# =============================================================================
url = os.path.join('ml-config','claim\claimtype.csv')
claimtype = pd.read_csv(url,delimiter='\s+', header=0)
print(claimtype['NO'])
# df = claimtype.loc[claimtype.NO > 1,'PendCode']
# print(df)
# =============================================================================

url2 = os.path.join('ml-config','trainingdata\\trainingdata_01.csv')
print(url2)
trainingdata_csv=pd.read_csv(url2, header=0)
print(trainingdata_csv)


