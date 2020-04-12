usd_to_euro = 0.92

phases = [
    # Substructures
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
    # Substations
    #     "num_substations": 1,

    # Vessels
    #     'scour_protection_install_vessel': 'ExampleScour',
    #     'trench_dig_vessel': 'StematSpirit',
    #     'array_cable_lay_vessel': 'cable_lay_vessel',
    #     'export_cable_lay_vessel': 'StematSpirit',
    #     "oss_install_vessel": "OlegStrashnov",  # Actually vessel from SPT Offshore

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
        'layout': 'grid',
        'num_turbines': 50,
        'row_spacing': 7,
        'turbine_spacing': 9,
        'substation_distance': 1
    },

    'port': {
        'num_cranes': 1,
        'monthly_rate': 0,  # 2000000,
        "name": "Green Port"
    },

    # Turbine + components
    'turbine': '8MW_generic',

    # Substructure components
    'substructure': {'diameter': 7.2},
    'monopile': {
        'type': 'Monopile',
        'length': 69,
        'diameter': 7.2,
        'deck_space': 496.8,
        'mass': 800,
        'monopile_steel_cost': 2000 / usd_to_euro,
    },

    'transition_piece': {
        'type': 'Transition Piece',
        'deck_space': 100,
        'mass': 400,
        'transition_piece_steel_cost': 2000 / usd_to_euro,
    },

    'scour_protection_design': {
        'cost_per_tonne': 40,
        #         'scour_protection_depth':0.3
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
        'num_substations': 2
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
        'wtiv': 'Benchmarking_WTIV_turbine'
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
        'spi_vessel': 'example_scour_protection_vessel'
    },

    # Phases
    'design_phases': [
        #         "MonopileDesign",
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