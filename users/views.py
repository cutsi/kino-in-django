from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from kino.models import Tickets
from kino.models import Projekcija
from django.contrib.auth.models import User

def register(request):
    if (request.method == "POST"):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created')
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form' : form})

@login_required()
def profile(request):
    tickets = Tickets.objects.all().filter(user = request.user)
    context = {"tickets": tickets}
    return render(request, "users/profile.html", context)

def test(request):
    proj_lst = Projekcija.objects.all().filter(kapacitet_dvorane = 18)
    cap = -1
    context = {
        "projekcije":proj_lst,
        "users_with_x_tickets": users_with_x_tickets(16),
        "projections_with_x_tickets":projections_with_x_tickets("9"),
        "projections_with_greater_than_x_capacity":projections_with_greater_than_x_capacity(cap),
        "cap":cap,
        "list_users":list_users()
        }
    return render(request, "users/test.html" ,context)

def users_with_x_tickets(num):
    cnt = 0
    lst = []
    lst_usernames = []
    tickets = Tickets.objects.all()
    for ticket in tickets:
        for user in tickets:
            if ticket.user == user.user:
                cnt = cnt + 1
        if cnt == num and ticket.user.username not in lst_usernames:
            lst_usernames.append(ticket.user.username)
            lst.append(ticket)
        cnt = 0
    return lst

def projections_with_x_tickets(seat_num):
    proj_lst = []
    tickets = Tickets.objects.all().filter(seat_number = seat_num)
    return tickets

def projections_with_greater_than_x_capacity(cap):
    proj = Projekcija.objects.all().filter(kapacitet_dvorane__gt = cap)
    return proj


def list_users():
    customers=User.objects.all().filter(is_superuser = False, is_staff=False)
    return customers

def obrana_zadnje_vjezbe(request):
    najveci1 = 0
    najveci2 = 0
    najveci3 = 0
    lst_count = []
    lst_users = []
    cnt = 0
    tickets = Tickets.objects.all()

    for ticket in tickets:
        for user in tickets:
            if ticket.user == user.user:
                cnt = cnt + 1
        if(ticket.user.username not in lst_users and cnt not in lst_count):
            lst_users.append(ticket.user.username)
            lst_count.append(cnt)
        cnt = 0

    najveci1 = max(lst_count)
    lst_count.remove(max(lst_count))
    print("najveci1")
    print(najveci1)
    najveci2 = max(lst_count)
    lst_count.remove(max(lst_count))
    print("najveci2")
    print(najveci2)
    najveci3 = max(lst_count)
    lst_count.remove(max(lst_count))
    print("najveci3")
    print(najveci3)

    najveci_usr1 = users_with_x_tickets(najveci1)
    najveci_usr2 = users_with_x_tickets(najveci2)
    najveci_usr3 = users_with_x_tickets(najveci3)
    context = {
        "najveci_usr1":najveci_usr1,
        "najveci_usr2":najveci_usr2,
        "najveci_usr3":najveci_usr3
        }
    return render(request,"users/obranaZadnjeVjezbe.html",context)


















#ispisati projekciju koja ima najveci/najmani broj prodanih karata
#projekcije koje imaju broj karata veci/manji od x prodanih
#svi useri koji imaju status admin/staff/active
#user sa najvise/najmanje kupljenih karata 
#pip install django-crispy-forms

#proj sa odredjenim kapacitetom done!!!!!!
#useri koji su kupili jednu kartu done!!!!!! 
#projekcije sa odredjenim brojem sjedala done!!!!!
#ispisi sve porjekcije koje sadrzavaju odredjeno sjedalo done!!!!!
#projekcije sa odredjenim kapacitetom npr vecim od 15 done!!!!!
#filtriranje karata koji imaju broj sjedala 9 npr done !!!!!
#ispisat oibcne korisnike done!!!!!
#broj slobonihi mjesta po projekciji done!!!!!
#korisnici koji su uzeli najmanje/najvise karata done!!!!!
