def handle_missing_values(df):
    df = df.copy()

    for column in df.columns:
        if df[column].dtype in ["int64", "float64"]:
            df[column] = df[column].fillna(df[column].median())

    return df
