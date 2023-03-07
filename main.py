import requests

url = "http://10.147.180.32:8112//alarm/v1/sendMessage"


data = {
    'phone': '18378307928',
    'title': 'test',
    'content':'test'
}
response = requests.post('http://10.147.180.32:8112//alarm/v1/sendMessage', data=data)
if response.status_code ==200:
    print("sucess")
else:
    print(response.content)