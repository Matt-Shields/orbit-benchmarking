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

def run_comparison():
    orbit_proj = instantiate_orbit()
    costs = pd.DataFrame()
    _orbit_costs = pd.Series(orbit_proj.phase_costs, name='orbit')

    costs = pd.concat([costs, _orbit_costs], axis=1, sort="False")
    # costs['rel_err'] = costs.apply(lambda row: (row.iloc[1] - row.iloc[0]) / row.iloc[0] * 100, axis=1)
    print(costs)

def instantiate_orbit():
    ProjectManager.compile_input_dict(phases)
    path = os.path.join(os.getcwd(), "library")
    filepath = os.path.join('library', 'weather', 'ERA5_1979_2019.csv')
    weather = pd.read_csv(filepath, parse_dates=["datetime"]).set_index(keys='datetime')
    ORBIT_project = ProjectManager(config, weather=weather, library_path=path)
    ORBIT_project.run_project()
    return ORBIT_project

if __name__ == "__main__":
    run_comparison()