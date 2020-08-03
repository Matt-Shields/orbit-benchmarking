"""
Plot results from benchmarking exercise
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
# Read in shared Excel file
data = pd.read_excel('Detailed model comparison.xlsx', sheet_name='Output comparisons')
print(data)


# Turbine
_turbine_models = data.iloc[[11,12,14,17], 0]
_turbine_times = data.iloc[[11,12,14,17], 7]
_turbine_delays = data.iloc[[11,12,14,17], 9]
_turbine_cost = data.iloc[[11,12,14,17], 5]
_turbine_component = ['Turbine'] * len(_turbine_models)
# Monopile
_monopile_models = data.iloc[[20,21,23,25,26], 0]
_monopile_times = data.iloc[[20,21,23,25,26], 7]
_monopile_delays = data.iloc[[20,21,23,25,26], 11]
_monopile_cost = data.iloc[[20,21,23,25,26], 5]
_monopile_component = ['Monopile'] * len(_monopile_models)
# Array cable
_array_models = data.iloc[[29,30,32,34,35], 0]
_array_times = data.iloc[[29,30,32,34,35], 7]
_array_delays = data.iloc[[29,30,32,34,35], 9]
_array_cost = data.iloc[[29,30,32,34,35], 5]
_array_component = ['Array cable'] * len(_array_models)
# Export cable
_export_models = data.iloc[[38,39,41,43], 0]
_export_times = data.iloc[[38,39,41,43], 7]
_export_delays = data.iloc[[38,39,41,43], 9]
_export_cost = data.iloc[[38,39,41,43], 5]
_export_component = ['Export cable'] * len(_export_models)
# Substation



med_err = lambda x: 100 * (x - np.median(x)) / np.median(x)
_turbine_times_med_err = med_err(_turbine_times)
print(data)

# Build dataframe
results = pd.DataFrame({
                       'Model': pd.concat([_turbine_models, _monopile_models, _array_models, _export_models]),
                       'Component': _turbine_component +_monopile_component + _array_component + _export_component,
                       'Installation time, days': pd.concat([_turbine_times, _monopile_times, _array_times, _export_times]),
                       'Weather delays, days': pd.concat([_turbine_delays, _monopile_delays, _array_delays, _export_delays]),
                       'Installation cost, M. Euros': pd.concat([_turbine_cost, _monopile_cost, _array_cost, _export_cost]),
                       'Error relative to median': pd.concat([
                           med_err(_turbine_times), med_err(_monopile_times), med_err(_array_times), med_err(_export_times)
                       ])
})

fig0, ax0 = plt.subplots()
sns.stripplot(x='Component', y='Installation time, days', data=results, hue='Model',
              size=7, linewidth=1, palette=sns.color_palette("Set1"), ax=ax0)

fig1, ax1 = plt.subplots()
sns.stripplot(x='Component', y='Error relative to median', data=results, hue='Model',
              size=7, linewidth=1, palette=sns.color_palette("Set1"), ax=ax1)

plt.show()