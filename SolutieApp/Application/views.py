from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

#----daca crapa sterge
from .models import Category, Product, Site, Function, SiteFunction

from .forms import LoginForm, SignUpForm, TemplatesForm, StoreForm, ProductCreationForm

def get_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            raw_pass = form.cleaned_data('password')
            new_user = authenticate(username=user, password=raw_pass)
            login(request, new_user)
            return HttpResponseRedirect('/dashboard/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def get_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/dashboard/')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


@login_required
def get_dashboard(request):
    sites = Site.objects.filter(created_by=request.user)
    return render(request, 'dashboard.html', {'sites':sites})

@login_required
def get_build(request):
    if request.method== 'POST':
        if 'submit1' in request.POST:
            form = TemplatesForm(request.POST)
            if form.is_valid():
                app_type = form.cleaned_data.get('wanted_template')
                app_name = form.cleaned_data.get('app_name')
                if app_type=='online_store':
                    save_form = StoreForm(initial={'title':app_name, 'app':app_type})
                products = Product.objects.all()
                productform = ProductCreationForm()
                return render(request, app_type + '.html', {'products': products,
                'name': app_name,
                'type': app_type.replace('_', ' '),
                'form': save_form,
                'productform': productform})
        elif 'submit2' in request.POST:
            site = Site.objects.filter(title=request.POST.get('title'))
            site_function = SiteFunction.objects.filter(site = site[0])
            functions = []
            for x in site_function:
                functions.append(x.function.name)
            return render(request,site[0].template + '.html', {
            'name' : site[0].title,
            'type': site[0].template,
            'form': StoreForm(initial={'title':site[0].title, 'app':site[0].template}),
            'productform': ProductCreationForm(),
            'functions': functions})

    else:
        return HttpResponseRedirect('/dashboard/')


@login_required
def save_product(request):
    if request.method=='POST':
        form = ProductCreationForm(request)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard/')

@login_required
def save_site(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            site = Site.objects.filter(title = form.cleaned_data.get('title'))
            if not site:
                site = Site(title = form.cleaned_data.get('title'), template = form.cleaned_data.get('app'), created_by = request.user)
                site.save()
            else:
                site = site[0]
            txt = form.cleaned_data.get('functions')
            function_names = txt.split("_")
            function_names.pop()
            SiteFunction.objects.filter(site = site).delete()
            for function_name in function_names:
                function = Function.objects.filter(name = function_name)
                if not function:
                    function = Function(name = function_name)
                    function.save()
                else:
                    function = function[0]
                site_function = SiteFunction(site = site, function = function)
                site_function.save()
            return HttpResponseRedirect('/dashboard/')


@login_required
def get_forms(request):
    form = TemplatesForm()
    return render(request, 'forms.html', {'form':form})

#-----daca crapa sterge
def all_products(request):
    products = Product.objects.all()
    return render(request, 'online_store.html', {'products': products})

def categories(request):
    return {
        'categories' : Category.objects.all()
    }

def get_template_online_store(request):
    if request.method == 'POST':
        products = Product.objects.all()
        site = Site.objects.filter(title=request.POST.get('title'))
        site_function = SiteFunction.objects.filter(site = site[0])
        functions = []
        for x in site_function:
            functions.append(x.function.name)

        return render(request, 'template_online_store.html', {'products': products,
        'site' : site[0],
        'functions': functions})


def get_summary(request):
    products = Product.objects.all()
    site = Site.objects.filter(title='Pinguinii')
    site_function = SiteFunction.objects.filter(site = site[0])
    functions = []
    for x in site_function:
        functions.append(x.function.name)
    return render(request, 'summary.html', {'products': products,
    'site' : site[0],
    'functions': functions})