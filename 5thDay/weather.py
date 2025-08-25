import requests
import pandas as pd
from datetime import date, timedelta
from typing import Dict, Any, Optional

# --- Configuration ---
LATITUDE = 17.3850
LONGITUDE = 78.4867
DAYS_TO_FETCH = 7

def fetch_weather_data(
    latitude: float, longitude: float, start_date: date, end_date: date
) -> Optional[Dict[str, Any]]:
    """
    Fetches daily weather forecast data from the Open-Meteo API.
    """
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}&"
        f"start_date={start_date.strftime('%Y-%m-%d')}&"
        f"end_date={end_date.strftime('%Y-%m-%d')}&"
        f"daily=temperature_2m_max,temperature_2m_min"
    )
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to connect to the weather service: {e}")
        return None
def process_data_to_dataframe(api_data: Dict[str, Any]) -> pd.DataFrame:
    """
    Processes the raw API data into a clean pandas DataFrame.
    """
    df = pd.DataFrame(api_data['daily'])
    df.rename(columns={
        'time': 'Date',
        'temperature_2m_max': 'Highest Temp (°C)',
        'temperature_2m_min': 'Lowest Temp (°C)'
    }, inplace=True)
    return df

def analyze_temperature_data(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Analyzes the weather DataFrame to find extremes and anomalies.
    """
    highest_temp_day = df.loc[df['Highest Temp (°C)'].idxmax()]
    lowest_temp_day = df.loc[df['Lowest Temp (°C)'].idxmin()]
    df['Max_Temp_Change'] = df['Highest Temp (°C)'].diff().abs()
    anomalies = df[df['Max_Temp_Change'] > 3].copy()
    return {
        "highest_temp_day": highest_temp_day,
        "lowest_temp_day": lowest_temp_day,
        "anomalies": anomalies
    }

def display_results(df: pd.DataFrame, analysis: Dict[str, Any]) -> None:
    """
    Prints the weather data and analysis results to the console.
    """
    print("--- Forecast for the Last 7 Days in Hyderabad ---")
    print(df[['Date', 'Highest Temp (°C)', 'Lowest Temp (°C)']].to_string(index=False))

    print("\n--- Overall Extremes for the 7-Day Period ---")
    highest = analysis['highest_temp_day']
    lowest = analysis['lowest_temp_day']
    print(f"The overall highest temperature was {highest['Highest Temp (°C)']}°C on {highest['Date']}.")
    print(f"The overall lowest temperature was {lowest['Lowest Temp (°C)']}°C on {lowest['Date']}.")

    print("\n--- Anomaly Report ---")
    anomalies_df = analysis['anomalies']
    if not anomalies_df.empty:
        print("Potential anomalies (sudden change in max temp > 3°C) were found:")
        for index, row in anomalies_df.iterrows():
            prev_day_temp = df.loc[index - 1, 'Highest Temp (°C)']
            print(f"- On {row['Date']}, temperature changed from {prev_day_temp}°C to {row['Highest Temp (°C)']}°C.")
    else:
        print("No significant temperature anomalies were detected.")

# --- Script Execution ---
# The code below will run directly when the script is executed.
end_date = date.today()
start_date = end_date - timedelta(days=DAYS_TO_FETCH - 1)

api_data = fetch_weather_data(LATITUDE, LONGITUDE, start_date, end_date)
print(api_data)
if api_data:
    try:
        weather_df = process_data_to_dataframe(api_data)
        analysis_results = analyze_temperature_data(weather_df)
        display_results(weather_df, analysis_results)
    except KeyError:
        print("Error: Could not parse the data. The API response structure may have changed.")
    except Exception as e:
        print(f"An unexpected error occurred during data processing: {e}")