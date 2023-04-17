# LM python module/package

```python
from lm import lm

bd = lm.here("~/repos/python-playground/lm-module")
path = "data/iris.csv"
df = pd.read_csv(path)

type(df)
type(df).__name__

print(df.to_string())
df.loc[:, "Sepal.Length"]
df.loc[:, ["Sepal.Length", "Species"]]
df.iloc[:, [2, 3]]

modelMatrix(df)
lm(df, "Sepal.Width")
```
