# src/data_utils.py

import pandas as pd
import numpy as np

def load_data(path: str, parse_dates=["Timestamp"]) -> pd.DataFrame:
    return pd.read_csv(path, parse_dates=parse_dates)

def clean_columns(df: pd.DataFrame, columns_to_impute: list) -> pd.DataFrame:
    df_copy = df.copy()
    df_copy[columns_to_impute] = df_copy[columns_to_impute].fillna(df_copy[columns_to_impute].median())
    return df_copy

def export_cleaned(df: pd.DataFrame, path: str):
    df.to_csv(path, index=False)

def summarize_missing(df: pd.DataFrame) -> pd.Series:
    return (df.isna().mean() * 100).sort_values(ascending=False)