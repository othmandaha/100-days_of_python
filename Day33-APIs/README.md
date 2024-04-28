# Day33 - ISS_overhead_notifier

This Python script tracks the International Space Station (ISS) and sends a notification if the ISS is above your location during nighttime.

## Features

- **Is it Dark?**: Checks if it is currently nighttime at your location using sunrise and sunset times obtained from the Sunrise-Sunset API.
- **Is ISS Close?**: Checks if the ISS is close to your location by comparing its coordinates with your provided latitude and longitude.
- **Send Notification**: Sends an email notification if the ISS is close and it is dark outside.

## Usage

1. Replace `LATITUDE` and `LONGITUDE` variables with your location's coordinates.
2. Replace `MY_EMAIL` and `MY_PASSWORD` with your email credentials.
3. Run the script.
4. The script will continuously check if the ISS is close and it is dark outside. If conditions are met, it will send a notification email.

## Dependencies

- `requests`: Used to make HTTP requests to APIs.
- `datetime`: Used to get the current time and manipulate time objects.
- `math.isclose`: Used to compare floating-point numbers for approximate equality.
- `smtplib`: Used to send email notifications.

## Notes

- Make sure to enable less secure apps access in your email account settings if you're using Gmail.

