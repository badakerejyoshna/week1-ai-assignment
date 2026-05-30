import requests

url = "https://catfact.ninja/fact"

response = requests.get(url)
data = response.json()

print("=== CAT FACT ===")
print("Fact:", data["fact"])
print("Length:", data["length"])