import requests

def get_geolocation(api_key, search_string):

    base_url = "https://us1.locationiq.com/v1/search"

    params = {
        "key": api_key,
        "q": search_string,
        "format": "json"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200 and data:
        result = {
            "place_id": data[0].get("place_id",""),
            "lat": data[0].get("lat",""),
            "lon": data[0].get("lon",""),
            "display_name": data[0].get("display_name","")
        }
        return result
    else:
        return None


api_key = ""

search_string = input("Enter location: ")

result = get_geolocation(api_key, search_string)

if result:
    print("Output:")
    for key,value in result.items():
        print(f"{key}: {value}")
