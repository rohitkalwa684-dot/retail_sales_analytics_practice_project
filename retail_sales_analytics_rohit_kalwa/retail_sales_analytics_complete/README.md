# Retail Sales Analysis Project

**Student:** Rohit Kalwa  
**Project type:** Personal learning / portfolio project  
**Tools used:** Python, Pandas, Matplotlib and Plotly

## Why I made this project

I wanted to practise working with a dataset that was not perfectly clean and learn how to turn it into useful information. In this project, I clean the data, calculate a few sales and profit measures, and make charts to understand the results.

**Please note:** The dataset is simulated for practice. It is not taken from a real shop or client, so the results should not be treated as real business results.

## Questions I explored

- What are the overall sales and profit in the dataset?
- How do sales change from month to month?
- Which categories and regions have the highest sales?
- Which products contribute the most sales?
- What problems should be checked before analysing a dataset?

## Files in this project

- `retail_sales_raw.csv` — the original practice dataset, including some data-quality issues
- `retail_sales_clean_reference.csv` — reference version for checking the cleaning work
- `analyze_sales.py` — the Python script used for cleaning and analysis
- `requirements.txt` — Python packages needed to run the project
- `outputs/` — cleaned data, summary tables, charts, and the interactive dashboard
- `PROJECT_REPORT.md` — a written summary of the work and findings

## How to run it

1. Install Python if it is not already installed.
2. Open a terminal in this project folder.
3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the analysis:

   ```bash
   python analyze_sales.py
   ```

5. Open `outputs/interactive_dashboard.html` in a web browser to explore the charts.

## What I learned

- How to inspect a dataset and find duplicate or missing values
- How to standardise text and convert columns to suitable data types
- How to use Pandas `groupby` to compare months, categories, regions, and products
- How to calculate sales, costs, profit, and profit margin
- How to present results using charts and a simple interactive dashboard

## A few things to keep in mind

Some records are removed when important fields are missing, and missing discounts are treated as zero. Those are assumptions for this practice project; a real business should confirm how missing information should be handled before analysis. The profit calculation also does not include overheads, shipping, taxes, or returns.

This is a learning project. I would like to improve it further by adding more checks and trying the same workflow on a public real-world dataset.
