import requests

def main():
    #api_key = open('api.txt', r).read()
    api_key = '7f393e3ce56acd17a4493f50687bd033'
    #location = input("Enter location: ")
    URI = 'http://api.openweathermap.org/data/2.5/weather'
    
    
    while True:
        location = input('Enter location or Exit to logoff: ').lower().lower()

        if location == "exit": return

        weather_details = requests.get(f'{URI}?q={location}&units=metric&appid={api_key}')

        if weather_details.json()['cod'] == '404':
            print("Invalid location!")
            continue
                    
        description = weather_details.json()['weather'][0]['description']
        temperature = round(weather_details.json()['main']['temp'])
        feels_like = round(weather_details.json()['main']['feels_like'])
        high = round(weather_details.json()['main']['temp_max'])
        low = round(weather_details.json()['main']['temp_min'])

        print(f"The weather in {location[0].upper()}{location[1:]} is {temperature}° C with {description}.")
        print(f"It feels like {feels_like}° C.")
        print(f"Today's high is {high}° C and today's low is {low}° C.")

        print("more details:")
        print(weather_details.json())


main()