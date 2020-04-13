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

def generate_results(config_start_date, config_year, costs, times):
    orbit_proj = instantiate_orbit(config_start_date, config_year)
    _orbit_costs = pd.Series(orbit_proj.phase_costs, name=config_year)
    _orbit_times = pd.Series(orbit_proj.phase_times, name=config_year)

    costs = pd.concat([costs, _orbit_costs], axis=1, sort="False")
    times = pd.concat([times, _orbit_times], axis=1, sort="False")

    # costs['rel_err'] = costs.apply(lambda row: (row.iloc[1] - row.iloc[0]) / row.iloc[0] * 100, axis=1)
    return costs, times

def compute_stats(costs, times):
    """Statistical results"""
    average_costs = np.round(costs.mean(axis=1) * 1e-6 * usd_to_euro, 1)
    average_times = np.round(times.mean(axis=1) * (1/24), 1)

    return average_costs, average_times

if __name__ == "__main__":
    config_start_date = '07/01'
    start_year = 2000
    end_year = 2002
    config_year = [str(y) for y in range(start_year, end_year)]
    costs = pd.DataFrame()
    times = pd.DataFrame()
    for c in config_year:
        costs, times = generate_results(config_start_date, c, costs, times)

    avg_cost, avg_time = compute_stats(costs, times)
    print(avg_cost, avg_time)