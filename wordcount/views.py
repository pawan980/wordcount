from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'homepage.html')

def count(request):
    text=request.GET['text']
    wordlist=text.split()
    return render(request,'count.html',{'text':text,'count':len(wordlist)})
