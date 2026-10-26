import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

FILE_NAME = "sales_data.csv"

def load_data():
    data = pd.read_csv(FILE_NAME)
    data["Date"] = pd.to_datetime(data["Date"])
    data["Total_Sales"] = data["Quantity"] * data["Price"]
    return data

def show_sales_chart(data, chart_frame):
    for widget in chart_frame.winfo_children():
        widget.destroy()

    sales = data.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)

    figure, ax = plt.subplots(figsize=(7, 4))
    sales.plot(kind="bar", ax=ax, color="skyblue")
    ax.set_title("Sales by Product")
    ax.set_xlabel("Product")
    ax.set_ylabel("Total Sales")
    figure.tight_layout()

    canvas = FigureCanvasTkAgg(figure, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)
    plt.close(figure)

def analyze_sales():
    try:
        product = product_box.get()
        region = region_box.get()
        data = all_data.copy()

        if product != "All":
            data = data[data["Product"] == product]

        if region != "All":
            data = data[data["Region"] == region]

        if data.empty:
            messagebox.showinfo("Sales Analysis", "No sales records found.")
            return

        total_sales = data["Total_Sales"].sum()
        total_orders = len(data)
        total_quantity = data["Quantity"].sum()
        best_product = data.groupby("Product")["Total_Sales"].sum().idxmax()

        total_label.config(text=f"Total Sales: ₹{total_sales:,.2f}")
        orders_label.config(text=f"Total Orders: {total_orders}")
        quantity_label.config(text=f"Quantity Sold: {total_quantity}")
        best_label.config(text=f"Best Product: {best_product}")

        show_sales_chart(data, chart_frame)

        table.delete(*table.get_children())
        for _, row in data.iterrows():
            table.insert("", "end", values=(
                row["Date"].strftime("%Y-%m-%d"),
                row["Product"],
                row["Region"],
                int(row["Quantity"]),
                f"₹{row['Price']:,.2f}",
                f"₹{row['Total_Sales']:,.2f}"
            ))

    except Exception as error:
        messagebox.showerror("Error", f"Could not analyze sales data.\n{error}")

def reset_filters():
    product_box.set("All")
    region_box.set("All")
    analyze_sales()

try:
    all_data = load_data()
except Exception as error:
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("File Error", f"Could not load {FILE_NAME}.\n{error}")
    root.destroy()
    raise SystemExit

root = tk.Tk()
root.title("SalesScope - Simple Sales Analyzer")
root.geometry("900x700")

heading = tk.Label(root, text="SalesScope", font=("Arial", 18, "bold"),
                   bg="#2c3e50", fg="white", pady=10)
heading.pack(fill="x")

filters = ttk.Frame(root, padding=10)
filters.pack(fill="x")

ttk.Label(filters, text="Product:").pack(side="left")
product_box = ttk.Combobox(
    filters, state="readonly",
    values=["All"] + sorted(all_data["Product"].dropna().unique().tolist()),
    width=15
)
product_box.set("All")
product_box.pack(side="left", padx=5)

ttk.Label(filters, text="Region:").pack(side="left")
region_box = ttk.Combobox(
    filters, state="readonly",
    values=["All"] + sorted(all_data["Region"].dropna().unique().tolist()),
    width=15
)
region_box.set("All")
region_box.pack(side="left", padx=5)

ttk.Button(filters, text="Analyze", command=analyze_sales).pack(side="left", padx=5)
ttk.Button(filters, text="Reset", command=reset_filters).pack(side="left", padx=5)

summary = ttk.Frame(root, padding=10)
summary.pack(fill="x")

total_label = ttk.Label(summary, text="Total Sales: ₹0", font=("Arial", 12, "bold"))
total_label.pack(side="left", padx=10)

orders_label = ttk.Label(summary, text="Total Orders: 0", font=("Arial", 12, "bold"))
orders_label.pack(side="left", padx=10)

quantity_label = ttk.Label(summary, text="Quantity Sold: 0", font=("Arial", 12, "bold"))
quantity_label.pack(side="left", padx=10)

best_label = ttk.Label(summary, text="Best Product: -", font=("Arial", 12, "bold"))
best_label.pack(side="left", padx=10)

chart_frame = ttk.Frame(root, padding=10)
chart_frame.pack(fill="both", expand=True)

columns = ("Date", "Product", "Region", "Quantity", "Price", "Total Sales")
table = ttk.Treeview(root, columns=columns, show="headings", height=8)
for column in columns:
    table.heading(column, text=column)
    table.column(column, width=120, anchor="center")
table.pack(fill="both", expand=True, padx=10, pady=10)

analyze_sales()
root.mainloop()
