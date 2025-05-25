# Feedback Uploader for Web Service

This Python script was developed as part of a Qwiklabs automation lab. It reads customer feedback stored in text files and uploads it to a Django-powered web service using a REST API.

## Features

- Reads `.txt` files containing feedback from `/data/feedback`
- Extracts structured content (title, name, date, feedback body)
- Converts each entry into a JSON dictionary
- Sends POST requests using the `requests` library
- Validates success response from the server

## Usage

1. Ensure the Django server is running and accessible via its IP.
2. Place your feedback files in `/data/feedback` (format: title, name, date, feedback).
3. Run the script:

```bash
python3 upload_feedback.py
```

Each file will be parsed and submitted to the server at:

```
http://<your-server-ip>/feedback/
```

Update the IP in the script if needed.

## Author

Bekzod Ochilov
