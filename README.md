# NASA Picture of the Day Generator

This Python script utilizes NASA's Astronomy Picture of the Day (APOD) API to fetch and save the daily celestial image. The script requires the `requests` library for API calls and the `PIL` (Pillow) library to handle and save images.

## Prerequisites

Before running the script, make sure you have the required libraries installed. You can install them using the following:

```bash
pip install requests Pillow
```

## API Key

To access NASA's APOD API, you need to obtain an API key. For testing purposes, a demo key is provided in the script (`DEMO_KEY`). For production or frequent use, it's recommended to get your own key from the [NASA API website](https://api.nasa.gov).

## Usage

1. Clone the repository or download the script.
2. Replace the `apiKey` variable with your NASA API key.
3. Run the script.

```bash
python script_name.py
```

## Output

The script will print a message indicating that it is running, and then it will fetch the information of the Picture of the Day from NASA's API. Subsequently, it will download and save the image as "Picture_Of_The_Day.png" in the script's directory.

Note: In case of any errors during the process, an error message will be displayed.
