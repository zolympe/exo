#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 16:11:26 2020

@author: jupiter
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import re

page_max=10
item_max_per_page=16

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
url="https://www.mec.ca/fr/sexe/hommes/produits/bottes-et-chaussures/chaussures/c/1195?page=1"

dataframe =pd.DataFrame()
myDict={ "brand":[] ,"price":[]}

for page in range(0,page_max):
    response = requests.get("https://www.mec.ca/fr/sexe/hommes/produits/bottes-et-chaussures/chaussures/c/1195?page={0}".format(page), headers=headers)
    print("statut de lecture de la page {:d} {:d}".format(page,response.status_code))

    # verification du code retour ok=200
    if (response.status_code==200) :
        print("ok")
    else:
        print("Houston we have a problem : jump to next page")
        continue
    
    # recuperation du contenu
    content = response.content
    
    # Parser BeautifulSoup
    soup = BeautifulSoup(content, "html.parser")

    # recherche des div contenant les chaussures     
    search_list = soup.find_all("div", {"class" : "flexigrid__tile__content"})
    
    CountDismiss=0 # compter les lignes incompletes
    CountOk=0      # compter les lignes completes
    for i in search_list:
        b=0 # pour verifier que le libelle est ok
        p=0 # pour verifier que le prix est ok
        brand=i.find("a",{"class":re.compile('product__name__link*')})
        if (brand):
            b=1
            brandTxt=brand.text
        price=i.find("li",{"class":"price"})
        if (price):
            p2=price.find_all(text=True,recursive=False)
            p=1
            priceTxt=p2[-1].strip()
            seekMinus=priceTxt.find('–')
            print(seekMinus)
            if seekMinus>0:
                 priceTxt=priceTxt[seekMinus+1:].strip()
        if (p and b): # si on a une ligne complete
            print(brandTxt + priceTxt) 
            CountOk+=1
            myDict['brand'].append(brandTxt)
            myDict['price'].append(priceTxt)
        if (p+b<2):
            print("One item was dismissed")
            CountDismiss+=1
    # bilan de page
    print("Page {:d} : {:d} read and {:d} dismiss".format(page,CountOk,CountDismiss))

df=pd.DataFrame(myDict)
df.to_csv("mec_chaussure.csv")

