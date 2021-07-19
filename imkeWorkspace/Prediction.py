import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression
import datetime

df = pd.read_csv("chicago_2016.csv", parse_dates=["start_time","end_time"])

# hinzufügen des Monats
df['month']= df["start_time"].apply(lambda x: x.month)

df = df[df['month'] == 5]

df.to_csv("may_data.csv")

