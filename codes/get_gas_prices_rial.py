import pandas as pd

# Load USD price in RIAL data
usd_price_df = pd.read_csv('dollar_price.csv', parse_dates=['DateTime'])

# Load gas prices in USD data
gas_price_df = pd.read_csv('Turkey_gasoline_prices.csv', parse_dates=['DateTime'])

# Merge gas prices data with USD price in RIAL data based on the month-year part of the date
gas_price_df['month_year'] = gas_price_df['DateTime'].dt.to_period('M')
usd_price_df['month_year'] = usd_price_df['DateTime'].dt.to_period('M')
merged_df = gas_price_df.merge(usd_price_df, on='month_year', how='left')

# Convert gas prices from USD to RIAL
merged_df['Gas_Price_Rial'] = merged_df['Close_x'] * merged_df['Close_y']

# Drop unnecessary columns
final_df = merged_df[['DateTime_x', 'Gas_Price_Rial']]

# Rename columns
final_df.columns = ['DateTime', 'Gas_Price_Rial']

# Format gas_price_rial column to display 2 decimal places
final_df['Gas_Price_Rial'] = final_df['Gas_Price_Rial'].round(2)

# Remove the day part from DateTime column
final_df['DateTime'] = final_df['DateTime'].dt.strftime('%Y-%m')

# Remove rows with NaN values in the gas prices in RIAL column
final_df = final_df.dropna(subset=['Gas_Price_Rial'])

# Save final dataframe to CSV
final_df.to_csv('turkey_prices_rial.csv', index=False)

# Display final dataframe
print(final_df)
