#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 12:47:29 2021

@author: osezeiyore
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 23:32:39 2021

@author: osezeiyore


CHALLENGE:
Can you write a query|line(s) of code to count the
number of male and female penguins with all numerical 
features above their species’ mean values?
"""

import pandas as pd


PENGUINS_DATA = (
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
)
df = pd.read_csv(
    PENGUINS_DATA,
)

#%% my initial solution

grouped_df=df.groupby('species')
d=pd.DataFrame()

for species, species_df in grouped_df:
    num_features=species_df.select_dtypes(include='number')
    d=d.append(species_df[~((num_features>num_features.mean()).sum(axis=1)-len(num_features.columns)).astype(bool)]) 
print(d['sex'].value_counts())


#%% alternate solution

df[(df.select_dtypes(include='number') > df.groupby('species').transform('mean')).all(axis=1)]['sex'].value_counts()
