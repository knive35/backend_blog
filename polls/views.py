from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from polls.models import blog
import json

def index(request):
   title=blog.objects.first().title
   categories=blog.objects.first().categories
   content=blog.objects.first().content
   #JSONObj= {}
   #JSONObj=blog()
   #JSONObj = {"bookname ": title, "price": content, "asd":categories}
   data = {'a': title, 'b': content, 'c': categories}

   #json = demjson.encode(data)
   #print (json)
   #json = '{"a": title, "b": content, "c": categories}'
   #text = demjson.decode(json)
   return HttpResponse(json.dumps(data))