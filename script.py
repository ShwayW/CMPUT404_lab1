import requests
print(requests.__version__)
page = requests.get('https://www.google.com')
print(page.status_code)
print(page.text)
script_itself = requests.get('https://raw.githubusercontent.com/ShwayW/CMPUT404_lab1/shway/script.py')
print(script_itself.text)