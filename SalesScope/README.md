# Sales Data Analyzer

A small beginner-friendly desktop app that reads sales data from a CSV file, analyzes it, and shows the results in a simple Tkinter dashboard.

Practice flow: **CSV → Pandas → NumPy → Analysis → Matplotlib → Tkinter Dashboard**

## Features

- KPI cards: Total Sales, Orders, Quantity Sold, Best Product, Average Order Value
- Filters: Product, Region and an optional date range (`YYYY-MM-DD`), with **Analyze** and **Reset** buttons
- Charts: Sales by Product (bar), Sales by Region (bar), Monthly Sales (line)
- Analysis tables: product, region, monthly (with % change) and Top 5 products
- Auto-generated **Insights** written in plain English
- Sales data table showing every record that matches the filters
- Handles missing/invalid CSV values, empty filter results and bad dates without crashing

## Technologies Used

- Python 3.8+
- Pandas (loading, filtering, grouping, sorting)
- NumPy (sum, mean, median, min, max, standard deviation, % change)
- Matplotlib (charts, embedded in the window)
- Tkinter (GUI, included with Python)
- CSV (data storage)

## Project Structure

```
sales_data_analyzer/
├── main.py          # data functions, chart functions and the Tkinter GUI
├── sales_data.csv   # sample data (Apr-Sep 2026)
└── README.md
```

## Installation

1. Install Python 3.8 or newer.
2. Install the libraries:

```
pip install pandas numpy matplotlib
```

Tkinter comes with Python on Windows and macOS. On Linux you may need: `sudo apt install python3-tk`

## How to Run

```
python main.py
```

Keep `sales_data.csv` in the same folder as `main.py`.

## Example Functionality

- Choose **Product = Laptop** and **Region = North**, then click **Analyze**. The KPIs, charts, insights and tables all update.
- Type `2026-06-01` in **From** and `2026-08-31` in **To** to study just the summer months.
- Click **Reset** to go back to the full dataset.
- Example insights:
  - Electronics generated 74% of total revenue.
  - North region had the highest sales.
  - Sales decreased by 18.5% in Sep 2026 compared with Aug 2026.

"Best-selling product" means the product with the highest total sales (revenue).

To use your own data, replace `sales_data.csv` with a file that has the columns
`Date,Product,Category,Quantity,Price,Region` (dates as `YYYY-MM-DD`).

## Future Improvements

- Category filter and a category chart
- Export the filtered data or charts to CSV / PNG
- Pick the CSV file from the window (File → Open)
- Pie chart for category share
- Simple unit tests for the analysis functions
