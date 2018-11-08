import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('../data/data.csv')
data

data.boxplot('happiness_rating', by='trade_number', figsize=(12, 8))

plt.savefig('../results/fig2_distribution_of_happiness.png')
