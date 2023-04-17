import re
import pandas as pd
from math import sqrt
from random import choices
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv('../data/iris.csv')

df.info()
df.describe() # Summary
df.head(5)
df.tail(5)

# Handle columns:
# -----------------------------------------------------------------------------

df['int_dummy'] = choices(range(2), k = df.shape[0]) # New column
df['Sepal.Width']                                    # Get one column
df[['Sepal.Width', 'Sepal.Length']]                  # Get multiple columns
df.select_dtypes('float')                            # Get all columns of type float
df.select_dtypes(['float', 'int'])                   # Get all columns of type float and int
df.select_dtypes(['float', 'int', 'object'])         # ...

df['Species'].str[0:3]

# Column wise functions:
df.sum()
df.max()
df.select_dtypes('float').quantile([0.1, 0.5, 0.9])

df[filter(lambda x: 'Sepal' in x, df.columns)]           # Filter for Sepal
df[filter(lambda x: re.search(r'^.+\.', x), df.columns)] # Filter with regexp

df['tmp1'] = 1
df['tmp2'] = 2
df = df.rename(columns = {'tmp2': 'tmp3'})
df = df.drop(['tmp1', 'tmp3'], axis = 1)

# Handle rows:
# -----------------------------------------------------------------------------

df[df['Species'] != 'versicolor'] # Drop versicolor rows
df[(df['Species'] != 'versicolor') & (df['Sepal.Width'] < 3)]
df[pd.notnull(df['Species'])]
df[pd.notnull(df).any(axis = 1)]

df.select_dtypes('float').sum(axis = 1)
df.select_dtypes('float').max(axis = 1)

# Apply:
# -----------------------------------------------------------------------------

def l2norm(x):
    return sqrt((x**2).sum())

df.select_dtypes(['float', 'int']).apply(l2norm, axis = 0)
df.select_dtypes(['float', 'int']).apply(l2norm, axis = 1)
df['norm'] = df.select_dtypes(['float', 'int']).apply(l2norm, axis = 1)

# Aggregate by group:
# -----------------------------------------------------------------------------

df.groupby('Species')[['Sepal.Width', 'Sepal.Length']].agg(l2norm)
df.groupby('Species')[['Sepal.Width', 'Sepal.Length']].agg([l2norm, sum])

df \
    .groupby('Species')[['Sepal.Width', 'Sepal.Length']] \
    .agg(lambda x: sqrt((x**2).sum())) # With lambda

dfg = df.groupby('Species', as_index = False)[['Sepal.Width', 'Sepal.Length']].agg(l2norm)

# Joins:
# -----------------------------------------------------------------------------

df.merge(dfg, on = 'Species', how = 'left', suffixes = ["", "_agg"])
df.merge(dfg, left_on = 'Species', right_on = 'Species', how = 'left', suffixes = ["_x", "_y"])

# Missings:
# -----------------------------------------------------------------------------




# Replace values (e.g., outliers):
# -----------------------------------------------------------------------------

# Basic visualizations with pandas:
# -----------------------------------------------------------------------------

#cvals = set(df['Species'].values)
ccode = pd.Categorical(df['Species'])
vcols = mpl.colormaps['Set1']

from matplotlib.colors import ListedColormap

colors = ['red', 'blue', 'green']  # List of colors for each category
cmap = ListedColormap(colors)

df.plot.scatter(x = 'Sepal.Width', y = 'Sepal.Length', c = 'Species', colormap = cmap,)
plt.show()

df.plot.box()
df.plot.box(vert = False)
plt.show()

from plotnine import *
(ggplot(df)
    + geom_point(aes(x = 'Sepal.Length', y = 'Sepal.Width', color = 'Species'))
    + theme_minimal()
    + ggtitle('My plot')
    + xlab("XXXX")
    + ylab("YYYY")
    # + theme(legend_position = 'bottom')
    + scale_color_brewer(palette=2)
)
