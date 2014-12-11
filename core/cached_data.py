import pandas as pd

from sklearn.externals import joblib


model = joblib.load('core/data/general_model/general_model.pkl')
aggregate_data = pd.DataFrame.from_csv('core/data/aggregate_data.csv').reset_index().set_index('Tm')
