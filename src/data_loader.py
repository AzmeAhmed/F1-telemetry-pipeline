import os
import fastf1

def load_f1_session_data():
    """
    Enables caching, loads the Singapore 2023 Grand Prix race session,
    prints basic summary statistics, and extracts telemetry data for all drivers.
    """
    # 1. Enable caching for FastF1 to optimize data retrieval and prevent redundant API requests
    cache_dir = 'f1_cache'
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
        
    fastf1.Cache.enable_cache(cache_dir) 

    # 2. Load the specific F1 session object (Singapore 2023 - Race)
    print("Fetching data from F1 servers (this might take a while on the first run)...")
    year = 2023
    grand_prix = 'Singapore'
    session_type = 'R'  # 'R' denotes the main Race session
    
    session = fastf1.get_session(year, grand_prix, session_type)
    session.load()  # Loads all timing, telemetry, weather, and results data

    # 3. Print basic session results to the terminal (Fully Automated)
    print("\n=================== SESSION INFO ===================")
    print(f"Event:       {session.event['EventName']} {year}")
    print(f"Session:     {session.name}")
    print("----------------------------------------------------")

    # Dynamically fetch the race winner (Index 0 in the sorted results dataframe)
    winner = session.results.iloc[0]
    print(f"Winner:      {winner['FullName']} ({winner['TeamName']})")

    # Dynamically fetch the absolute fastest lap of the entire race
    fastest_lap = session.laps.pick_fastest()
    fastest_driver = fastest_lap['Driver']
    
    # Format the timedelta to a highly readable string format (MM:SS.mmm)
    fastest_time = str(fastest_lap['LapTime'])[10:19] 
    print(f"Fastest Lap: {fastest_time} by driver {fastest_driver}")
    print("====================================================\n")

    # 4. Prepare telemetry data for all drivers (Data visualization foundation)
    print("Processing multi-driver telemetry data...")
    all_drivers_telemetry = {}

    for driver in session.drivers:
        driver_abbr = session.results.loc[driver]['Abbreviation']
        driver_laps = session.laps.pick_driver(driver)
        
        # Skip drivers who didn't complete a single lap (e.g., DNS or early DNF)
        if driver_laps.empty:
            continue
            
        # Get the fastest single lap for this specific driver to analyze their peak performance
        fastest_lap_driver = driver_laps.pick_fastest()
        
        # Extract full telemetry data (Speed, Throttle, Brake, RPM, Gear, Distance)
        telemetry = fastest_lap_driver.get_car_data().add_distance()
        
        # Store telemetry in a dictionary mapped by the driver's abbreviation
        all_drivers_telemetry[driver_abbr] = {
            'telemetry_df': telemetry,
            'team_name': session.results.loc[driver]['TeamName'],
            'all_laps_df': driver_laps
        }
    
    print(f"Successfully processed telemetry for {len(all_drivers_telemetry)} active drivers.")
    print("Data loader is fully primed for visualization pipelines.")
    
    return session, all_drivers_telemetry

if __name__ == '__main__':
    load_f1_session_data()