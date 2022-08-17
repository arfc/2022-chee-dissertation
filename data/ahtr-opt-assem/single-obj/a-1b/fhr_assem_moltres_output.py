import pandas as pd 

df = pd.read_csv('fhr_assem_moltres_csv.csv')
print({"max_temp": list(df['temp_max'])[-1]})