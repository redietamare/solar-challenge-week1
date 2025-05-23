# src/eda_utils.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import zscore

def plot_time_series(df, cols, time_col="Timestamp"):
    df = df.set_index(time_col)
    df[cols].plot(subplots=True, figsize=(14, 8))
    plt.tight_layout()
    plt.show()

def plot_cleaning_effect(df):
    df.groupby("Cleaning")[["ModA", "ModB"]].mean().plot(kind='bar')
    plt.ylabel("Irradiance (W/m²)")
    plt.title("Cleaning Impact on ModA & ModB")
    plt.show()

def plot_correlation_heatmap(df, cols):
    corr = df[cols].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()

def plot_scatter(df, x, y, title=""):
    sns.scatterplot(data=df, x=x, y=y)
    plt.title(title)
    plt.show()

def plot_histogram(df, col):
    df[col].hist(bins=30, edgecolor='black')
    plt.title(f"Histogram of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()

def plot_bubble_chart(df, x, y, size_col):
    plt.figure(figsize=(8, 6))
    plt.scatter(df[x], df[y], s=df[size_col]*2, alpha=0.5, edgecolor='k')
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f"{x} vs {y} (Bubble size: {size_col})")
    plt.grid(True)
    plt.show()

def detect_outliers(df, cols):
    z_scores = df[cols].apply(zscore)
    outliers = (abs(z_scores) > 3)
    return outliers.sum()
