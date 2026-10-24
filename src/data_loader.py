import fastf1 
import pandas as pd

def compare_driver_laptimes(year: int, grand_prix: str, driver_a: str, driver_b: str) -> None:
    """
    Fetch session data and mathematically compare the fastest lap time between two drivers.
    """ 
    # Initialize and load the session
    session = fastf1.get_session(year, grand_prix, 'R')  # 'R' for race session
    session.load()

    # Extract all lap data
    laps = session.laps

    # Filter fastest lap for each driver
    fastest_lap_a = laps.pick_driver(driver_a).pick_fastest()
    fastest_lap_b = laps.pick_driver(driver_b).pick_fastest()

    # Extract the actual lap time values
    time_a = fastest_lap_a['LapTime']
    time_b = fastest_lap_b['LapTime']

    # Convert sector times into timedelta format for analysis
    s1_time_a = pd.Timedelta(fastest_lap_a['Sector1Time'])
    s1_time_b = pd.Timedelta(fastest_lap_b['Sector1Time'])

    s2_time_a = pd.Timedelta(fastest_lap_a['Sector2Time'])
    s2_time_b = pd.Timedelta(fastest_lap_b['Sector2Time'])

    s3_time_a = pd.Timedelta(fastest_lap_a['Sector3Time'])
    s3_time_b = pd.Timedelta(fastest_lap_b['Sector3Time'])

    # Output individual results to stdout
    print(f"Driver {driver_a} fastest lap: {time_a}")
    print(f"Driver {driver_b} fastest lap: {time_b}")
    print("-" * 50)

    # Perform the mathematical comparison to determine the faster driver
    if time_a < time_b:
        delta = time_b - time_a
        print(f"ANALYSIS RESULT: {driver_a} was faster than {driver_b} by {delta.total_seconds():.3f} seconds!")
    elif time_b < time_a:
        delta = time_a - time_b
        print(f"ANALYSIS RESULT: {driver_b} was faster than {driver_a} by {delta.total_seconds():.3f} seconds!")
    else:
        print("ANALYSIS RESULT: Both drivers recorded the exact same lap time down to the millisecond!")


    # Perform the mathematical comparison for Sector 1
    if s1_time_a < s1_time_b:
        delta = s1_time_b - s1_time_a
        print(f"SECTOR 1 RESULT: {driver_a} was faster than {driver_b} by {delta.total_seconds():.3f} seconds!")
    elif s1_time_b < s1_time_a:
        delta = s1_time_a - s1_time_b
        print(f"SECTOR 1 RESULT: {driver_b} was faster than {driver_a} by {delta.total_seconds():.3f} seconds!")
    else:
        print("SECTOR 1 RESULT: Both drivers recorded the exact same Sector 1 time!")


    # Perform the mathematical comparison for Sector 2
    if s2_time_a < s2_time_b:
        delta = s2_time_b - s2_time_a
        print(f"SECTOR 2 RESULT: {driver_a} was faster than {driver_b} by {delta.total_seconds():.3f} seconds!")
    elif s2_time_b < s2_time_a:
        delta = s2_time_a - s2_time_b
        print(f"SECTOR 2 RESULT: {driver_b} was faster than {driver_a} by {delta.total_seconds():.3f} seconds!")
    else:
        print("SECTOR 2 RESULT: Both drivers recorded the exact same Sector 2 time!")


    # Perform the mathematical comparison for Sector 3
    if s3_time_a < s3_time_b:
        delta = s3_time_b - s3_time_a
        print(f"SECTOR 3 RESULT: {driver_a} was faster than {driver_b} by {delta.total_seconds():.3f} seconds!")
    elif s3_time_b < s3_time_a:
        delta = s3_time_a - s3_time_b
        print(f"SECTOR 3 RESULT: {driver_b} was faster than {driver_a} by {delta.total_seconds():.3f} seconds!")
    else:
        print("SECTOR 3 RESULT: Both drivers recorded the exact same Sector 3 time!")


if __name__ == '__main__':
    # Test execution using standard English naming conventions
    compare_driver_laptimes(2024, 'Silverstone', 'HAM', 'VER')
