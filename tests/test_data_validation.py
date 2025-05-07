import pandas as pd
import os

def test_no_missing_critical_columns(df):
    required_columns = ['DATERECEIVED', 'DECISIONDATE', 'PRODUCTCODE', 'DECISION_DAYS']
    for col in required_columns:
        assert col in df.columns, f"Missing required column: {col}"

def test_decision_days_non_negative(df):
    assert (df['DECISION_DAYS'] >= 0).all(), "Negative decision days found"

def test_no_null_product_codes(df):
    assert df['PRODUCTCODE'].notnull().all(), "Null PRODUCTCODE entries found"

if __name__ == "__main__":
    # Use lightweight test dataset
    test_data_path = os.path.join("tests", "data", "sample_510k_test_data.csv")
    df = pd.read_csv(test_data_path, parse_dates=["DATERECEIVED", "DECISIONDATE"], index_col=0)

    test_no_missing_critical_columns(df)
    test_decision_days_non_negative(df)
    test_no_null_product_codes(df)

    print("✅ All sample tests passed.")
