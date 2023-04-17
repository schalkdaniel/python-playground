import pandas as pd
import xgboost as xgb
from sklearn.model_selection import GridSearchCV, cross_val_score, KFold
from sklearn.preprocessing import OrdinalEncoder

# Load a dataset as a pandas DataFrame
df = pd.read_csv('data/iris.csv')
target = 'Species'

# Split the data into features and labels
X = df.drop(target, axis=1)

encoder = OrdinalEncoder()
y = encoder.fit_transform(df[[target]])
# y = df[target]

# Define the XGBoost model
model = xgb.XGBClassifier()

# Define the hyperparameter search space
param_grid = {
    'max_depth': [2, 3],
    'learning_rate': [0.1, 0.01],
    'n_estimators': [50, 100, 200],
    'gamma': [0, 0.1, 0.5],
    'subsample': [0.5, 0.8, 1.0],
    'colsample_bytree': [0.5, 0.8, 1.0]
}

# Define the outer cross-validation strategy
outer_cv = KFold(n_splits=5, shuffle=True, random_state=42)

# Define the inner cross-validation strategy
inner_cv = KFold(n_splits=5, shuffle=True, random_state=42)

# Create an instance of the GridSearchCV class with the XGBoost model, the hyperparameter search space, the inner cross-validation strategy, and the scoring metric
grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    scoring='accuracy',
    cv=inner_cv,
    n_jobs=-1
)

# Perform the nested cross-validation and print the results
outer_scores = cross_val_score(
    estimator=grid_search,
    X=X,
    y=y,
    cv=outer_cv,
    n_jobs=-1
)

print('Nested CV accuracy: {:.2f} +/- {:.2f}'.format(outer_scores.mean(), outer_scores.std()))

outer_scores2 = cross_val_score(
    estimator=model,
    X=X,
    y=y,
    cv=outer_cv,
    n_jobs=-1,
    scoring=
)



model.fit(X, y)
model.predict(X)
