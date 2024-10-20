import pandas as pd

# df = pd.read_csv('athlete_events1.csv')
# region_df = pd.read_csv('noc_regions1.csv')

def preprocess(region_df, df):
    # global df,region_df
    # filtering for summer olympics
    df = df[df['Season'] == 'Summer']
    # merge with region_df
    df = df.merge(region_df, on='NOC', how='left')
    # dropping duplicates
    df.drop_duplicates(inplace=True)
    # one hot encoding medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df