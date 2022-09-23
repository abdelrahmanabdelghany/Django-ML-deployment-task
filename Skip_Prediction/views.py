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
        if valid(Data) :
            print(valid(Data))
            result=predict(Data)
            return render(request,'resultpage.html',{'name':result})
        else:     return render(request,'EnterFeaures.html',{'message':'please enter valid values'})



def predict(Data):
    prediction = model.predict(np.array(Data).reshape(1, -1))
    if prediction==1:
        return 'skipped'
    if prediction==0:
        return 'not skipped'

def valid(Data):

    sesseion_lenght=Data[0]
    end_trackdone=Data[1]
    if sesseion_lenght=='' or end_trackdone== '':
        print('empty')
        return False
    sesseion_lenght=int(Data[0])
    end_trackdone=int(Data[1])
    if sesseion_lenght>0 and end_trackdone in[0,1] :
        return True
