# This Phyton code (v2) is created by Burcak Avci for "Dataset on surface topographies prepared by micro-milling and their friction coefficients in dry sliding" for the data repository at 10.5281/zenodo.18014400

# Dependencies
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import matplotlib.cm as cm

# Data location relative to script location. If both are in same folder, use '.'
data_dir = './data' 
input_dir =os.path.join(data_dir, 'exported_AP')

# Verify data path existance
if not os.path.exists(input_dir):
    print(f"Error: The directory {input_dir} was not found...")

print(f"Files in data directory: {os.listdir(data_dir)}")
print(f"Files in input directory: {os.listdir(input_dir)}")

filename = "CoF_S13_90_1N.txt" # Arbitrarily chosen sample and sliding orientation from Data Set 2
filepath = os.path.join(input_dir, filename)

data = np.loadtxt(filepath, encoding='latin1', skiprows=1) # Data loading

# Data processing
all_x_data_pairs = []
all_y_data_pairs = []

if data.ndim > 1:
    num_pairs = data.shape[1] // 2

    for i in range(num_pairs):
        x_vals = data[:, 2 * i]
        y_vals = data[:, 2 * i + 1]
        all_x_data_pairs.append(x_vals)
        all_y_data_pairs.append(y_vals)

    print(f"Successfully loaded and extracted {num_pairs} x-y pairs from {filename}.")
    print(f"Each pair contains {len(all_x_data_pairs[0])} data points.")
else:
    print(f"Error: Data is not in the expected 2D format for {filename}.")
# Plotting all scratch cycles 
plt.figure(figsize=(12, 8))

colormap = plt.colormaps['plasma']
colors = [colormap(i / (num_pairs - 1)) for i in range(num_pairs)]

for i in range(num_pairs):
    plt.plot(all_x_data_pairs[i], all_y_data_pairs[i], color=colors[i], label=f'{i+1}')

plt.xlabel('Distance (mm)', fontsize=18)
plt.xlim(0,3)
plt.ylabel('CoF', fontsize=18)
plt.ylim(0,1)
plt.title(f'Scratch cycles 1-{num_pairs} for {filename}', fontsize=18)
plt.legend(loc='upper right', ncol=10, fontsize=15, columnspacing=0.5)
plt.annotate("a)", xy=(0.1, 0.9), fontsize=30)
plt.grid(True)
plt.tick_params(axis='x', labelsize=18)
plt.tick_params(axis='y', labelsize=18)
plt.tight_layout()
plt.show()

# Calculation of average CoF for each scratch cycle
file_avg_values = []
file_std_values = []

# Define the starting index (for x-values) and x-value range - to disregard the effect of running-in for steady-state average calculation
start_index = 47  # Row 48 (0-indexed)
x_min = 1.0       # 1 mm
x_max = 3.0       # 3 mm

for i in range(num_pairs):
    x_array = all_x_data_pairs[i]
    y_array = all_y_data_pairs[i]

    # Consider data points from the start_index onwards
    x_subset = x_array[start_index:]
    y_subset = y_array[start_index:]

    # Create a boolean mask for x-values within the specified range
    mask = (x_subset >= x_min) & (x_subset <= x_max)

    # Apply the mask to get the filtered y-values for the current pair
    filtered_y_for_current_pair = y_subset[mask]

    # Calculate mean and standard deviation for the current pair's filtered y-values
    avg_y = np.mean(filtered_y_for_current_pair)
    std_y = np.std(filtered_y_for_current_pair)

    file_avg_values.append(avg_y)
    file_std_values.append(std_y)

# Append a dictionary with the filename and its average y-values to the main list
# (Ensure all_avg_values and all_std_values are initialized if not already)
if 'all_avg_values' not in locals() or 'all_avg_values' not in globals():
    all_avg_values = []
if 'all_std_values' not in locals() or 'all_std_values' not in globals():
    all_std_values = []

all_avg_values.append({'Filename': filename, 'Average_CoF_per_cycle': file_avg_values})
all_std_values.append({'Filename': filename, 'Std_CoF_per_cycle': file_std_values})

print(f"Calculated mean and std dev for {num_pairs} pairs from {filename}.")
print(f"First 5 average CoF values per cycle: {file_avg_values[:5]}")
print(f"First 5 standard deviation CoF values per cycle: {file_std_values[:5]}")

# Create a pandas DataFrame from the currently collected data for the single file
df_current_file_avg = pd.DataFrame([{'Filename': filename, 'Average_CoF_per_cycle': file_avg_values}])
df_current_file_std = pd.DataFrame([{'Filename': filename, 'Std_CoF_per_cycle': file_std_values}])

print("\nDataFrame for current file's average CoF values:")
display(df_current_file_avg)

# Plotting average CoF for each scratch cycle
plt.figure(figsize=(12, 8))

x_cycle_numbers = np.arange(1, num_pairs + 1)

y_avg_cof = df_current_file_avg['Average_CoF_per_cycle'].iloc[0]

plt.scatter(x_cycle_numbers, y_avg_cof, c=colors, s=50)
plt.errorbar(x_cycle_numbers, y_avg_cof, yerr=df_current_file_std['Std_CoF_per_cycle'].iloc[0], fmt='none', color='grey', capsize=5)

plt.xlabel('Scratch cycles', fontsize=18)
plt.xlim(0, num_pairs + 1)
plt.ylabel('Average CoF', fontsize=18)
plt.title(f'Variation of CoF for {filename}', fontsize=18)
plt.annotate("b)", xy=(2, 0.9), fontsize=30)
plt.grid(True)
plt.tick_params(axis='x', labelsize=18)
plt.tick_params(axis='y', labelsize=18)
plt.tight_layout()
plt.show()
