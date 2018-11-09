import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('../data/data.csv')
data

fig, ax = plt.subplots()

for key, grp in data.groupby(['participant_name']):
    ax = grp.plot(ax=ax, kind='line', x='trade_number', y='happiness_rating', label=key)
plt.legend(loc='best')
plt.xlabel('Number of trades')
plt.ylabel('Happiness Rating')
plt.title('Happiness of individuals with candy selection vs. number of candy trades')
plt.show()

fig.savefig('../results/fig1_happiness_of_individuals.png')
