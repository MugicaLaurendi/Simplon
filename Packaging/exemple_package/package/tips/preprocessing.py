from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
import pandas as pd

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder

def scaler_cat(X_cat_train, X_cat_test):
    ohe = OneHotEncoder(sparse=False)
    ohe.fit(X_cat_train)
    X_cat_train_scaled = ohe.transform(X_cat_train)
    X_cat_train_scaled_df = pd.DataFrame(X_cat_train_scaled)

    X_cat_test_scaled = ohe.transform(X_cat_test)
    X_cat_test_scaled_df = pd.DataFrame(X_cat_test_scaled)
    return X_cat_train_scaled_df, X_cat_test_scaled_df

def scaler_num(X_num_train, X_num_test):
    scaler = MinMaxScaler()
    scaler.fit(X_num_train)
    X_num_train_scaled = scaler.transform(X_num_train)
    X_num_test_scaled = scaler.transform(X_num_test)
    X_num_train_scaled_df = pd.DataFrame(X_num_train_scaled)
    X_num_test_scaled_df = pd.DataFrame(X_num_test_scaled)
    return X_num_train_scaled_df, X_num_test_scaled_df


def scaler_X(X,y):
    print("""
    return X_train_prep_df, X_test_prep_df, y_train_2, y_test_2
    """)
    X_train_2,X_test_2, y_train_2, y_test_2 = train_test_split(X, y, test_size=0.3, random_state=60)

    X_cat_train = X_train_2.select_dtypes(include=['category'])
    X_cat_test = X_test_2.select_dtypes(include=['category'])
    X_cat_train_scaled_df, X_cat_test_scaled_df = scaler_cat(X_cat_train,X_cat_test)

    X_num_train = X_train_2.select_dtypes(include=['float64','int64'])
    X_num_test = X_test_2.select_dtypes(include=['float64','int64'])
    X_num_train_scaled_df,  X_num_test_scaled_df = scaler_num(X_num_train, X_num_test)

    X_train_prep_df = pd.concat([X_cat_train_scaled_df, X_num_train_scaled_df], axis=1)
    X_test_prep_df = pd.concat([X_cat_test_scaled_df, X_num_test_scaled_df], axis=1)

    return X_train_prep_df, X_test_prep_df, y_train_2, y_test_2

def scaler_X_bis(X,y, split = False):
    print("""
    return X_scaled
    """)
    ohe = OneHotEncoder(sparse=False)
    X_cat = X.select_dtypes(include=['category','object'])
    ohe.fit(X_cat)
    X_cat_scaled = ohe.transform(X_cat)
    scaler = MinMaxScaler()
    X_num = X.select_dtypes(include=['float64','int64'])
    scaler.fit(X_num)
    X_num_scaled = scaler.transform(X_num)
    df_cat = pd.DataFrame(X_cat_scaled,columns= [f"cat_{e}" for e in pd.DataFrame(X_cat_scaled).columns])
    df_num = pd.DataFrame(X_num_scaled, columns= [f"num_{e}" for e in pd.DataFrame(X_num_scaled).columns])
    X_scaled = pd.concat([df_cat, df_num], axis=1)
    return X_scaled

# def scaler_cat(features_cat):
#     ohe = OneHotEncoder(sparse=False)
#     features_cat_scaled = ohe.fit_transform(features_cat)
#     features_cat_scaled_df = pd.DataFrame(features_cat_scaled)
#     return features_cat_scaled_df

# def scaler_num(features_num):
#     scaler = MinMaxScaler()
#     scaler.fit(features_num)
#     features_num_scaled = scaler.transform(features_num)
#     features_num_scaled_df = pd.DataFrame(features_num_scaled)
#     return features_num_scaled_df


# def scaler_features(features):
#     features_cat = features.select_dtypes(include=['category'])
#     features_cat_scaled_df = scaler_cat(features_cat)

#     features_num = features.select_dtypes(include=['float64','int64'])
#     features_num_scaled_df = scaler_num(features_num)

#     features_prep_df = pd.concat([features_cat_scaled_df, features_num_scaled_df], axis=1)
#     return features_prep_df
