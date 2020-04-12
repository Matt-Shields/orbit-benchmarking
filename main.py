"""
Compare ORBIT results with BVG Guide to Offshore Wind Farm

Matt Shields
"""

import os

import yaml
import pandas as pd
import matplotlib.pyplot as plt

import ORBIT
from ORBIT import ProjectManager
print(f"Using ORBIT version {ORBIT.__version__}.")

from orbit_config import phases, config, usd_to_euro

def generate_results(config_start_date, config_year):
    orbit_proj = instantiate_orbit(config_start_date, config_year)
    costs = pd.DataFrame()
    _orbit_costs = pd.Series(orbit_proj.phase_costs, name='orbit')

    costs = pd.concat([costs, _orbit_costs], axis=1, sort="False")
    # costs['rel_err'] = costs.apply(lambda row: (row.iloc[1] - row.iloc[0]) / row.iloc[0] * 100, axis=1)
    print(costs)

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

if __name__ == "__main__":
    config_start_date = '07/01'
    config_year = '2000'
    generate_results(config_start_date, config_year)