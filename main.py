"""
Compare ORBIT results with BVG Guide to Offshore Wind Farm

Matt Shields
"""

import os

import yaml
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import ORBIT
from ORBIT import ProjectManager
print(f"Using ORBIT version {ORBIT.__version__}.")

from orbit_config import phases, config, usd_to_euro

def instantiate_orbit(config_start_date, config_year):
    """ Instantiate instance of ORBIT project for a given year within the time series"""
    ProjectManager.compile_input_dict(phases)
    path = os.path.join(os.getcwd(), "library")
    filepath = os.path.join('library', 'weather', 'ERA5_1979_2019.csv')
    weather = pd.read_csv(filepath, parse_dates=["datetime"]).set_index(keys='datetime')

    # Update config for specified start date
    config_date = config_start_date + '/' + config_year
    config['install_phases'] = {k: config_date for (k, v) in config['install_phases'].items()}

    # Run project
    ORBIT_project = ProjectManager(config, weather=weather, library_path=path)
    ORBIT_project.run_project()

    return ORBIT_project

def generate_results(config_start_date, config_year, costs, times, weather_delays):
    """Run ORBIT project and compile results"""
    orbit_proj = instantiate_orbit(config_start_date, config_year)

    # Times and costs
    _orbit_costs = pd.Series(orbit_proj.phase_costs, name=config_year)
    _orbit_times = pd.Series(orbit_proj.phase_times, name=config_year)
    costs = pd.concat([costs, _orbit_costs], axis=1, sort="False")
    times = pd.concat([times, _orbit_times], axis=1, sort="False")

    # Weather delays
    _weather_delays = pd.Series()
    # Extract weather efficiency and convert to percent downtime
    for i in config['install_phases']:
        # Each phase has a different vessel efficiency name
        if 'Turbine' in i or 'Monopile' in i:
            _delay = times.loc[i].values[0] * (1 - orbit_proj._phases[i].\
                                     detailed_output[i]['WTIV_operational_efficiency'])
        elif 'Array' in i:
            _delay = times.loc[i].values[0] * (1 - orbit_proj._phases[i]. \
                                               detailed_output[i]['Array_Cable_Installation_Vessel_operational_efficiency'])
        elif 'Export' in i:
            _delay = times.loc[i].values[0] * (1 - orbit_proj._phases[i]. \
                                               detailed_output[i]['Export_Cable_Installation_Vessel_operational_efficiency'])
        elif 'Substation' in i:
            _delay = times.loc[i].values[0] * (1 - orbit_proj._phases[i]. \
                                               detailed_output[i]['Heavy_Lift_Vessel_operational_efficiency'])
        elif 'Scour' in i:
            _delay = times.loc[i].values[0] * (1 - orbit_proj._phases[i]. \
                                               detailed_output[i]['SPI_Vessel_operational_efficiency'])
        else:
           print('Weather delay not found for ', i)

        _weather_delays = _weather_delays.append(pd.Series(_delay, index=[i], name=config_year))
    weather_delays = pd.concat([weather_delays, _weather_delays], axis=1, sort='False')

    return costs, times, weather_delays

def compute_stats(costs, times, weather_delays):
    """Summary statistics over all years of weather data set"""
    # Costs (in millions of Euros for benchmarking work)
    average_costs = np.round(costs.mean(axis=1) * 1e-6 * usd_to_euro, 1)
    # Time (convert to days)
    average_times = np.round(times.mean(axis=1) * (1/24), 1)
    # Delays (convert to days)
    average_delays = np.round(weather_delays.mean(axis=1) * (1 / 24), 1)

    return average_costs, average_times, average_delays

if __name__ == "__main__":
    # Define start date for all phases and beginning/end year for statistical results
    config_start_date = '07/01'
    start_year = 1979
    end_year = 2018
    config_year = [str(y) for y in range(start_year, end_year+1)]
    # Initialize output structures and loop through each year of time series
    costs = pd.DataFrame()
    times = pd.DataFrame()
    weather_delays = pd.DataFrame()
    for c in config_year:
        costs, times, weather_delays = generate_results(config_start_date, c, costs, times, weather_delays)
    # Compute summary statistics and print results
    avg_cost, avg_time, avg_delays = compute_stats(costs, times, weather_delays)
    print("\nAverage phase cost (M Euro):\n----------")
    print(avg_cost)
    print("\nAverage phase duration (days):\n----------")
    print(avg_time)
    print("\nAverage phase weather delays (days):\n----------")
    print(avg_delays)
