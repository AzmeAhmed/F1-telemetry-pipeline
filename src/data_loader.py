import fastf1 

def compare_driver_laptimes(year: int, grand_prix: str, driver_a: str, driver_b: str)-> None:

    """
    Fetch session data and compare the fastest lap time between two drivers.
    """ 
    # Initalize and load the session
    session = fastf1.get_session(year, grand_prix, 'R')  # 'R' for race session
    session.load()

    # Extract all lap data
    laps = session.laps

    # Filter fastest lap for each driver
    fastest_lap_a = laps.pick_driver(driver_a).pick_fastest()
    fastest_lap_b = laps.pick_driver(driver_b).pick_fastest()

    # Output results to stdout
    print(f"Driver {driver_a} fastest lap: {fastest_lap_a['LapTime']}")
    print(f"Driver {driver_b} fastest lap: {fastest_lap_b['LapTime']}")


if __name__ == '__main__':
    # Test execution using standard english naming conventions
    compare_driver_laptimes(2024, 'Silverstone', 'HAM', 'VER')