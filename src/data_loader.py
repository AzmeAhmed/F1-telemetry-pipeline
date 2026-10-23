import fastf1 

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


if __name__ == '__main__':
    # Test execution using standard English naming conventions
    compare_driver_laptimes(2024, 'Silverstone', 'HAM', 'VER')
