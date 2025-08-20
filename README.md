# 🌤️ POGODKIN - weather forecast service

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3%2B-lightgrey?logo=flask)](https://flask.palletsprojects.com/)
[![OpenWeather](https://img.shields.io/badge/API-OpenWeatherMap-orange?logo=openweathermap)](https://openweathermap.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

<div align="center">
  <img src="static\images\example.png" width="1000" alt="Pogodkin Preview">
  
  *minimalistic weather service*
</div>

## ✨ Peculiarities

- **🎯 Accurate data** - current weather from OpenWeatherMap API
- **🎨 Stylish design** - glassmorphism and smooth gradients
- **⚡ Quick search** - instantly get weather for any city
- **🌡️ Detailed information** - temperature, humidity, pressure, wind speed

## 🛠️ Tech stack

### Backend
- **Python 3.10+** - main programming language
- **Flask** - lightweight web framework
- **Flask-Async** - asynchronous request processing
- **Aiohttp** - working with HTTP requests

### Frontend
- **HTML5** - semantic layout
- **CSS3** - modern styles and animations
- **Glassmorphism** - design with glass effect
- **Adaptive layout** - mobile-first approach

### API
- **OpenWeatherMap** - getting meteorological data

## 🚀 Install and Run

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- OpenWeatherMap API key

### 1. Cloning the repository
```bash
git clone https://github.com/zkqw3r/Weather-website.git
cd Weather-website
```
### 2. Creating a virtual environment
```bash
python -m venv venv
```
#### or
```bash
python3 -m venv venv
```
### 3. Setting up a virtual environment
```bash
source venv/bin/activate  # Linux/Mac
```
#### or
```bash
venv\Scripts\activate     # Windows
```
### 4. Installing dependencies
```bash
pip install -r requirements.txt
```
### 5. Setting up environment variables
Create a .env file in the root directory:
env
```bash
API="your_api_key_here"
```
### 6. Launching the application
```bash
python flask_app.py
```
💻 The application will be available at: http://127.0.0.1:5000/ or http://localhost:5000
---
### 📝 To-do list

- [ ] Display weather for several days ahead

- [ ] Another language

