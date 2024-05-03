# Day 35 - Stock Trading Alert 

## Introduction
This Python script monitors the stock price of a specified company and sends SMS alerts with recent news headlines if the stock price increases or decreases by 5%.

## Requirements
- Python 3.x
- `requests` library (for making HTTP requests)
- `twilio` library (for sending SMS alerts)
- API keys for Alpha Vantage (for stock data) and News API (for news data)
- Twilio account SID and authentication token

## Usage
1. Install the required libraries by running:
    ```
    pip install requests twilio
    ```

2. Obtain API keys:
    - **Alpha Vantage**: Sign up at [Alpha Vantage](https://www.alphavantage.co/) and obtain an API key.
    - **News API**: Sign up at [News API](https://newsapi.org/) and obtain an API key.
    - **Twilio**: Sign up at [Twilio](https://www.twilio.com/) and obtain your account SID and authentication token.

3. Set environment variables:
    - Set the environment variables `TWILIO_SID` and `TWILIO_AUTH` with your Twilio account SID and authentication token respectively.

4. Replace `'Your Number here'` with your phone number in international format (e.g., `+1234567890`) where you want to receive the SMS alerts.

5. Run the script. It will fetch the stock data, calculate the percentage change in stock price, retrieve recent news related to the company, and send an SMS alert if the percentage change is greater than or equal to 5%.

## Code Explanation
- The script first imports necessary libraries: `requests`, `os`, and `twilio.rest.Client`.
- It defines constants for the stock symbol, company name, stock API endpoints, API keys, and Twilio credentials.
- Makes an HTTP request to the Alpha Vantage API to fetch daily stock data.
- Parses the JSON response to extract the closing prices of the last two days.
- Calculates the percentage change in stock price.
- If the percentage change is greater than or equal to 5%, it fetches news related to the company using the News API.
- Constructs an SMS message with the headline and description of the top news article.
- Sends the SMS alert using Twilio.

## Note
- Ensure that you have sufficient credits or allowance for sending SMS alerts using Twilio to avoid any charges.

