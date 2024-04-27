# Day 32 - Birthday Email Sender

This Python script automates the process of sending birthday emails to your contacts. It reads birthday information from a CSV file (`birthdays.csv`) and sends personalized emails to those whose birthdays match the current date.

## Prerequisites

Before running and testing the script, make sure you do the following:

1. **Update Email Credentials:**
   - Replace `YOUR EMAIL` with your email address in the `MY_EMAIL` variable.
   - Replace `YOUR PASSWORD` with your email password in the `MY_PASSWORD` variable.

2. **Allow Less Secure Apps:**
   - Go to your email provider settings and allow less secure apps to access your account. This step is necessary for SMTP authentication.

3. **Update SMTP Address:**
   - Update the SMTP server address in the script to match your email provider's SMTP server. Replace `"YOUR EMAIL PROVIDER SMTP SERVER ADDRESS"` with the correct SMTP server address.

4. **Update Birthdays Data:**
   - Ensure that the `birthdays.csv` file contains today's month and day for the birthdays you want to recognize.