import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('avglQpercountry.csv')

# Filter countries with an average IQ >= 100
filtered_df = df[df['Average IQ'] >= 100]

# Sort by "Average IQ" in descending order
filtered_df = filtered_df.sort_values(by="Average IQ", ascending=False)

# Print the filtered DataFrame
print(filtered_df)

# Create the bar plot
plt.figure(figsize=(14, 8))
bars = plt.bar(filtered_df['Country'], filtered_df['Average IQ'], color="skyblue")

# Add title and labels
plt.title("Average IQ by Country (IQ >= 100)")
plt.xlabel('Country')
plt.ylabel('Average IQ')

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Show the plot
plt.tight_layout()  # Adjusts the layout to prevent label cutoff
plt.show()
