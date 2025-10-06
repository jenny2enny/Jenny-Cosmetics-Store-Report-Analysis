# 📊 Jenny Cosmetics Store Analysis

## 📝 Project Overview
This project presents a comprehensive analysis of sales data from Jenny Cosmetics, a multinational cosmetics retailer. The dataset includes transaction records from various countries, detailing sales personnel, product categories, shipment volumes, and revenue figures. The goal is to uncover insights into sales performance, product popularity, and market trends.

## 📂 Dataset Description
- **Source**: `cosmetics.csv`
- **Records**: 374 transactions
- **Fields**:
  - `Sales Person`: Name of the salesperson
  - `Country`: Country of transaction
  - `Product`: Cosmetic product sold
  - `Date`: Date of sale
  - `Amount ($)`: Revenue generated
  - `Boxes Shipped`: Quantity shipped

## 🧼 Data Cleaning
- Verified no missing or null values
- Confirmed no duplicate records
- Converted `Date` column to datetime format for time-based analysis

## 📊 Exploratory Data Analysis (EDA)

### 📈 Descriptive Statistics
- **Average Sale Amount**: $7,778.35  
- **Average Boxes Shipped**: 249  
- **Sales Period**: January to August 2022

### 🌍 Country-wise Sales
Top-performing countries by revenue:

| Country       | Total Sales ($) |
|---------------|------------------|
| USA           | 628,487.86       |
| New Zealand   | 557,059.85       |
| Australia     | 505,497.64       |
| UK            | 497,061.54       |
| Canada        | 374,562.31       |
| India         | 346,434.92       |

### 👥 Salesperson Performance
Top 3 salespeople by revenue:

| Sales Person     | Total Sales ($) | Boxes Shipped |
|------------------|------------------|----------------|
| Olivia D'Souza   | 387,405.91       | 12,619         |
| Sophia Nair      | 319,887.82       | 10,473         |
| Isabella Roy     | 302,087.60       | 9,116          |

### 🗓️ Monthly Trends
Sales peaked in:

| Month    | Total Sales ($) |
|----------|------------------|
| March    | 484,101.59       |
| April    | 452,650.04       |
| May      | 396,609.09       |

### 🧴 Top Products by Country

| Country     | Top Product           | Sales ($)     |
|-------------|------------------------|----------------|
| USA         | Anti-Aging Serum       | 113,821.81     |
| Australia   | Hair Repair Oil        | 91,002.87      |
| UK          | Hydrating Face Serum   | 75,719.24      |
| New Zealand | SPF 50 Sunscreen       | 87,897.03      |
| Canada      | Under Eye Cream        | 59,336.49      |
| India       | Anti-Aging Serum       | 39,111.02      |

## 📌 Key Performance Indicators (KPIs)

| KPI                    | Value        |
|------------------------|--------------|
| Total Sales            | $2,909,104.12 |
| Total Boxes Shipped    | 93,153        |
| Unique Products Sold   | 15            |
| Total Countries        | 6             |
| Total Sales Persons    | 10            |

## 🧰 Tools & Libraries Used
- Python
- Pandas
- NumPy
- Seaborn
- Matplotlib

## 📁 Folder Structure
