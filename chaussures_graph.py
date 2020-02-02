#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 19:05:29 2020

@author: jupiter
"""

import pandas as pd
import matplotlib.pyplot as plt

synthese={ "seller":[],"maker":[],"meanPrice":[],"countIt":[]}
# Liste des marques
maker=('Scarpa','Vaja','La Sportiva','Salomon','Nike','Adidas','Keen','Asics','Oboz','Altra','North Face','Brooks','New Balance','Saucony','Forsake','Merrel','Merrell')
seller=('mec','sportexpert')

# chargement du CSV 
df=pd.read_csv("chaussures.csv")
df.sort_values(['seller','maker'])

for j in seller:
   for i in maker:
      dfTemporaire=df[(df['seller']==j) & (df['maker']==i)]
      if (dfTemporaire.empty==False):
          countIt=0
          Mean=0
          for index,k in dfTemporaire.iterrows():
              countIt=countIt+1
              Mean=Mean+k['price']
          synthese['seller'].append(j)
          synthese['maker'].append(i)
          synthese['meanPrice'].append(Mean)
          synthese['countIt'].append(countIt)

plot.


