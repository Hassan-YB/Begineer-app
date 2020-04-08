from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse ,HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .models import International,Domestic,Flight,Passenger
from .forms import NameForm


def index(request):
    latest_flights_list=Flight.objects.order_by('-Starting_time')[:5]
    context={'latest_flights_list':latest_flights_list}
    return render(request,'flights/index.html',context)

def detail(request,Flight_id):
    flight=get_object_or_404(Flight,pk=Flight_id)
    if request.method=='POST':
        form=NameForm(request.POST)
        if form.is_valid():
            passenger=Passenger()
            passenger.Passenger_flight=flight
            passenger.Name=form.cleaned_data['name']
            passenger.Surname=form.cleaned_data['surname']
            passenger.save()
            return HttpResponseRedirect('/flights/')
    else:
        form=NameForm()
    return render(request,'flights/detail.html',{'flight':flight,'form':form})

