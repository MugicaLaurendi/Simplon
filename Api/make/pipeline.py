import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import statsmodels.api as sm
import statsmodels.stats.api as sms
import warnings
warnings.filterwarnings('ignore')

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn import set_config
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
from statsmodels.compat import lzip


# Pipeline

def print_modele():


        data = sns.load_dataset("tips")

        y = data['tip']
        X = data.drop(columns=['tip'])

        X_train_3,X_test_3, y_train_3, y_test_3 = train_test_split(X, y, test_size=0.3, random_state=60)

        num_pipeline = Pipeline([
                                ('imputer', SimpleImputer(strategy="median")),
                                ('minmax_scaler', MinMaxScaler())
                                ])

        cat_transformer = OneHotEncoder(handle_unknown='ignore', drop='first')

        preprocessor = ColumnTransformer([
                                        ('num_transformer', num_pipeline, ["size","total_bill"]),
                                        ('cat_transformer', cat_transformer, ["sex","smoker","day","time"])
                                        ])

        pipeline_workflow = make_pipeline(preprocessor, LinearRegression())
        pipeline_workflow_ridge = make_pipeline(preprocessor, Ridge())

        pipeline_workflow.fit(X_train_3,y_train_3)
        pipeline_workflow.score(X_test_3, y_test_3)
        y_pred = pipeline_workflow.predict(X_test_3)

        pickle.dump(pipeline_workflow, open('pipline.pkl', 'wb'))
        pickled_model = pickle.load(open('pipline.pkl', 'rb'))
        pickled_model.score(X_test_3, y_test_3)
