import yfinance as yf
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime



def clearlines():
    clearlines = "\n" * 100
    print(clearlines)


root = tk.Tk()
root.geometry("600x200")
root.title("random viewer hahahaa unless")

def getInput():
    userinput = entry.get()
    userinput.upper()
    return userinput

def showstockdata():
    root.title("STOCK VIEW")
    root.geometry("1920x1800")
    ticker = getInput()

    try:
        # Fetch stock data for the entered ticker
        stockData = yf.download(ticker, start="2023-12-1", end="2024-12-7")

        # Clear previous labels
        for widget in root.winfo_children():
            if isinstance(widget, tk.Label) and widget != label_prompt:
                widget.destroy()

        if not stockData.empty:
            # Display the first 5 rows of the stock data
            datalabel = tk.Label(root, text=stockData.head())
            datalabel.pack(pady=35)

            # plot time augbaugbwa
            figure = plt.Figure(figsize=(10, 5), dpi=100)
            ax = figure.add_subplot(111)
            ax.set_title(f"Stock Prices for {ticker}", fontsize=15)

            stockData['Close'].plot(kind='line', legend=True, ax=ax, color='r', marker='o', fontsize=10)


            # create a canvas
            canvas = FigureCanvasTkAgg(figure, root)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)











        else:
            datalabel = tk.Label(root, text="No data found for the specified entry.")
            datalabel.pack(pady=40)



    except Exception as e:
        # Handle any error (e.g., invalid ticker symbol)
        datalabel = tk.Label(root, text=f"Error fetching data: {e}")
        datalabel.pack(pady=40)

entry = tk.Entry(root, width=30)
entry.pack(pady=30)

submitbutton = tk.Button(
    root,
    text="SUBMIT",
    command=showstockdata
)

submitbutton.pack(pady=10)

label_prompt = tk.Label(root, text="Enter a stock ticker symbol:")
label_prompt.pack(pady=5)

root.mainloop()
