import pandas as pd
from sklearn.model_selection import train_test_split

def null_count(df):
    df.isna().sum()
    return

def train_test_split(df, frac):
    train, val = df, train_size=frac, test_size=(frac/1)
    return