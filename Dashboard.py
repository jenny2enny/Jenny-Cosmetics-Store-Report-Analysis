# Create from interactive dassboard using streamlit
# import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 

# set app title
st.set_page_config(page_title="Jenny Cosmetics Store Dasboard", layout="wide") 

st.title("Jenny Cosmetics Store Dashboard")

# Load the dataset 
df = pd.read_csv("cosmetics.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month_name()
df['Year'] = df['Date'].dt.year

# Sidebar for filters
df = df.rename(columns={"Amount": "Amount"})
st.sidebar.header("Filters")
Country = st.sidebar.multiselect("Select Country", options=df['Country'].unique(), default=df['Country'].unique())
sales_person = st.sidebar.multiselect("Select Sales Person", options=df['Sales Person'].unique(), default=df['Sales Person'].unique())
product = st.sidebar.multiselect("Select Product", options=df['Product'].unique(), default=df['Product'].unique())

df_filtered = df[(df
                  ['Country'].isin(Country)) &
                  (df['Sales Person'].isin(sales_person)) &
                    (df['Product'].isin(product))
                    ]

#KPIs
kpi1 = df_filtered['Amount'].sum()
kpi2 = df_filtered['Boxes Shipped'].sum()
kpi3 = df_filtered['Product'].nunique()
kpi4 = df_filtered['Country'].nunique()
kpi5 = df_filtered['Sales Person'].nunique()

st.markdown("### Key Performance Indicators")
kpi_cols = st.columns(5)
kpi_cols[0].metric("Total Sales ($)", f"${kpi1:,.2f}")
kpi_cols[1].metric("Total Boxes Shipped", f"{kpi2}")
kpi_cols[2].metric("Unique Products", f"{kpi3}")
kpi_cols[3].metric("Unique Countries",f"{kpi4}") 
kpi_cols[4].metric("Unique Sales Persons",f"{kpi5}")

                   
st.markdown("---")

 #sales performance by sales person
st.subheader("Sales Performance by Sales Person")
perf = df_filtered.groupby('Sales Person')[['Amount', 'Boxes Shipped']].sum().sort_values('Amount', ascending=False)
st.dataframe(perf)
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.bar(perf.index, perf['Amount'], color='skyblue', label='Amount')
ax1.bar(perf.index, perf['Boxes Shipped'], color='lightcoral', bottom=perf['Amount'], label='Boxes Shipped')
plt.xlabel("Sales Person")
plt.ylabel("Total Sales Amount")
plt.title("Sales Performance by Sales Person") 
plt.xticks(rotation=45)
plt.legend()
st.pyplot(fig1)

#Total sales per country
st.subheader("Total Sales per Country")
con = df_filtered.groupby('Country')['Amount'].sum().sort_values(ascending=False)
st.dataframe(con)
fig2, ax2 = plt.subplots(figsize=(10, 6))
plt.bar(con.index, con.values, color='pink',)
plt.title("Total Sales per Country")
plt.xlabel("Country")
plt.ylabel("Total Sales Per Counrty")
plt.xticks(rotation=45)
st.pyplot(fig2) 

#Monthly sales trend 
st.subheader("Monthly Sales Trend")
trend = df_filtered.groupby('Month')['Amount'].sum().sort_values(ascending=False)
st.dataframe(trend)
fig3, ax3 = plt.subplots(figsize=(8,4))
ax3.plot(trend.index, trend.values, marker='o', linestyle='-', color='purple')
plt.xlabel("Month")
plt.ylabel("Total Sales  ($)")
plt.title("Monthly Sales Trend") 
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig3)

# Top products by Country
st.subheader("Top Products by Country")
top_products = df.groupby(['Country', 'Product'])['Amount'].sum().reset_index()
top_products = top_products.sort_values(by=['Country', 'Amount'], ascending=[True,False])
top_products = top_products.groupby('Country').head(1)
st.dataframe(top_products)
fig4, ax4 = plt.subplots(figsize=(5, 5))
ax4.pie(top_products['Amount'], labels=top_products['Product'], autopct= '%1.1f%%', startangle=140)
plt.axis("equal") # equal aspect ratio ensures that pie is drawn as a circle
plt.title("Top selling product by Country(Donut chart)") 
plt.legend(top_products['Country'])
st.pyplot(fig4)


fig5, ax5 = plt.subplots(figsize=(10, 6))
for country in top_products['Country'].unique():
    subset = top_products[top_products['Country'] == country]
    ax5.plot(subset['Product'], subset['Amount'], label=country)
plt.title("top selling product by Country")
plt.xlabel("Product")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45)
plt.legend(title='Country')
plt.tight_layout()
st.pyplot(fig5)

st.markdown("---")
st.markdown("Report generated on:" + pd.Timestamp.now().strftime("%Y-%m-%d"))



