import requests

API_URL = "https://www.virustotal.com/api/v3/files"
FILE_NAME = "webpack.png"

with open('.env', 'r') as env_file:
  API_KEY = env_file.readline().strip()

files = {"file": (FILE_NAME, open(FILE_NAME, "rb"), "image/png")}
headers = {"accept": "application/json", "x-apikey": API_KEY }
response = requests.post(API_URL, files=files, headers=headers)

analysis_id = response.json()['data']['id']

# ANALYSIS_URL = "https://www.virustotal.com/api/v3/analyses/MzdmNjYyZDdlZjc1ZGI3MGE3ZWRmYjljMzY4YWYwNzc6MTY3MDE4NTAxNQ%3D%3D"
ANALYSIS_URL = "https://www.virustotal.com/api/v3/analyses/" + analysis_id

headers = {"accept": "application/json", "x-apikey": API_KEY }

response = requests.get(ANALYSIS_URL, headers=headers)
print(response.text)

