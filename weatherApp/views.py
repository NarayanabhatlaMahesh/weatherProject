from django.shortcuts import render, HttpResponse
import requests

x = requests.get


# Create your views here.
def firstfunction(request):
    data={}
    apikey="639e0e2a424031a335c60202c1a9c2a0"
    if request.method=='POST':
        city=request.POST['city']
        source = requests.get('https://api.openweathermap.org/data/2.5/weather?&appid='+apikey+'&q='+city)
        print(source.json())
        keys=[]
        vals=[]
        for i in source.json():
            keys.append(i)
            vals.append(source.json()[i])
            a=zip(keys,vals)
        return render(request, 'firstfunction.html',{'keys':a})
    return render(request,'firstfunction.html')