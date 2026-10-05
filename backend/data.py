import pandas as pd
from pathlib import Path


DATA_PATH = Path(__file__).parent.parent / "data" / "financial_data.csv"

df = pd.read_csv(DATA_PATH)


def get_month_data(month: str):
    """Get financial data for a specific month."""

    result = df[df["month"].str.lower() == month.lower()]

    if result.empty:
        return None

    return result.iloc[0].to_dict()


def get_all_data():
    """Get all available financial data."""

    return df.to_dict(orient="records")