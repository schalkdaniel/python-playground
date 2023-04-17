from os import path
import pandas as pd
import numpy as np

class here :
    def __init__(self, base_dir = "") :
        self.base_dir = ""
        self.here(base_dir)
    
    def here(self, append) :
        bnew = self.base_dir + "/" + append
        if (path.isdir(bnew)) :
            self.base_dir = bnew
        else :
            raise Exception("Directory does not exist!")
    
    def file(self, file) -> str :
        f = self.base_dir + "/" + file
        if (path.isfile(f)) :
            return f
        else :
            raise Exception("File does not exist!")

def modelMatrix(df):
    n = df.shape[0]
    
    # Create empty data matrix with just an intercept column:
    cnames = df.columns
    X = np.empty(shape = (n, 0), dtype = float)
    X = np.append(X, np.array([np.repeat(1,n)]).transpose(), axis = 1)
    
    # Also init a names vector with the intercept:
    Xnames = ["Intercept"]
    for cn in cnames:
        ea = []
        if df.dtypes.loc[cn] == "O":
            x = df.loc[:, cn]
            classes = x.unique()
            for gn in np.delete(classes, 0):
                bseries = x == gn
                iseries = bseries.astype(int)
                ea.append(iseries)
                Xnames.append(cn + "." + gn)
        else:
           ea.append(df.loc[:, cn].to_numpy())
           Xnames.append(cn)
        ea = np.array(ea).transpose()
        X = np.append(X, np.array(ea), axis = 1)
    return {'cnames': Xnames, 'matrix': X}

def lm(df, target) :
    tnum = df.loc[:, target].to_numpy()
    mm = modelMatrix(df.drop(columns = target))
    X = mm['matrix']
    XtX = np.dot(X.transpose(), X)
    XtXinv = np.linalg.inv(XtX)
    Xty = np.dot(X.transpose(), tnum)
    return pd.DataFrame(data = {'cnames': mm["cnames"], 'coef': np.dot(XtXinv, Xty)})

