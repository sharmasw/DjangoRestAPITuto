from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views import View
# Create your views here.

@require_http_methods(['GET'])
def index(request):
    if request.method=='GET':
        return JsonResponse({'a':'a'})

@require_http_methods(['POST'])
def postINdex(request):
    if request.method=='POST':
        return JsonResponse({'b':'b'})

'''Because Django’s URL resolver expects to send the request and associated arguments to a callable function, 
not a class, class-based views have an as_view() class method which returns a function that can be called when 
a request arrives for a URL matching the associated pattern'''


data ={}


def recordAll(request):
    if request.method=='GET':
        return JsonResponse(data) #retriev data


class AppAPI(View):

    http_method_names=['get','post','put','delete']

    def get(self,request,userID):
        if request.method =='GET':
            return JsonResponse({'result':data[userID]})


    def post(self,request):
        if request.method=='POST':
            userID=request.POST['userID']
            comments=request.POST['comments']
            data[userID]=comments
        return JsonResponse({'result':'Added comment of user '+ userID})
    
    def put(self,request,userID):
        if request.method=='PUT':
            print (request.body)
            import json
            bodyval=json.loads(request.body)
            print (bodyval)
            data[userID]=bodyval['comments']
        return JsonResponse({'result':'Added comment of user '+ userID})

    def delete(self,request,userID):
        if request.method =='DELETE':
            del data[userID]
            return JsonResponse({'result':'Deleted'})

