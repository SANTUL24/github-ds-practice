import pandas as pd

from preprocessing import handle_missing_values


def test_handle_missing_values():
    df = pd.DataFrame({
        "income": [10000, None, 30000],
        "age": [25, 30, None]
    })

    result = handle_missing_values(df)

    assert result["income"].isna().sum() == 0
    assert result["age"].isna().sum() == 0
