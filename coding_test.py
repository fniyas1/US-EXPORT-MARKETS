import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd

# read in data and see its info
data = pd.read_excel("Coding Test.xlsx", sheet_name=1, header=None)
print(data.head())

# seperate soybeans data from 'Oct'
soybeans = pd.read_excel("Coding Test.xlsx", sheet_name=1, skiprows=5, nrows=10, header=None)
soybeans.columns = ["Country", "2024", "2025"]
print(soybeans)

# soybeans horizontal bar chart
plt.figure(figsize=(10,7))
plot1 = soybeans.plot(kind='barh', x="Country", stacked=True, width=0.3)
plt.xlabel("Metric Tons") 
plot1.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:,.0f}")) # formatting numbers
plot1.legend(loc="lower center", bbox_to_anchor=(0.5, -0.25), ncol=2,handlelength=1, handleheight=1)
plt.box(False)
plt.grid(axis='x', linestyle='-', alpha=0.7)
plt.title("U.S. Soybean Exports 2024 vs 2025", pad=20)
plt.tight_layout()

fig1 = plt.gcf() 

# seperate corn data from 'Oct'
corn = pd.read_excel("Coding Test.xlsx", sheet_name=1, skiprows=17, nrows=10, header=None)
corn.columns = ["Country", "2024", "2025"]
print(corn)

# corn bar chart
plt.figure(figsize=(10,7))
plot2 = corn.plot(kind='bar', x="Country", width=0.5)
plt.xticks(rotation=45, ha='right')
plt.ylabel("Metric Tons")
plt.xlabel("")
plt.ylim(0, 25000000)
plot2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))
plot2.legend(loc="lower center", bbox_to_anchor=(0.5, -0.39), ncol=2, handlelength=1, handleheight=1)
plt.box(False)
plt.grid(axis='y', linestyle='-', alpha=0.7)
plt.title("U.S. Corn Exports 2024 vs 2025", pad=20)
plt.tight_layout()
fig2 = plt.gcf()

# seperate wheat data from 'Oct'
wheat = pd.read_excel("Coding Test.xlsx", sheet_name=1, skiprows=29, nrows=11, header=None)
wheat.columns = ["Country", "2024", "2025"]
print(wheat)

# wheat line chart
wheat_t = wheat.set_index("Country").T  # flips rows and columns

plt.figure(figsize=(10,7))
wheat_t.plot(ax=plt.gca())
plt.ylabel("Metric Tons")
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))
plt.legend(loc="lower center", bbox_to_anchor=(0.5, -0.2), ncol=4, handlelength=1, handleheight=1)
plt.xticks([0, 1], ["2024", "2025"])
plt.box(False)
plt.grid(axis='y', linestyle='-', alpha=0.7)
plt.title("U.S. Wheat Exports 2024 vs 2025", pad=20)
plt.tight_layout()

fig3 = plt.gcf()

# seperate soybeans data from 'Nov'
soy_nov = pd.read_excel("Coding Test.xlsx", sheet_name=2, skiprows=5, nrows=10, header=None)
soy_nov.columns = ["Country", "2024"]
print(soy_nov)

# soybeans pie chart
plt.figure(figsize=(10,7))
plt.pie(soy_nov["2024"], autopct="%1.1f%%", pctdistance=1.1)
plt.title("U.S. Soybean Exports 2024")
plt.legend(soy_nov["Country"], loc="lower center", bbox_to_anchor=(0.5, -0.20), ncol=3)
plt.tight_layout()

fig4 = plt.gcf()

# seperate corn data from 'Nov'
corn_nov = pd.read_excel("Coding Test.xlsx", sheet_name=2, skiprows=17, nrows=10, header=None)
corn_nov.columns = ["Country", "2024"]
print(corn_nov)

# corn horizontal bar chart
plt.figure(figsize=(10,7))
corn_nov.plot(kind="barh", x="Country", legend=False, width=0.3)
plt.xlabel("Metric Tons")
plt.gca().xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))
plt.box(False)
plt.grid(axis='x', linestyle='-', alpha=0.7)
plt.title("U.S. Corn Exports 2024", pad=20)
plt.tight_layout()

fig5 = plt.gcf()

# seperate wheat data from 'Nov'
wheat_nov = pd.read_excel("Coding Test.xlsx", sheet_name=2, skiprows=29, nrows=10, header=None)
wheat_nov.columns = ["Country", "2024"]
print(wheat_nov)

# wheat area chart
plt.figure(figsize=(10,7))
wheat_nov.plot(kind="area", x="Country", legend=False)
plt.ylabel("Metric Tons")
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))
plt.xticks(range(len(wheat_nov["Country"])), wheat_nov["Country"], rotation=45, ha="right")
plt.box(False)
plt.grid(axis='y', linestyle='-', alpha=0.7)
plt.ylim(0, 4000000)
plt.title("U.S. Wheat Exports 2024", pad=20)
plt.tight_layout()

fig6 = plt.gcf()

# tkinter for generating chart in tabs
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title("U.S. Export Markets")


tabs = ttk.Notebook(root)
tabs.pack(expand=1, fill='both')

def add_chart(fig, title):
    frame = ttk.Frame(tabs, width=900, height=700)
    frame.pack_propagate(False) 
    tabs.add(frame, text=title)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=1, fill="both")


add_chart(fig1, "Soybeans Oct")
add_chart(fig2, "Corn Oct")
add_chart(fig3, "Wheat Oct")
add_chart(fig4, "Soybeans Nov")
add_chart(fig5, "Corn Nov")
add_chart(fig6, "Wheat Nov")

root.update()
for tab in tabs.tabs():
    tabs.select(tab)
    root.update()

tabs.select(0)  # go back to first tab
root.geometry("1000x800")
root.mainloop()
