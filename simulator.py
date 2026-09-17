import random

## TEST ##
# test = "testing testing 1 2 3"
# print(test)

## SIMULATOR ##

# PHASES #

PHASES = {
    "pre_launch": {
        "heart_rate": (50.0, 84.0),
        "SpO2": (95.0, 98.0), 
        "respiration": (6.0, 26.0), 
        "body_temp": (36.0, 36.8), 
        "g_force": (1.0, 1.0)
    }, 
    "launch": {
        "heart_rate": (82.0, 130.0),
        "SpO2": (94.0, 98.0), 
        "respiration": (10.0, 20.0), 
        "body_temp": (36.7, 36.7), 
        "g_force": (1.0, 4.0)
    }, 
    "ascent": {
        "heart_rate": (82.0, 130.0),
        "SpO2": (94.0, 98.0), 
        "respiration": (10.0, 20.0), 
        "body_temp": (36.5, 37.0), 
        "g_force": (1.0, 4.0)
    }, 
    "orbit": {
        "heart_rate": (60.0, 94.0),
        "SpO2": (94.4, 95.7), 
        "respiration": (10.0, 18.0), 
        "body_temp": (36.7, 38.0), 
        "g_force": (0.0, 0.0)
    }, 
    "exercise": {
        "heart_rate": (120.0, 160.0),
        "SpO2": (94.0, 98.0), 
        "respiration": (18.0, 35.0), 
        "body_temp": (38.4, 40.0), 
        "g_force": (0.0, 0.0)
    }, 
    "eva": {
        "heart_rate": (84.0, 150.0),
        "SpO2": (94.0, 98.0), 
        "respiration": (15.0, 30.0), 
        "body_temp": (37.0, 39.0), 
        "g_force": (0.0, 0.0)
    }, 
    "sleep": {
        "heart_rate": (50.0, 70.0),
        "SpO2": (94.0, 98.0), 
        "respiration": (8.0, 16.0), 
        "body_temp": (36.0, 37.5), 
        "g_force": (0.0, 0.0)
    }, 
    "reentry": {
        "heart_rate": (72.0, 104.0),
        "SpO2": (94.0, 98.0), 
        "respiration": (16.0, 24.0), 
        "body_temp": (37.9, 38.1), 
        "g_force": (3.33, 7.19)
    }, 
    "landing": {
        "heart_rate": (70.0, 110.0),
        "SpO2": (94.0, 98.0), 
        "respiration": (12.0, 24.0), 
        "body_temp": (37.0, 38.1), 
        "g_force": (6.0, 8.0)
    }
}

# RANDOM TELEMETRY GENERATOR #
def random_telemetry(phase, telemetry_type): 
    phase_data = PHASES[phase] # dictionary
    data_range = phase_data[telemetry_type] # tuple
    generated_telemetry = round(random.uniform(*data_range), 1) # float
    print(f"{telemetry_type}: {generated_telemetry}")
    # TO-D0: return and store generated_telemetry

random_telemetry("pre_launch", "heart_rate")


