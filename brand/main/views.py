from django.shortcuts import render
from django.http import HttpResponse
from .models import Services,About,Team,Clients,Portfolio

# Create your views here.



def index(request):

    services = Services.objects.filter(is_visible=True)
    about = About.objects.all()
    team = Team.objects.all()
    clients = Clients.objects.filter(is_visible=True)
    portfolio = Portfolio.objects.filter(is_visible=True)

    context = {

        'title_services': "Services",
        "under_services_title" : "Lorem ipsum dolor sit amet consectetur",
        "services" : services,

        'title_about': "About",
        "under_about_title" : "Lorem ipsum dolor sit amet consectetur.",
        "end_about_timeline" : "Be Part<br>&nbsp;Of Our<br>&nbsp;Story!",
        "about" : about,
        
        "team" : team ,

        "clients" : clients ,

        'title_portfolio': "Portfolio",
        "under_portfolio_title" : "Lorem ipsum dolor sit amet consectetur.",
        "portfolio_button" : "<span>&nbsp;Close Project</span>",
        "portfolio" : portfolio,

    }

    return render(request, "main.html", context=context)

    # return render(request, "main.html")