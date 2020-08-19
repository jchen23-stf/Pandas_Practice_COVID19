import pandas as pd
import matplotlib.pyplot as plt
us_data = pd.read_csv('us-counties.csv')
# print(us_data.describe())
# print(us_data.head())
print(us_data.county)
is_ca_data = us_data['state']=='California'
ca_data = us_data[is_ca_data]
x = ca_data['date']
y = ca_data['deaths']
plt.plot(x,y)
plt.show()
