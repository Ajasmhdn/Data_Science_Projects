# -*- coding: utf-8 -*-
"""DataScience_Covid19_Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EtT2K5aRqO3Vc_aCJTRYaEWfEsqRbuRF
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv("/content/drive/MyDrive/csv_file/dpc-covid19-ita-andamento-nazionale.csv")
data.head()

data.columns

data.tail()

data.describe()

data.isnull().sum()

"""# **Relating the variables with scatterplots**"""

data.columns

# Assuming your dataframe is called df
# Create a dictionary that maps the Italian names to the English names
name_dict = {
    'data': 'date',
    'stato': 'state',
    'ricoverati_con_sintomi': 'hospitalized_with_symptoms',
    'terapia_intensiva': 'intensive_care',
    'totale_ospedalizzati': 'total_hospitalized',
    'isolamento_domiciliare': 'home_isolation',
    'totale_positivi': 'total_positive',
    'variazione_totale_positivi': 'change_in_total_positive',
    'nuovi_positivi': 'new_positive',
    'dimessi_guariti': 'discharged_recovered',
    'deceduti': 'deceased',
    'casi_da_sospetto_diagnostico': 'cases_from_suspected_diagnosis',
    'casi_da_screening': 'cases_from_screening',
    'totale_casi': 'total_cases',
    'tamponi': 'swabs',
    'casi_testati': 'tested_cases',
    'note': 'notes',
    'ingressi_terapia_intensiva': 'intensive_care_entries',
    'note_test': 'test_notes',
    'note_casi': 'case_notes',
    'totale_positivi_test_molecolare': 'total_positive_molecular_test',
    'totale_positivi_test_antigenico_rapido': 'total_positive_rapid_antigen_test',
    'tamponi_test_molecolare': 'molecular_test_swabs',
    'tamponi_test_antigenico_rapido': 'rapid_antigen_test_swabs'
}

# Use the rename function to replace the column names
data = data.rename(name_dict, axis='columns')

data.columns

sns.relplot(x="total_cases", y="discharged_recovered",hue='discharged_recovered', data=data)

sns.pairplot(data)

sns.relplot(x='hospitalized_with_symptoms', y='home_isolation', kind='line', data=data)

sns.catplot(x="total_cases", y="discharged_recovered",hue='discharged_recovered', data=data)