# -*- coding: utf-8 -*-
"""
@author: Marco Antonio Vieira Morais
@email: marco.morais@ifmt.edu.br
Objetivo: Impelmentação para baixar as imagens do TOPODATA
"""

import os
import requests
import pandas as pd

# Diretorio de saída
dir_out = "C:\\Imagens_download"

# Site com dados
topodata = "http://www.dsr.inpe.br/topodata/data/geotiff/"

# Lendo arquivo com os nomes dos arquivos
arq_nomes = "C:/Users/ecoge/Desktop/nomes_arq_topodata.csv"
td_nomes = pd.read_csv(arq_nomes)

# Filtrando os nomes para altitude númerica ZN
zn = td_nomes[td_nomes["Tipo"] == "ZN"]

"""
Códigos dos dados disponíveis para download no site do INPE
ZN - Altitude - numérica	
SN - Declividade - numérica
ON - Orientação - numérica
VN - v. Vertical - numérica
HN - rv. Horizontal - numérica
SA - Declividade - classes
SB - Declividade - classes
SC - Declividade - classes
OC - Orientação - octantes
V3 - Curv. Vertical - 3 classes
V5 - Curv. Vertical - 5 classes
H3 - Curv. Horizontal - 3 classes
H5 - Curv. Horizontal - 5 classes
FT - Forma de terreno - classes
RS - Relevo sombreado – numérico
DD - ADD - divisores e talvegue
"""

# Fazendo o Download
for nome in zn["Nome"]:
    url = topodata + nome
    response = requests.get(url)
    if response.status_code == 200:
        arq = os.path.join(dir_out, nome)
        with open(arq, "wb") as f:
            f.write(response.content)
