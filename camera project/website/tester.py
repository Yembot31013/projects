import requests

url = "https://python.org/static/stylesheets/style.a193d3b62d35.css"

response = requests.get(url)
with open('test.css', 'wt') as p:
  p.write(response.text)