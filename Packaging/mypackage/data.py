import pandas as pd
import os

class Data() :

    def __init__(self, csv= '/root/.pyenv/versions/3.8.12/envs/simplon/lib/python3.8/site-packages/akinator/akinator.csv'):
        self.csv = csv

    def get_data(self) :
        return pd.read_csv(self.csv)
