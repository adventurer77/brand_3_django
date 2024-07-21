from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Services,About,Team,Clients,Portfolio
from .forms import ContactForm
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):

    template_name = "main.html"


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        services = Services.objects.filter(is_visible=True)
        about = About.objects.all()
        team = Team.objects.all()
        clients = Clients.objects.filter(is_visible=True)
        portfolio = Portfolio.objects.filter(is_visible=True)
        form = ContactForm()

        
        
        context['title_services'] =  "Services"
        context["under_services_title"] = "Lorem ipsum dolor sit amet consectetur"
        context["services"] = services

        context['title_about'] = "About"
        context["under_about_title" ] = "Lorem ipsum dolor sit amet consectetur."
        context["end_about_timeline"] = "Be Part<br>&nbsp;Of Our<br>&nbsp;Story!"
        context["about"] = about
            
        context["team"] = team 

        context["clients"] = clients 

        context['title_portfolio'] = "Portfolio"
        context["under_portfolio_title"] = "Lorem ipsum dolor sit amet consectetur."
        context["portfolio_button"] = "<span>&nbsp;Close Project</span>"
        context["portfolio"] = portfolio

        context['title_contact'] = "Contact Us"
        context["under_contact_title"] = "Lorem ipsum dolor sit amet consectetur."
        context["contact_button"] = "Send Message"
        context["form"] = form

        return context
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Thank you for your question, we will contact you as soon as possible.")
            return redirect('main:index')
        else:
            
            messages.error(request, "There were errors in your form. Please correct and try again.")
            
            return redirect('main:index')

# def index(request):

#     services = Services.objects.filter(is_visible=True)
#     about = About.objects.all()
#     team = Team.objects.all()
#     clients = Clients.objects.filter(is_visible=True)
#     portfolio = Portfolio.objects.filter(is_visible=True)

#     context = {

#         'title_services': "Services",
#         "under_services_title" : "Lorem ipsum dolor sit amet consectetur",
#         "services" : services,

#         'title_about': "About",
#         "under_about_title" : "Lorem ipsum dolor sit amet consectetur.",
#         "end_about_timeline" : "Be Part<br>&nbsp;Of Our<br>&nbsp;Story!",
#         "about" : about,
        
#         "team" : team ,

#         "clients" : clients ,

#         'title_portfolio': "Portfolio",
#         "under_portfolio_title" : "Lorem ipsum dolor sit amet consectetur.",
#         "portfolio_button" : "<span>&nbsp;Close Project</span>",
#         "portfolio" : portfolio,

#     }

#     return render(request, "main.html", context=context)

    # return render(request, "main.html")