import matplotlib.pyplot as plt
import pandas as pd

def here(h) :
    path_base = "~/repos/python-playground"
    return path_base + "/" + h

dat = pd.read_csv(here("/data/iris.csv"))
dat.head(5)
dat.dtypes
dat.info()
dat.loc[:,"Species"]
dat.iloc[:,0]

x = dat.loc[:,"Sepal.Width"].values
y = dat.loc[:,"Sepal.Length"].values
c = dat.loc[:,"Species"].values
clrkey = list(set(c))
clrcode = ["red", "blue", "green"]
clrmap = {}

for i in range(len(clrkey)) :
    clrmap[clrkey[i]] = clrcode[i]

clrs = []
for i in range(len(c)) :
    clrs.append(clrmap[c[i]])

plt.scatter(x, y, c = clrs)
plt.show()
