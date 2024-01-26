This code provides a versatile solution for plotting time-series data with different Y-axis labels. By changing the filename and Y-axis label, you can easily generate three distinct graphs from a single codebase. This is particularly useful when dealing with datasets containing diverse variables.

Instructions :

1. Clone the Repository:
[git clone https://github.com/your/repo.git
cd repo ]


2. Prepare Data:
- Ensure that your data is in CSV format.
- Place your data file ('data.csv') in the same directory as the code.


3. Run the Code:
- Execute the code in a Python environment.
- Ensure that you have the required dependencies installed.

4. Generate Graphs:
- You can generate three different graphs by making slight modifications to the code.
- Change the filename and Y-axis label as follows:


Graph 1: Air Temperature
data = pd.read_csv('data.csv', skiprows=9, names=['Month', 'Air Temperature'])
...
plt.plot(data['Air Temperature'], label='Air Temperature', color='red')
...
plt.ylabel('Temperature(°C)')
...
plt.title('Air Temperature Data', fontsize=20)

Graph 2: Monthly Precipitation
data = pd.read_csv('data.csv', skiprows=9, names=['Month', 'mm per Day'])
...
plt.plot(data['mm per Day'], label='mm per Day', color='red')
...
plt.ylabel('mm per Day')
...
plt.title('Monthly Precipitation Data', fontsize=20)
Graph 3: Surface Soil Moisture
data = pd.read_csv('data.csv', skiprows=9, names=['Month', 'kg per metre square'])
...
plt.plot(data['kg per metre square'], label='kg per metre square', color='red')
...
plt.ylabel('kg per metre square')
...
plt.title('Surface Soil Moisture Data', fontsize=20)
...

5. View Graphs:
- Run the modified code to generate and view the respective graphs.
