import pandas as pd
import numpy as np
import random
import datetime

# Create a date range for the time series
start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2023, 12, 31)
date_range = [start_date + datetime.timedelta(days=i) for i in range((end_date - start_date).days + 1)]

# Generate fake data for the dataset
np.random.seed(0)
data = {
    'Date': date_range,
    'Revenue': np.random.randint(1000, 5000, len(date_range)),
    'Orders': np.random.randint(50, 200, len(date_range)),
    'Customers': np.random.randint(20, 100, len(date_range)),
    'Products_Sold': np.random.randint(100, 500, len(date_range)),
    'Returns': np.random.randint(5, 30, len(date_range))
}

# Create a DataFrame from the generated data
df = pd.DataFrame(data)

# Sort the DataFrame by date
df = df.sort_values(by='Date')

# Display the first few rows of the dataset
print(df.head())
