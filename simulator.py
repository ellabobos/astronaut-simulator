import random, time

## TEST ##
# test = "testing testing 1 2 3"
# print(test)

## SIMULATOR ##

# PHASES #

phases = ["pre_launch", "launch", "ascent", "orbit", "exercise", "eva", "sleep", "reentry", "landing"]
phase_times = {"pre_launch": 6, "launch": 6, "ascent": 4, "orbit": 14, "exercise": 6, "eva": 8, "sleep": 8, "reentry": 5, "landing": 3}
past_phases = {} # phases the astronaut has already been in + the corresponding telemetry (updates once per second)

PHASES_DATA = {
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
# TO-DO: return and store generated_telemetry
def point_tlm(phase, telemetry_type): 
    phase_data = PHASES_DATA[phase] # dictionary
    data_range = phase_data[telemetry_type] # tuple

    if phase in past_phases: # if the astronaut has been in this phase
        phase_tlm = past_phases[phase]
        if telemetry_type in phase_tlm: # if this type of telemetry has been recorded for this phase
            lower_fluct = phase_tlm[telemetry_type] - 1
            higher_fluct = phase_tlm[telemetry_type] + 1
            # If the fluct can go beyond the bounds of this telemetry type, keep this telemetry point the same
            if (lower_fluct < data_range[0] or higher_fluct > data_range[1]): 
                generated_telemetry = phase_tlm[telemetry_type]
                print(f"{telemetry_type}: {generated_telemetry}")
            else: # the fluct cannot go beyond the bounds of this telemetry type
                generated_telemetry = round(random.uniform(phase_tlm[telemetry_type] - 1, phase_tlm[telemetry_type] + 1), 1)
                print(f"{telemetry_type}: {generated_telemetry}")
        else: # this type of telemetry has not been recorded for this phase
            generated_telemetry = round(random.uniform(*data_range), 1) # baseline (where astronaut starts)
            print(f"{telemetry_type}: {generated_telemetry}")
            phase_tlm[telemetry_type] = generated_telemetry # add this type of telemetry to the dictionary associated w/ the current phase
    else: # the astronaut has not yet experienced this phase
        generated_telemetry = round(random.uniform(*data_range), 1) # baseline (where astronaut starts)
        print(f"{telemetry_type}: {generated_telemetry}")

        # Creates a dictionary of the phases we've been in and matches the telemetry names w/ the generated telemetry
        curr_tlm = {telemetry_type: generated_telemetry}
        past_phases[phase] = curr_tlm

def phase_tlm(phase):
    phase_data = PHASES_DATA[phase]
    for tlm in phase_data:
        point_tlm(phase, tlm)



# START SIM #
# TO-DO
#   * (DONE) Make 1-minute simulation (5-min sim / 5)
#       - pre-launch: 0:00-0:06 (6)
#       - launch: 0:06-0:12 (7)
#       - ascent: 0:12-0:16 (5)
#       - orbit: 0:16-0:30 (15)
#       - exercise: 0:30-0:36 (7)
#       - sleep: 0:36-0:44
#       - orbit: 0:44-0:52
#       - reentry: 0:52-0:57
#       - landing: 0:57-1:00
#   * Fix what's adding an extra second to each phase (except the first phase)
#   * Program each phase with an adequate length of time (~20-30 secs/phase)
#       - 5-minute simulation
#       - (DONE) Once a telemetry value is chosen (at random), the fluctuations should
#         be small for the rest of the phase
#       - During phase transitions, the telemetry fluctuations can increase/decrease
#         more dramatically based on the two phases involved (might have to consult research) (e.g. how quickly (or not) the g-force increases during descent)
#   * (DONE) Within a phase, make the telemetry fluctuations smooth (realistic)
#       - Future Goal: tailor the small fluctuations to the phase (size of fluctuations
#         depend on the type of telemetry) (e.g. g-force probably doesn't fluctuate by 1 as much as the other telemetry types)
#   * (DONE) Fix mission time so that it continuously increases across all phases
#   * Make the transition between phases smoother (to increase accuracy of the simulation)
#       - Might need to adjust length of phases to accomodate for these transitions (in order to keep it at a 1 or 5 min sim)
#   * (DONE) For the small fluctuations, don't let them go beyond the upper and lower bounds of that telemetry type (e.g. g-force cannnot be -0.6)
#   * Clean up point_tlm
#       - helper functions might help reduce the embedded if/else statements
#

def start_sim():
    mission_time = 0
    for phase in phases:
        phase_length = phase_times[phase]
        for second in range(0, phase_length + 1):
            print(f"Mission time: {mission_time} seconds")
            print(f"Phase: {phase}")

            mission_time += 1

            phase_tlm(phase)
            print("")
            time.sleep(1)

start_sim()
