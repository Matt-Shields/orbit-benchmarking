usd_to_euro = 0.92

phases = [
    # Substructures
    'MonopileDesign',
    'MonopileInstallation',
    #     'ScourProtectionDesign',
    #     'ScourProtectionInstallation',

    # Turbines
    'TurbineInstallation',

    #     # Electrical
    'ArraySystemDesign',
    'ArrayCableInstallation',
    'ExportSystemDesign',
    'ExportCableInstallation',
    'OffshoreSubstationDesign',
    'OffshoreSubstationInstallation'
]

config = {
    # Site/plant
    'site': {
        'depth': 22.5,
        'distance': 124,
        'distance_to_landfall': 42,
        'distance_to_beach': 0,
        'distance_to_interconnection': 3,
        'mean_windspeed': 9.13
    },

    'plant': {
        'layout': 'ring',
        'num_turbines': 50,
        'row_spacing': 9,
        'turbine_spacing': 7,
        'substation_distance': 1
    },

    'port': {
        'num_cranes': 1,
        'monthly_rate': 0,  # 2000000,
        "name": "Green Port"
    },

    # Turbine + components
    'turbine': '20MW_generic',

    # Substructure components
    # 'substructure': {'diameter': 7.2},
    # 'monopile': {
    #     'type': 'Monopile',
    #     'length': 69,
    #     'diameter': 7.2,
    #     'deck_space': 496.8,
    #     'mass': 800,
    #     'monopile_steel_cost': 2000 / usd_to_euro,
    # },

    # 'transition_piece': {
    #     'type': 'Transition Piece',
    #     'deck_space': 100,
    #     'mass': 400,
    #     'transition_piece_steel_cost': 2000 / usd_to_euro,
    # },

    # Use Monopile Design module
    'monopile_design': {
        'monopile_steel_cost': 2000 / usd_to_euro,
        'tp_steel_cost': 3000 / usd_to_euro,
        'transition_piece_length': 15,
        'load_factor': 2.75
    },

    'scour_protection_design': {
        'cost_per_tonne': 50,
        # 'scour_protection_depth': 2
    },

    # Electrical
    'array_system_design': {
        'cables': 'XLPE_630mm_66kV'
    },

    'array_system': {
        'strategy': 'lay_bury'
    },

    'export_system': {
        'strategy': 'lay_bury'
    },

    'export_system_design': {
        'cables': 'XLPE_1000mm_220kV',
        'percent_added_length': 0
    },

    'substation_design': {
        'num_substations': 2,
        # Updated to increase substation costs to reflect ORCA, BNEF values
        'oss_pile_cost_rate': 2250,
        'oss_substructure_cost_rate': 6250,
        'mpt_cost_rate': 25000,  # 125000 gives us ~41m/MW, per BNEF
        'topside_fab_cost_rate': 29000,
        'shunt_cost_rate': 70000
    },

    #     "offshore_substation_topside": {
    #         "type": "Topside",
    #         "deck_space": 200,
    #         "weight": 2000,
    #     },
    #     "offshore_substation_substructure": {
    #         "type": "Monopile",
    #         "deck_space": 500,
    #         "weight": 1850,
    #         "length": 69,  # Assumed to be the same as monopile length
    #     },

    # Phase specific configurations
    'MonopileInstallation': {
        'wtiv': 'Benchmarking_WTIV_turbine',

    },

    'TurbineInstallation': {
        'wtiv': 'Benchmarking_WTIV_20MW_turbine',
        'kwargs': {"tower_section_fasten_time": 2.0,  # hr, applies to all sections
                   "tower_section_release_time": 0.0,  # hr, applies to all sections
                   "tower_section_attach_time": 0.5,  # hr, applies to all sections
                   "nacelle_fasten_time": 2.5,  # hr
                   "nacelle_release_time": 0.0,  # hr
                   "nacelle_attach_time": 1.0,  # hr
                   "blade_fasten_time": 1.0,  # hr
                   "blade_release_time": 0.0,  # hr
                   "blade_attach_time": 2.0,  # hr
                   "site_position_time": 4.6 # hr
                   },
    },

    'ArrayCableInstallation': {
        'array_cable_install_vessel': 'cable_lay_vessel'
    },

    'ExportCableInstallation': {
        'export_cable_install_vessel': 'cable_lay_vessel'
    },

    'OffshoreSubstationInstallation': {
        "num_feeders": 2,
        "feeder": "zero_cost_large_feeder",
        "oss_install_vessel": "Benchmarking_WTIV_turbine"
    },

    'ScourProtectionInstallation': {
        'spi_vessel': 'current_scour_protection_vessel'
    },

    # Phases
    'design_phases': [
                "MonopileDesign",
                'ScourProtectionDesign',
                'ArraySystemDesign',
                'ExportSystemDesign',
                'OffshoreSubstationDesign'
    ],

    'install_phases': {
        'MonopileInstallation': '07/01/2000',  # Updated dates
        'ScourProtectionInstallation': '07/01/2000',  # Placed at the end of the monopile installation
        'TurbineInstallation': '07/01/2000',
        'ArrayCableInstallation': '07/01/2000',
        'ExportCableInstallation': '07/01/2000',
        'OffshoreSubstationInstallation': '07/01/2000'
    }
}