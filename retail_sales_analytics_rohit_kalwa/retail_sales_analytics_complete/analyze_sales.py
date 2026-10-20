from pathlib import Path
import json
import pandas as pd
import matplotlib.pyplot as plt

STUDENT_NAME = "Rohit Kalwa"
ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(ROOT / "retail_sales_raw.csv")
raw_rows = len(df)
duplicate_count = int(df.duplicated().sum())
print(f"Raw rows: {raw_rows}; exact duplicates: {duplicate_count}")
print("Missing values before cleaning:\n", df.isna().sum())

for col in ["region", "category", "product"]:
    df[col] = df[col].astype("string").str.strip()
df["region"] = df["region"].str.title()
df["category"] = df["category"].str.replace(r"\s+", " ", regex=True)
df["product"] = df["product"].str.replace(r"\s+", " ", regex=True)
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

numeric_cols = ["quantity", "unit_price", "discount_pct", "unit_cost", "sales", "cost", "profit"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.drop_duplicates()
essential = ["order_id", "order_date", "region", "category", "product", "quantity", "unit_price", "unit_cost"]
df = df.dropna(subset=essential)
df["discount_pct"] = df["discount_pct"].fillna(0)
df["sales"] = (df["quantity"] * df["unit_price"] * (1 - df["discount_pct"])).round(2)
df["cost"] = (df["quantity"] * df["unit_cost"]).round(2)
df["profit"] = (df["sales"] - df["cost"]).round(2)
df["month"] = df["order_date"].dt.to_period("M").astype(str)
df.to_csv(OUT / "cleaned_sales.csv", index=False)

total_sales, total_profit = float(df.sales.sum()), float(df.profit.sum())
kpis = {
    "total_sales": round(total_sales, 2),
    "total_profit": round(total_profit, 2),
    "unique_orders": int(df.order_id.nunique()),
    "units_sold": int(df.quantity.sum()),
    "average_order_value": round(float(df.groupby("order_id").sales.sum().mean()), 2),
    "profit_margin_pct": round(total_profit / total_sales * 100, 2) if total_sales else 0,
    "raw_rows": raw_rows,
    "exact_duplicate_rows_removed": duplicate_count,
    "cleaned_rows": int(len(df))
}
(OUT / "kpis.json").write_text(json.dumps(kpis, indent=2), encoding="utf-8")
pd.DataFrame([kpis]).to_csv(OUT / "kpis.csv", index=False)

monthly = df.groupby("month", as_index=False).agg(sales=("sales", "sum"), profit=("profit", "sum"))
category = df.groupby("category", as_index=False).agg(sales=("sales", "sum"), profit=("profit", "sum"), units=("quantity", "sum")).sort_values("sales", ascending=False)
region = df.groupby("region", as_index=False).agg(sales=("sales", "sum"), profit=("profit", "sum"), units=("quantity", "sum")).sort_values("sales", ascending=False)
products = df.groupby("product", as_index=False).agg(sales=("sales", "sum"), profit=("profit", "sum"), units=("quantity", "sum")).sort_values("sales", ascending=False)

for name, table in [("monthly_performance", monthly), ("category_performance", category),
                    ("regional_performance", region), ("product_performance", products)]:
    table.to_csv(OUT / f"{name}.csv", index=False)

charts = [
    (monthly["month"], monthly["sales"], "Monthly Sales Trend", "month", "Sales", "line"),
    (category["category"], category["sales"], "Sales by Product Category", "Category", "Sales", "bar"),
    (region["region"], region["profit"], "Profit by Region", "Region", "Profit", "bar"),
    (products.head(8)["product"], products.head(8)["sales"], "Top Products by Sales", "Product", "Sales", "bar")
]
for x, y, title, xlabel, ylabel, kind in charts:
    plt.figure(figsize=(10, 5))
    if kind == "line":
        plt.plot(x, y, marker="o")
    else:
        plt.bar(x, y)
    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel)
    plt.xticks(rotation=25, ha="right"); plt.tight_layout()
    filename = title.lower().replace(" ", "_") + ".png"
    plt.savefig(OUT / filename, dpi=160); plt.close()

# Optional interactive dashboard
try:
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    from plotly.offline import plot
    fig = make_subplots(rows=2, cols=2, subplot_titles=(
        "Monthly Sales", "Sales by Category", "Profit by Region", "Top Products by Sales"
    ))
    fig.add_trace(go.Scatter(x=monthly.month, y=monthly.sales, mode="lines+markers", name="Sales"), row=1, col=1)
    fig.add_trace(go.Bar(x=category.category, y=category.sales, name="Category sales"), row=1, col=2)
    fig.add_trace(go.Bar(x=region.region, y=region.profit, name="Regional profit"), row=2, col=1)
    fig.add_trace(go.Bar(x=products.head(8)["product"], y=products.head(8)["sales"], name="Product sales"), row=2, col=2)
    fig.update_layout(title=f"Retail Sales Analysis | {STUDENT_NAME} | Sales ₹{total_sales:,.0f} | Profit ₹{total_profit:,.0f}",
                      height=820, showlegend=False, template="plotly_white")
    plot(fig, filename=str(OUT / "interactive_dashboard.html"), auto_open=False, include_plotlyjs=True)
except ImportError:
    print("Plotly is not installed; install it with `pip install plotly` for the interactive dashboard.")

print(f"\nRetail Sales Analysis — Student: {STUDENT_NAME}")
print("KPI SUMMARY")
for key, value in kpis.items():
    print(f"{key}: {value}")
print(f"\nOutputs saved to {OUT}")
