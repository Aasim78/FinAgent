from typing import Optional
from data import get_month_data, get_all_data


def get_financial_data(month: Optional[str] = None):
    """
    Retrieve financial data for a specific month
    or all available financial data.
    """

    if month:
        data = get_month_data(month)

        if data is None:
            return {
                "error": f"No financial data available for {month}."
            }

        return data

    return get_all_data()


def calculate_profit(revenue: float, expenses: float):
    """Calculate profit."""

    profit = revenue - expenses

    return {
        "revenue": revenue,
        "expenses": expenses,
        "profit": profit
    }


def calculate_profit_margin(revenue: float, expenses: float):
    """Calculate profit margin percentage."""

    if revenue == 0:
        return {
            "error": "Revenue cannot be zero."
        }

    profit = revenue - expenses
    margin = (profit / revenue) * 100

    return {
        "revenue": revenue,
        "expenses": expenses,
        "profit": profit,
        "profit_margin": round(margin, 2)
    }


def calculate_growth(old_value: float, new_value: float):
    """Calculate percentage growth."""

    if old_value == 0:
        return {
            "error": "Original value cannot be zero."
        }

    growth = ((new_value - old_value) / old_value) * 100

    return {
        "old_value": old_value,
        "new_value": new_value,
        "growth_percentage": round(growth, 2)
    }


def compare_months(month1: str, month2: str):
    """Compare financial performance between two months."""

    data1 = get_month_data(month1)
    data2 = get_month_data(month2)

    if data1 is None:
        return {
            "error": f"No data available for {month1}."
        }

    if data2 is None:
        return {
            "error": f"No data available for {month2}."
        }

    revenue_growth = (
        (data2["revenue"] - data1["revenue"])
        / data1["revenue"]
    ) * 100

    expense_growth = (
        (data2["expenses"] - data1["expenses"])
        / data1["expenses"]
    ) * 100

    return {
        "from_month": month1,
        "to_month": month2,
        "revenue_growth": round(revenue_growth, 2),
        "expense_growth": round(expense_growth, 2)
    }

def analyze_financial_performance():
    """
    Analyze financial performance across all available months.
    Calculates profit and profit margin for each month and
    identifies the best-performing months.
    """

    data = get_all_data()

    if not data:
        return {
            "error": "No financial data available."
        }

    monthly_analysis = []

    for row in data:
        revenue = row["revenue"]
        expenses = row["expenses"]

        profit = revenue - expenses

        if revenue != 0:
            profit_margin = (profit / revenue) * 100
        else:
            profit_margin = 0

        monthly_analysis.append({
            "month": row["month"],
            "revenue": revenue,
            "expenses": expenses,
            "profit": profit,
            "profit_margin": round(profit_margin, 2)
        })

    highest_revenue = max(
        monthly_analysis,
        key=lambda x: x["revenue"]
    )

    highest_profit = max(
        monthly_analysis,
        key=lambda x: x["profit"]
    )

    highest_margin = max(
        monthly_analysis,
        key=lambda x: x["profit_margin"]
    )

    lowest_profit = min(
        monthly_analysis,
        key=lambda x: x["profit"]
    )

    average_revenue = sum(
        x["revenue"] for x in monthly_analysis
    ) / len(monthly_analysis)

    average_profit = sum(
        x["profit"] for x in monthly_analysis
    ) / len(monthly_analysis)

    return {
        "monthly_analysis": monthly_analysis,
        "highest_revenue_month": highest_revenue,
        "highest_profit_month": highest_profit,
        "highest_profit_margin_month": highest_margin,
        "lowest_profit_month": lowest_profit,
        "average_monthly_revenue": round(average_revenue, 2),
        "average_monthly_profit": round(average_profit, 2)
    }