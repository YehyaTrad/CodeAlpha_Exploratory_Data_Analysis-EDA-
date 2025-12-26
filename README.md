# 📊 Exploratory Data Analysis (EDA)
## CodeAlpha Data Analytics Internship – Task 2

---

## 📌 Project Overview
This project focuses on **Exploratory Data Analysis (EDA)** as part of the **CodeAlpha Data Analytics Internship**.

The goal of this task is to explore, understand, and analyze a real-world dataset using **statistical techniques and visualizations** in order to uncover patterns, trends, anomalies, and data quality issues.

---

## 🛠️ Tools & Technologies Used
- 🐍 **Python**
- 📊 **Pandas** – Data manipulation and analysis
- 📈 **Matplotlib** – Plotting charts
- 🎨 **Seaborn** – Advanced visualizations
- 🧹 **Regex (re)** – Data cleaning

---

## 📂 Project Structure
```
CodeAlpha_Exploratory_Data_Analysis
├── EDA.py # Exploratory Data Analysis script
├── books_cleaned_data.csv # Cleaned dataset
└── README.md # Project documentation
```


---

## 📑 Dataset Description
The dataset contains **1000 books** with the following features:

| Column | Description |
|------|------------|
| 📘 Title | Name of the book |
| 💰 Price | Book price in GBP (£) |
| 📦 Stock | Availability (1 = In Stock, 0 = Out of Stock) |

The dataset was cleaned prior to analysis to ensure accurate numeric and categorical values.

---

# ❓ Questions Asked Before Analysis (As Required)

✔ What is the overall price distribution of books?  
✔ Are most books cheap, medium-priced, or expensive?  
✔ Are books generally in stock or out of stock?  
✔ Do higher prices affect stock availability?  
✔ Are there any unusual prices or outliers?  

These questions guided the exploratory analysis process.

---

# 🔍 Data Exploration & Preparation
- Inspected dataset structure and data types
- Identified numeric and non-numeric columns
- Removed missing and duplicate values
- Selected numeric features for statistical analysis

Key numeric features:
- **Price**
- **Stock**

---

# 📊 Visualizations & Insights

## 1️⃣ 📈 Price Distribution of Books
**Visualization:** Histogram with average price indicator  

**Insight:**  
Most books are priced in the **£20–£30 range**, with fewer books at higher prices. The distribution is right-skewed due to a small number of expensive books.

---

## 2️⃣ 📦 Stock Availability
**Visualization:** Bar chart showing percentage of books in stock  

**Insight:**  
The majority of books are **in stock**, indicating strong availability across the dataset.

---

## 3️⃣ 💰 Price Outliers
**Visualization:** Boxplot  

**Insight:**  
A small number of books have significantly higher prices than the rest, indicating the presence of price outliers.

---

## 4️⃣ 🏆 Top 15 Most Expensive Books
**Visualization:** Horizontal bar chart with book titles  

**Insight:**  
This visualization highlights the most expensive books, making extreme values easy to identify.

---

## 5️⃣ 🔗 Correlation Between Price & Stock
**Visualization:** Correlation heatmap  

**Insight:**  
There is **little to no correlation** between book price and stock availability, suggesting that price does not strongly influence whether a book is in stock.

---

# 🧪 Hypothesis Testing
**Hypothesis:**  
> Higher-priced books are more likely to be out of stock.

**Result:**  
❌ The hypothesis was rejected. Correlation analysis shows a weak relationship between price and stock availability.

---

# ⚠️ Data Issues Identified
- Non-numeric columns (e.g., book titles) cannot be used in correlation analysis
- Price outliers may affect averages
- Binary stock variable limits deeper statistical modeling

These issues were addressed through proper column selection, cleaning, and robust visualizations.

---

# ▶️ How to Run the Analysis

### 1️⃣ Install required libraries
```bash
pip install pandas matplotlib seaborn
```
### 2️⃣ Run the EDA script
```
python EDA.py
```

# 🎯 Key Takeaways

-Explored dataset structure and data quality

-Identified trends, patterns, and anomalies

-Tested assumptions using statistical analysis

-Created clear, intuitive visualizations


# 👤 Author

Yehya Alaa Trad
Data Analytics Intern – CodeAlpha

🔗 GitHub: https://github.com/YehyaTrad

🔗 LinkedIn: https://www.linkedin.com/in/yehya-trad-690196327?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app

### 📜 License

This project is created for educational and internship purposes only.
