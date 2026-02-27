"""
Configuration file for Clinical AI Early Warning Platform.
Contains simulation parameters, patient types, and alert thresholds.
"""

SIMULATION_PARAMS = {
    "patient_type": "normal",
    "update_interval": 1,  # seconds
    "bp_threshold": 140,
    "hr_threshold": 100,
    "spO2_threshold": 92,
}
