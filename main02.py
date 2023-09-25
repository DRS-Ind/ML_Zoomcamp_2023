import pandas as pd
from pandas import Series, DataFrame

dataframe = pd.read_csv('csv_file_for_02.csv')


def prepare_and_split_the_dataset(raw_dataframe, split_train, split_val, split_test):
    new_dataframe = raw_dataframe.sample(frac=1, random_state=42)
    pass


def main():
    # Q1
    df = dataframe[dataframe.ocean_proximity.isin(['<1H OCEAN', 'INLAND'])]
    # print(f'\nNumber of columns: {df.columns}')
    columns_with_missing_items = {name: True for name in list(df.columns) if df[name].isnull().any()}
    print(f"Missing values in: {list(columns_with_missing_items.keys())[0]}")

    # Q2
    percentile = df['population'].quantile(q=0.5).mean()
    print(f'\nThe median (50% percentile) for variable \'population\': {percentile}')

    # Q3
    pass


if __name__ == '__main__':
    main()
