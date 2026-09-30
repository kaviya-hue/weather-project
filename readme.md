# 🌤️ Python Weather App

A simple Python weather application that uses the **OpenWeatherMap API** to fetch and display the current weather information for a city.

## Features

* Enter any city name
* Fetch current weather data
* Display city name
* Display temperature in Celsius
* Display weather condition
* Uses `.env` to securely store the API key

## Technologies Used

* Python
* Requests
* Python-dotenv
* OpenWeatherMap API

## Project Structure

```text
weather/
│
├── main.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
cd weather
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## API Key Setup

Create a `.env` file in the project folder:

```env
weather_api_key=YOUR_API_KEY
```

Get an API key from OpenWeatherMap:

https://openweathermap.org/api

**Do not upload your `.env` file to GitHub.**

## Run the Project

```bash
python main.py
```

Example:

```text
Enter city: Pondicherry

City: Puducherry
Temperature: 34.31 °C
Weather: few clouds
```

## How It Works

The program:

1. Loads the API key from the `.env` file.
2. Takes the city name from the user.
3. Sends a request to the OpenWeatherMap API.
4. Receives the weather information as JSON.
5. Extracts the city, temperature, and weather condition.
6. Displays the information in the terminal.

## Author

Kaviya
