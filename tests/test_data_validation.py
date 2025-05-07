import pandas as pd

def test_no_missing_critical_columns(df):
    """
    Check that required columns are not missing.
    """
    required_columns = ['DATERECEIVED', 'DECISIONDATE', 'PRODUCTCODE', 'DECISION_DAYS']
    for col in required_columns:
        assert col in df.columns, f"Missing required column: {col}"

def test_decision_days_non_negative(df):
    """
    Check that all decision days are zero or positive.
    """
    assert (df['DECISION_DAYS'] >= 0).all(), "Negative decision days found"

def test_no_null_product_codes(df):
    """
    Ensure no null values in product codes for analysis.
    """
    assert df['PRODUCTCODE'].notnull().all(), "Null PRODUCTCODE entries found"

# Optional: Example test runner for interactive testing
if __name__ == "__main__":
    df = pd.read_csv("data/Basecamp_combined_cleansed.csv", parse_dates=["DATERECEIVED", "DECISIONDATE"], index_col="KNUMBER")
    from scripts.data_processing import calculate_decision_days
    df = calculate_decision_days(df)

    test_no_missing_critical_columns(df)
    test_decision_days_non_negative(df)
    test_no_null_product_codes(df)
    print("✅ All tests passed.")
