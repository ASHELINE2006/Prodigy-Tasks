import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
dataset = pd.read_csv('population.csv')
print(dataset)
dataset_cleaned = dataset.dropna()
print(dataset_cleaned)
dataset_cleaned.head()
dataset_final = dataset_cleaned.drop(['Series Name','Series Code','Country Code'],axis=1)
selected_country = 'Andorra'
country_values = dataset_final[dataset_final['Country Name'] == selected_country]
years = country_values.columns[1:]
population = country_values.iloc[:,1:].values.flatten()
plt.figure(figsize = (10,6))
plt.bar(years, population, color = 'red', align = 'center')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title(f'Population of {selected_country} over the years')
plt.show()
