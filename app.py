import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
# We load from our locally saved CSVs instead of hitting the API everytime
# the app runs faster more reliable and doesnt depend on network

#Annual macro indicators(GDP growth, inflation, unmeployment) from world bank
wb_df = pd.read_csv("data/processed/worldbank_indicators.csv")

# Monthly private sector credit growth from CBK
credit_df = pd.read_csv("data/processed/cbk_credit_growth.csv"  )

# Monthly mobile money data( transaction value + registered accounts)
mobile_df = pd.read_csv("data/processed/cbk_mobile_money.csv")


# --- Page config ---
# This sets the browser tab title and makes the layout use the full page width
# instead of the narrow centered column Streamlit defaults to.
st.set_page_config(page_title="Kenya Economic Pulse", layout="wide")

# --- Header ---
st.title("🇰🇪 Kenya Economic Pulse Dashboard")
st.markdown("Tracking Kenya's key macro and financial indicators across time.")

st.divider()

# --- Section 1: Annual Macro Trends (World Bank) ---
st.subheader("Macro Economic Trends (Annual)")

# Let the user pick which indicator(s) they want to see —
# this is what makes it a dashboard rather than just a static chart.
indicators = wb_df["indicator"].unique().tolist()
selected = st.multiselect(
    "Select indicators to display:",
    options=indicators,
    default=indicators  # show all three by default
)

# Filter the dataframe down to only what the user selected.
filtered_wb = wb_df[wb_df["indicator"].isin(selected)]

# Build the line chart — one line per indicator, colored automatically by Plotly.
fig1 = px.line(
    filtered_wb,
    x="year",
    y="value",
    color="indicator",
    title="Kenya Macro Indicators (World Bank)",
    labels={"value": "Value (%)", "year": "Year", "indicator": "Indicator"},
)
st.plotly_chart(fig1, use_container_width=True)

st.divider()

# --- Section 2: Monthly Credit Growth (CBK) ---
st.subheader("Private Sector Credit Growth (Monthly, CBK)")

# Build a period column for proper x-axis display — combining year and month
# into one label like "2015-Jan" gives us a readable time axis without needing
# to convert to full datetime, which would require more complex handling of
# the month name strings.
credit_df["period"] = credit_df["year"].astype(str) + "-" + credit_df["month"]

fig2 = px.line(
    credit_df,
    x="period",
    y="value",
    title="Kenya Private Sector Credit Growth (%)",
    labels={"value": "Credit Growth (%)", "period": "Month"},
)

# Reduce x-axis label clutter — with 135 monthly data points, showing every
# single label would make the x-axis unreadable.
fig2.update_xaxes(nticks=20)

st.plotly_chart(fig2, use_container_width=True)

st.divider()

# --- Section 3: Mobile Money (CBK) ---
st.subheader("Mobile Money Trends (Monthly, CBK)")

# Split the combined mobile_df into two separate charts since the two indicators
# are on completely different scales — transaction value is in KSh billions,
# accounts are in millions of people. Plotting them on the same axis would
# make one line look completely flat next to the other.
mobile_value = mobile_df[mobile_df["indicator"] == "Mobile money transaction value (KSh billions)"].copy()
mobile_accounts = mobile_df[mobile_df["indicator"] == "Registered mobile money accounts (millions)"].copy()

# Build the same period column we used for credit growth.
mobile_value["period"] = mobile_value["year"].astype(str) + "-" + mobile_value["month"]
mobile_accounts["period"] = mobile_accounts["year"].astype(str) + "-" + mobile_accounts["month"]

# Use two columns so both charts sit side by side rather than stacked vertically —
# easier to compare growth trajectories at a glance.
col1, col2 = st.columns(2)

with col1:
    fig3 = px.line(
        mobile_value,
        x="period",
        y="value",
        title="M-Pesa Transaction Value (KSh Billions)",
        labels={"value": "KSh Billions", "period": "Month"},
    )
    fig3.update_xaxes(nticks=10)
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    fig4 = px.line(
        mobile_accounts,
        x="period",
        y="value",
        title="Registered Mobile Money Accounts (Millions)",
        labels={"value": "Accounts (Millions)", "period": "Month"},
    )
    fig4.update_xaxes(nticks=10)
    st.plotly_chart(fig4, use_container_width=True)

    # KPI summary row — gives visitors the most recent numbers at a glance
# before they even look at the charts.
st.subheader("Latest Snapshot")
k1, k2, k3, k4 = st.columns(4)

latest_gdp = wb_df[wb_df["indicator"] == "GDP growth"].sort_values("year").iloc[-1]
latest_inf = wb_df[wb_df["indicator"] == "Inflation"].sort_values("year").iloc[-1]
latest_credit = credit_df.iloc[-1]
latest_mpesa = mobile_value.sort_values("period").iloc[-1]

k1.metric("GDP Growth (Latest)", f"{latest_gdp['value']:.1f}%", f"{latest_gdp['year']}")
k2.metric("Inflation (Latest)", f"{latest_inf['value']:.1f}%", f"{latest_inf['year']}")
k3.metric("Credit Growth (Latest)", f"{latest_credit['value']:.1f}%")
k4.metric("M-Pesa Value (Latest)", f"KSh {latest_mpesa['value']:.0f}B")