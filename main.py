import pandas as pd

import sklearn
print(sklearn.__version__)



df = pd.read_csv('fake-reviews-dataset.csv')

print(df.head())


print(df.info())
print(df.describe())

print(df.isnull().sum())
print(df['label'].value_counts())

import nltk

# Scarica il tokenizzatore 'punkt' e altre risorse utili
nltk.download('punkt')
nltk.download('stopwords')

