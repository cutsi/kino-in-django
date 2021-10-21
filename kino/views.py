from django.shortcuts import render
from django.http import HttpResponse
from .models import Karta
from django.shortcuts import redirect
from .models import Projekcija
from .forms import *
from .models import Tickets
from .forms import ProjekcijaForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Max
from django.db.models import Min
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
"""
def home(request):
    context = {
        "projekcije":Projekcija.objects.all(),
        "tickets": Tickets.objects.all()
    }
    return render(request, 'kino/home.html',context)"""


def button_click(request):
    if(request.GET.get('mybtn')):
        customer=User.objects.get(user_id=request.user.id)
        ticket = Tickets(customer,Projekcija.objects.filter("karate kid").first())
        ticket.save()
    return render(request,'kino/home.html')

@staff_member_required
def staff(request):
    lst = []
    lst1 = []
    lst2 = []
    staff_list = []
    cnt = 0
    dic = {}
    users = User.objects.all()
    for usr in users:
        if usr.is_superuser:
            staff_list.append(usr)
    projekcije = Projekcija.objects.all()
    tickets = Tickets.objects.all()
    maxx = Projekcija.objects.aggregate(Max('broj_prodanih_karata'))
    minn = Projekcija.objects.aggregate(Min('broj_prodanih_karata'))
    proj_obj = Projekcija.objects.all().filter(broj_prodanih_karata = maxx.get("broj_prodanih_karata__max")).first()
    proj_obj_min = Projekcija.objects.all().filter(broj_prodanih_karata = minn.get("broj_prodanih_karata__min")).first()
    proj_obj_over_2 = Projekcija.objects.all().filter(broj_prodanih_karata__gt = 2)
    najveci = 0
    for ticket in tickets:
        for user in tickets:
            if ticket.user == user.user:
                cnt = cnt + 1
        if cnt > najveci:
            najveci = cnt
            usr = ticket.user
            lst2.append(cnt)
        cnt = 0
    
    for proj in projekcije:
        for ticket in tickets:
            if ticket.projekcija_id == proj.id and ticket.user.username not in lst1:
                lst1.append(ticket.user.username)
                lst.append(ticket)
        lst1 = []
            
    context = {
        "projekcije":Projekcija.objects.all(),
        "lst": lst,
        "max":proj_obj,
        "min":proj_obj_min,
        "mmm":proj_obj_over_2,
        "max_tickets":max(lst2),
        "user_with_most_tickets":usr,
        "staff_list":staff_list,
    }
    return render(request,'kino/staff.html', context)
    
def home(request):
    if(request.method == "POST"):
        ime_proj = request.POST.get("ime_filma")
        kapacitet = request.POST.get("kapacitet")
        if int(kapacitet) < 1:
            messages.error(request,f'No more tickets for projection ' + ime_proj)
            return redirect('kino-home')
        seat_exists = False
        seat = request.POST.get("broj_sjedala")
        proj_id = request.POST.get('proj_id')
        proj_obj = Projekcija.objects.all().filter(id = proj_id).first()
        tickets = Tickets.objects.all()
        for ticket in tickets:
            if ticket.projekcija == proj_obj and ticket.seat_number == seat:
                seat_exists = True
        if seat_exists == False:
            ticket = Tickets(user = request.user, projekcija = proj_obj, seat_number = seat)
            ticket.save()
            proj_obj.kapacitet_dvorane = proj_obj.kapacitet_dvorane - 1
            proj_obj.broj_prodanih_karata = proj_obj.broj_prodanih_karata + 1
            proj_obj.save()
            return redirect("profile")
        messages.error(request,f'Ticket seat is taken')
        return redirect('kino-home') 
    elif request.method == "GET" or None:
        context = {
        "projekcije":Projekcija.objects.all(),
        "tickets": Tickets.objects.all()
    }
        return render(request, 'kino/home.html',context)

#napraviti novi template i na njemu ispisati imena prva 3 korisnika koji su kupili najveci broj karata 