
# Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the dataset
data_path = 'API_SP.POP.TOTL.FE.IN_DS2_en_csv_v2_433602.csv'
data = pd.read_csv(data_path, skiprows=4)

# Considering the year 2022 

# Distribution of Female Population for 2022
# Dropping rows with missing values for 2022
population_2022 = data[['Country Name', '2022']].dropna()

# Creating histogram
plt.figure(figsize=(10, 6))
sns.histplot(population_2022['2022'], bins=20, kde=True)
plt.title('Distribution of Female Population in 2022')
plt.xlabel('Female Population')
plt.ylabel('No. of Countries')
plt.show()

# Plotting the Trend of Female Population Over the Years for a Selected Country (here, India)
selected_country = 'India'  
country_data = data[data['Country Name'] == selected_country].iloc[:, 4:-1].T  
country_data.columns = ['Female Population']
country_data.index.name = 'Year'
country_data = country_data.reset_index()

# Creating line plot
plt.figure(figsize=(120, 60))
sns.lineplot(x='Year', y='Female Population', data=country_data)
plt.title(f'Trend of Female Population Over the Years in {selected_country}')
plt.xlabel('Year')
plt.ylabel('Female Population')
plt.xticks(rotation=90) 
plt.show()
