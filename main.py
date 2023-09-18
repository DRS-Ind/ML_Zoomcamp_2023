import pandas as pd


def main():
    df = pd.read_csv('csv_file_for_01.csv')

    # Q1
    print(f'\nPandas`s version: {pd.__version__}')

    # Q2
    print(f'\nNumber of columns: {len(df.columns)}')

    # Q3
    print(f'\nIf missing data True, else False:')
    print(df.isnull().any())

    # Q4
    print(f'\nNumber of unique values: {df["ocean_proximity"].nunique()}')

    # Q5
    df2 = df[df['ocean_proximity'] == 'NEAR BAY']
    # print(df2.to_string())  # update dataset
    average = df2['median_house_value'].mean()
    print(f'\nAverage value for the houses near the bay: {round(average)}')

    # Q6
    average_total_bedrooms = df['total_bedrooms'].mean()
    print(f'\nBefore update mean value: {average_total_bedrooms}')
    new_df = df['total_bedrooms'].fillna(0)
    new_average_total_bedrooms = new_df.mean()
    print(f'After update mean value: {new_average_total_bedrooms}')
    print(f'Has the mean value changed: {["Yes" if average_total_bedrooms != new_average_total_bedrooms else "No"][0]}')

    # Q7
    pass


if __name__ == '__main__':
    main()
