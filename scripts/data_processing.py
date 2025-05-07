import pandas as pd

def load_510k_data(file_path):
    """
    Loads FDA 510(k) submission data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Parsed DataFrame with datetime fields and KNUMBER as index.
    """
    df = pd.read_csv(
        file_path,
        parse_dates=["DATERECEIVED", "DECISIONDATE"],
        index_col="KNUMBER",
        low_memory=False
    )
    return df

def calculate_decision_days(df):
    """
    Adds a DECISION_DAYS column to the DataFrame based on date differences.

    Args:
        df (pd.DataFrame): DataFrame containing DATERECEIVED and DECISIONDATE.

    Returns:
        pd.DataFrame: DataFrame with DECISION_DAYS column.
    """
    df = df.copy()
    df['DECISION_DAYS'] = (df['DECISIONDATE'] - df['DATERECEIVED']).dt.days
    return df

def filter_top_product_codes(df, n=10):
    """
    Filters the DataFrame to only include rows from the top N most frequent PRODUCTCODEs.

    Args:
        df (pd.DataFrame): DataFrame with 'PRODUCTCODE' column.
        n (int): Number of top product codes to include.

    Returns:
        pd.DataFrame: Filtered DataFrame with top product codes only.
    """
    top_codes = df['PRODUCTCODE'].value_counts().head(n).index
    return df[df['PRODUCTCODE'].isin(top_codes)]

def summarize_decision_days_by_product_code(df):
    """
    Groups the DataFrame by PRODUCTCODE and summarizes DECISION_DAYS.

    Args:
        df (pd.DataFrame): DataFrame with PRODUCTCODE and DECISION_DAYS.

    Returns:
        pd.DataFrame: Summary statistics grouped by PRODUCTCODE.
    """
    return df.groupby('PRODUCTCODE')['DECISION_DAYS'].describe()
