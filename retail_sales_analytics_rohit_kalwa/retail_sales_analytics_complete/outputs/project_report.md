# Retail Sales Analysis — Project Report

**Prepared by:** Rohit Kalwa  
**Project:** Student portfolio / practice project  
**Period covered:** January–December 2025 (simulated data)

## 1. About the project

For this project, I practised cleaning a retail sales dataset and using Python to answer some basic business questions. I first checked the data, handled a few quality issues, calculated sales and profit measures, and then made charts to compare the results.

**Dataset note:** All records in this project are synthetic practice data. They do not describe a real company, shop, or customer.

## 2. Questions I wanted to answer

- What are the total sales and profit?
- What is the overall profit margin?
- Which month had the highest and lowest sales?
- Which product category, region, and product had the highest sales?
- What data-quality issues needed attention?

## 3. Cleaning the data

- Rows in the original file: **1,208**
- Exact duplicate rows found and removed: **7**
- Rows after removing duplicates: **1,200**
- Rows left after checking required fields: **1,194**
- Extra spaces were removed from text fields and region names were standardised.
- The order date and numeric columns were converted to suitable data types.
- Sales were recalculated using quantity, unit price, and discount. Cost and profit were recalculated as well.
- Missing discount values were treated as 0% for this exercise.

I used these rules to practise a repeatable cleaning workflow. For an actual business dataset, I would confirm the treatment of missing values with the data owner before removing or changing records.

## 4. Main results

| Measure | Result |
|---|---:|
| Total sales | ₹11,701,473.61 |
| Total profit | ₹3,870,628.16 |
| Unique orders | 1,194 |
| Units sold | 5,339 |
| Average order value | ₹9,800.23 |
| Profit margin | 33.08% |

These figures are calculated from the simulated dataset and are only for demonstrating the analysis.

## 5. What I noticed

- **Category:** Furniture had the highest sales, at ₹5,805,160.75.
- **Region:** North had the highest sales, at ₹3,361,349.94, and the highest profit, at ₹1,134,855.70.
- **Product:** Monitor had the highest sales, at ₹3,266,535.46.
- **Month:** August 2025 had the highest sales, at ₹1,151,082.34. November 2025 had the lowest, at ₹701,882.60.

These are patterns in the practice data. They do not explain why the differences happened, so I would need more information before making a real business decision.

## 6. Possible next steps

1. Check whether the best-selling products are consistently available in stock.
2. Compare profit margins as well as sales before suggesting discounts or promotions.
3. Look at promotions, holidays, stock availability, and other details to understand monthly changes.
4. Add a regular check for duplicate rows, missing values, and inconsistent labels.

These are ideas to investigate, not proven recommendations for a real company.

## 7. Tools and skills practised

- Python and Pandas for data cleaning and analysis
- Grouping and summarising data with `groupby`
- Basic business measures such as sales, profit, and margin
- Matplotlib charts and a Plotly interactive dashboard
- Writing down assumptions and explaining results clearly

## 8. Limitations

- The dataset is synthetic and does not support real-world business conclusions.
- Shipping, tax, returns, and overhead costs are not included.
- Profit here is based on the dataset's unit-cost field; it is not a full accounting profit calculation.
- Results depend on the cleaning rules described above.

## 9. How to reproduce the analysis

Install the packages from `requirements.txt` and run `python analyze_sales.py`. The script regenerates the cleaned dataset, KPI tables, charts, and interactive dashboard when the required packages are installed.
