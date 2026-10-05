from tools import (
    get_financial_data,
    calculate_profit,
    calculate_profit_margin,
    calculate_growth,
    compare_months
)


print("\n--- March Financial Data ---")
print(get_financial_data("March"))


print("\n--- March Profit ---")
print(calculate_profit(1500000, 800000))


print("\n--- March Profit Margin ---")
print(calculate_profit_margin(1500000, 800000))


print("\n--- January to March Growth ---")
print(calculate_growth(1000000, 1500000))


print("\n--- January vs March ---")
print(compare_months("January", "March"))