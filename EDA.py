import pandas as pd

# Load cleaned CSV
df = pd.read_csv("books_cleaned_data.csv")

# Display first 5 rows
print(df.head())

# Basic info
print(df.info())

# Summary statistics
print(df.describe())

# Check missing values
print(df.isnull().sum())

# Check duplicates
print(df.duplicated().sum())

##

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,5))
sns.histplot(df["Price"], bins=25, color="steelblue")

plt.axvline(df["Price"].mean(), color="red", linestyle="--", label="Average Price")
plt.legend()

plt.title("Most Books Are Priced Around the Average (£)")
plt.xlabel("Book Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.show()

###

stock_percent = df["Stock"].value_counts(normalize=True) * 100
stock_percent = stock_percent.rename({1: "In Stock", 0: "Out of Stock"})

plt.figure(figsize=(6,4))
sns.barplot(x=stock_percent.index, y=stock_percent.values)

for i, val in enumerate(stock_percent.values):
    plt.text(i, val + 1, f"{val:.1f}%", ha='center')

plt.title("Most Books Are Available in Stock")
plt.ylabel("Percentage (%)")
plt.xlabel("")
plt.ylim(0, 100)
plt.tight_layout()
plt.show()

top_books = df.sort_values("Price", ascending=False).head(15)

plt.figure(figsize=(12,6))
sns.barplot(y="Title", x="Price", data=top_books)

plt.title("Top 15 Most Expensive Books")
plt.xlabel("Price (£)")
plt.ylabel("")
plt.tight_layout()
plt.show()

###

df["Price Category"] = pd.cut(
    df["Price"],
    bins=[0, 20, 40, df["Price"].max()],
    labels=["Low Price", "Medium Price", "High Price"]
)

price_cat = df["Price Category"].value_counts()

plt.figure(figsize=(6,4))
sns.barplot(x=price_cat.index, y=price_cat.values)

plt.title("Most Books Fall in the Medium Price Range")
plt.ylabel("Number of Books")
plt.xlabel("")
plt.tight_layout()
plt.show()

###
numeric_df = df.select_dtypes(include=["number"])


plt.figure(figsize=(5,4))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    cbar=False
)

plt.title("Price Has Little Effect on Stock Availability")
plt.tight_layout()
plt.show()
