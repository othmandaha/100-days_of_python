# Day35 - Rain Alert App 

This Python script checks the weather forecast for rain in the next 12 hours using the OpenWeatherMap API and sends an SMS notification using Twilio if rain is expected.

## Prerequisites
- Python 3.x
- `requests` library
- `twilio` library
- OpenWeatherMap API key
- Twilio account SID and authentication token

## Installation
1. Clone or download the repository.
2. Install the required libraries using pip:
    ```
    pip install requests twilio
    ```

## Usage
1. Set up environment variables for the OpenWeatherMap API key, Twilio SID, and Twilio authentication token.
2. Modify the latitude and longitude coordinates according to the desired location.
3. Run the script.