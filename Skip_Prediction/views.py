from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import pickle
import numpy as np
# Create your views here.

#request handler
result=[]
model=[]
def say_hello(request):
    global model
    model = pickle.load(open('DT.pkl', 'rb'))
    return render(request,'Home.html',{'name':'aboda'})

def secondpage(request):
    return render(request,'EnterFeaures.html')

@csrf_exempt
def resultpage(request):
    if request.method == 'POST':
        Data=list(request.POST.dict().values())


        print(Data)

        result=predict(Data)
        print(result)
        return render(request,'resultpage.html',{'name':result})



def predict(Data):
    prediction = model.predict(np.array(Data).reshape(1, -1))
    print(prediction)
    if prediction==1:
        return 'song will be skipped'
    if prediction==0:
        return 'song wont be skipped'
