import pandas as pd
import plotly.express as px
import panel as pn
pn.extension()


data = {
    "Month": [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ],
    "Sales": [120, 130, 115, 140, 160, 170, 150, 155, 165, 180, 175, 190],
    "Website Visits": [1500, 1450, 1600, 1550, 1700, 1650, 1800, 1750, 1600, 1850, 1900, 1950],
    "Conversion Rate (%)": [8.0, 9.1, 7.2, 8.6, 9.4, 10.2, 9.3, 9.0, 8.5, 9.7, 9.2, 10.1],
    "Customer Satisfaction": [7.8, 8.0, 7.6, 8.3, 8.7, 8.9, 8.4, 8.1, 8.0, 8.5, 8.8, 9.0]
}

df = pd.DataFrame(data)
df.head()


# Sales Trend Over Months
fig_sales = px.line(df, x="Month", 
                    y="Sales", 
                    title="Monthly Sales")

# Website Visits vs. Conversion Rate
fig_conversion = px.scatter(
    df, x="Website Visits", 
    y="Conversion Rate (%)", 
    size= "Sales",
    title="Website Visits and Conversion Rate"
)

# Customer Satisfaction Over Months
fig_satisfaction = px.bar(df, x="Month", 
                          y="Customer Satisfaction",
                         
                          title="Customer Satisfaction Score")
# E-Commerce Performance Dashboard
dashboard = pn.Column(
    
    pn.Row(fig_sales, fig_satisfaction),
    pn.Row(fig_conversion)
)

#display the dashboard
dashboard.show()
