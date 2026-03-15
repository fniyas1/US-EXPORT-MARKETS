# US-EXPORT-MARKETS
# Data Visualizations

Python data visualization of the top 10 U.S. agricultural export markets for soybeans, corn, and wheat using pandas, matplotlib, and tkinter.

## Requirements to Run Code

In python, install the required libraries by running this in your terminal:

```
pip install pandas matplotlib openpyxl
```

## To Run

1. Make sure `coding_test.py` and `Coding Test.xlsx` are in the same folder
2. Open your terminal and navigate to that folder
3. Run the following command:
```
python coding_test.py
```
4. A window will open with tabs for Oct and Nov, each containing three charts for soybeans, corn, and wheat

## Assumptions & Decisions

- The Excel file contains two sheets with data: **Oct** (January–October) and **Nov** (January–November)
- Each sheet has three separate datasets (Soybeans, Corn, Wheat). Specific row ranges were selected for each commodity using `skiprows` to skip blank rows and section headers
- The Nov sheet only contains data for 2024, while the Oct sheet contains both 2024 and 2025 for year comparison
- Visualization titles were made more descriptive for context
- X and Y axis labels were added to indicate unit of measurement (Metric Tons)
- Percentages were added to the Soybeans pie chart (Nov) for easier readability of market share
