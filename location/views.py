from django.shortcuts import render
import requests
import json
# Create your views here.

def index(request):
    ip = requests.get('https://api.ipify.org?format=json')   # This is for user IP
    ip_address = json.loads(ip.text)
    res = requests.get('http://ip-api.com/json/'+ip_address['ip']) # This is location information api
    location_one = res.text
    location_data = json.loads(location_one)
    return render(request, 'index.html', {'data': location_data})