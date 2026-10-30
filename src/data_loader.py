import fastf1 
import pandas as pd
import matplotlib.pyplot as plt

def compare_driver_laptimes(year: int, grand_prix: str, driver_a: str, driver_b: str) -> None:
    """
    Fetch session data and mathematically compare the fastest lap time and telemetry between two drivers.
    """ 
    # Steg 2: Robust felhantering kring laddningen
    try:
        session = fastf1.get_session(year, grand_prix, 'R')  # 'R' for race session
        session.load()
        laps = session.laps
    except Exception as e:
        print(f"ERROR: Failed to load session data for {year} {grand_prix}. Details: {e}")
        return

    # Filter fastest lap for each driver (updated syntax with 'drivers')
    fastest_lap_a = laps.pick_drivers(driver_a).pick_fastest()
    fastest_lap_b = laps.pick_drivers(driver_b).pick_fastest()

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

    # Steg 3: Utöka telemetrin (hämta maxhastighet)
    telemetry_a = fastest_lap_a.get_telemetry()
    telemetry_b = fastest_lap_b.get_telemetry()
    
    max_speed_a = telemetry_a['Speed'].max()
    max_speed_b = telemetry_b['Speed'].max()

    # Output individual results to stdout
    print(f"Driver {driver_a} fastest lap: {time_a}")
    print(f"Driver {driver_b} fastest lap: {time_b}")
    print(f"Driver {driver_a} max speed: {max_speed_a:.1f} km/h")
    print(f"Driver {driver_b} max speed: {max_speed_b:.1f} km/h")
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

    plt.figure(figsize=(10, 5))

    plt.plot(telemetry_a['Distance'], telemetry_a['Speed'], label=f"{driver_a} Speed", color='blue')
    plt.plot(telemetry_b['Distance'], telemetry_b['Speed'], label=f"{driver_b} Speed", color='red')
    plt.xlabel("Distance (m)")
    plt.ylabel("Speed (km/h)")
    plt.title("Speed Comparison")
    plt.legend()
    plt.savefig("f1_telemetry_output.png")
    plt.close()