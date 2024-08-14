import requests
import os
import datetime
import asyncio

# Assuming DATA is a dictionary to store the weather information
DATA = {}

async def set_weather_information():
    api_key = os.getenv('weather_API')  # Use the secret named 'weather_API'
    city = 'stockholm'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        r = response.json()

        DATA['city_temperature'] = round(r['main']['temp'])
        DATA['city_weather'] = r['weather'][0]['description']
        DATA['city_weather_icon'] = r['weather'][0]['icon']
        DATA['sun_rise'] = datetime.datetime.fromtimestamp(r['sys']['sunrise']).astimezone().strftime('%H:%M')
        DATA['sun_set'] = datetime.datetime.fromtimestamp(r['sys']['sunset']).astimezone().strftime('%H:%M')

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

def generate_readme():
    # Call the weather information function
    asyncio.run(set_weather_information())

    # Generate the README content
    content = f"# Auto Regenerate Repository\n\n"
    content += f"This README was last updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    content += f"\n![TryHackMe](https://tryhackme-badges.s3.amazonaws.com/deshoha.png)\n"
    
    # Add weather information to the README
    if 'city_temperature' in DATA:
        content += f"\n## Weather Information\n"
        content += f"- Temperature: {DATA['city_temperature']}°C\n"
        content += f"- Weather: {DATA['city_weather']}\n"
        content += f"- Weather Icon: ![Weather Icon](http://openweathermap.org/img/wn/{DATA['city_weather_icon']}@2x.png)\n"
        content += f"- Sunrise: {DATA['sun_rise']}\n"
        content += f"- Sunset: {DATA['sun_set']}\n"

    with open("README.md", "w") as readme_file:
        readme_file.write(content)

if __name__ == "__main__":
    generate_readme()
