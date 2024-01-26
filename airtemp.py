import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load the data, skipping the first 9 rows
data = pd.read_csv('data.csv', skiprows=9, names=['Month', 'Air Temperature'])

# Convert 'Date' column to datetime format (ignoring time)
data['Month'] = pd.to_datetime(data['Month'].str.split(' ').str[0], format='%d-%m-%Y')

# Set 'Date' column as index
data.set_index('Month', inplace=True)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(data['Air Temperature'], label='Air Temperature', color='red')

# Format the x-axis to show Month and Year
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gcf().autofmt_xdate()  # Rotation

plt.xlabel('Month')
plt.ylabel('Temperature(°C)')
plt.title('Air Temperature Data', fontsize=20)
plt.grid()
plt.legend()
plt.show()
]
