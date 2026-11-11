# 🌦️ Basic Weather App – Python

## 📌 Project Overview
The Basic Weather App is a Python-based application that fetches current weather information for a given city using the OpenWeatherMap API.

Users can enter a city name and get real-time weather details.

## ✨ Features
- Enter any city name.
- Display city name.
- Show temperature in Celsius (°C).
- Show temperature in Fahrenheit (°F).
- Display humidity percentage.
- Show weather description.
- Display wind speed.
- Handle invalid city names.
- Handle network errors.

## 🛠️ Technologies Used
- Python
- Requests Library
- OpenWeatherMap API
- JSON

## 📂 Project Structure

```text
Task-4-Weather-App/
│
├── weather_app.py
├── README.md
└── .gitignore
```

## ⚙️ Installation

**Step 1:** Install Python on your computer.

**Step 2:** Install the required library.

```bash
pip install requests
```

**Step 3:** Create an account on OpenWeatherMap and generate an API key.

Website: https://openweathermap.org/

**Step 4:** Add your API key to the Python program.

```python
API_KEY = "YOUR_API_KEY"
```

Replace `YOUR_API_KEY` with your actual API key.

**Important:** Never upload your actual API key to GitHub.

## ▶️ How to Run

Open the terminal in VS Code and execute:

```bash
python weather_app.py
```

Enter your city name when prompted.

Example:

```text
Enter city name: Ahmedabad
```

## 📊 Sample Output

```text
----- WEATHER REPORT -----

City: Ahmedabad
Temperature: XX °C
Temperature: XX °F
Humidity: XX %
Weather: clear sky
Wind Speed: X m/s
```

*Note: Actual weather values change according to current weather conditions.*

## ❌ Error Handling

The application handles:
- Invalid city names.
- Invalid API keys.
- Network connection errors.
- API request errors.

## 🎯 Objective

The main objective of this project is to learn Python API integration, JSON data handling, user input, and exception handling.

## 👨‍💻 Internship Details

**Organization:** Oasis Infobyte  
**Internship Track:** Python Programming  
**Task Number:** Task 4  
**Project Name:** Basic Weather App

---

**Developed using Python as part of the Oasis Infobyte Python Programming Internship.**
