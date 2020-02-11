# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("./train.csv")
df_clean = df.copy()

df_clean['MSSubClass'] = df.MSSubClass.apply(lambda x:f"SUBCLASS_{x}")
df_clean['LotFrontage'] = df.LotFrontage.fillna(value=np.mean(df.LotFrontage).astype(int))
df_clean['Alley'] = df.Alley.fillna(value="<UNK>")
df_clean['MasVnrType'] = df.MasVnrType.fillna(value="None").value_counts()

