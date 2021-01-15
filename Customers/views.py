import datetime

from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    if request.method == 'GET':
        Cust = Customers.objects.all()
        return render(request, 'Home.html', {'Cust': Cust})

    if request.method == 'POST':
        value = request.POST.get('submit')
        request.session['value'] = value
        request.method = 'GET'
        return redirect('Transfer')

def Transfer(request):
    try:
            if request.method == 'GET':
                if (request.session.get('value', None) != None):
                      value = request.session['value']
                      cust = Customers.objects.all()
                      person = Customers.objects.get(pk=value)
                      return render(request, 'transfer.html', {'obj': person, 'cust': cust})
            if request.method == 'POST':
                     value = request.session['value']
                     data1 = Customers.objects.get(pk=value)
                     data2 = Customers.objects.get(Name= request.POST['To'])
                     transfers = Transfers()
                     transfers.From = data1.Name
                     transfers.To = request.POST['To']
                     transfers.Amount = request.POST['Amount']
                     transfers.date = datetime.date.today()
                     if (int(request.POST['Amount']) > int(data1.Current_Balance)):
                         messages.info(request, 'Amount is more than available!')
                         request.method = 'GET'
                         return render(request, 'transfer.html')
                     else:
                         data1.Current_Balance = int(data1.Current_Balance) - int(request.POST['Amount'])
                         data2.Current_Balance = int(data2.Current_Balance) + int(request.POST['Amount'])
                         data1.save()
                         data2.save()
                         transfers.save()
                         messages.info(request, 'Transaction successful !')
                         request.method = 'GET'
                         return redirect('index')

    except Exception as e:
        print('Error:-',e)
        messages.info(request, 'Something went Wrong!')
        return redirect('/Transfer')

