import pandas as pb 
import numpy as np

df_regiony = pb.read_csv('zadanie_3.csv') 

regiogrup = df_regiony.groupby('Region')['Amount'].sum()

