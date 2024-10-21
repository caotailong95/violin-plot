import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data from the user
data = {
    'Monitoring Position': ['1', '2', '3', '4'],
    'Max Size (mm)': [1153.95, 1154.03, 1153.97, 1153.93],
    'Min Size (mm)': [1154.09, 1154.16, 1154.05, 1154.02],
    'Nominal (mm)': [1154.00, 1154.00, 1154.00, 1154.00],
    'Mean (mm)': [1154.01, 1154.08, 1154.02, 1153.99],
    'STD (mm)': [0.02, 0.02, 0.01, 0.01],
    '6STD (mm)': [0.13, 0.09, 0.07, 0.08],
    'L-OUT%': [25.95, 0.00, 5.55, 86.85],
    'Tot-OUT%': [25.95, 0.00, 5.55, 86.85],
    'Est.Low (mm)': [1153.95, 1154.03, 1153.97, 1153.93],
    'Est.High (mm)': [1154.09, 1154.16, 1154.05, 1154.02],
    'Est.Range (mm)': [0.14, 0.13, 0.08, 0.09],
}

# Actual measured distances
actual_measured = [1154.015, 1153.991, 1153.948, 1154.009]

# Generate data points for the distributions based on the given means and STDs
np.random.seed(42)
n_runs = 2000
dist_data = {
    'Position 1': np.random.normal(1154.01, 0.02, n_runs),
    'Position 2': np.random.normal(1154.08, 0.02, n_runs),
    'Position 3': np.random.normal(1154.02, 0.01, n_runs),
    'Position 4': np.random.normal(1153.99, 0.01, n_runs),
}

# Convert the data to a DataFrame for plotting
df_dist = pd.DataFrame(dist_data)

# Create the violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(data=df_dist, inner="quartile", cut=0)

# Highlight the actual measured points
for i, actual in enumerate(actual_measured):
    plt.scatter(i, actual, color='red', s=100, marker='x', label=f'Actual Measurement {i+1}' if i == 0 else "")

# Set labels and title
plt.title('Violin Plot for Monitoring Positions with Actual Measurements Highlighted')
plt.xlabel('Monitoring Position')
plt.ylabel('Size (mm)')
plt.legend(loc='upper left')

# Show the plot
plt.show()
