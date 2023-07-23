import pandas as pd

dataset = pd.read_csv(r'country_vaccinations.csv')
print("Shape of given dataset: ",dataset.shape)
print("Count of column: ",len(dataset.columns))
print("Nmae of parameter used: ",dataset.columns)
print("Display empty row data: ",dataset.loc[:,dataset.isna().any()])