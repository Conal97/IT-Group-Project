from django.db.models.query import prefetch_related_objects
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from typing import OrderedDict
from django.core.exceptions import NON_FIELD_ERRORS
from django.shortcuts import redirect, render
from django.http import HttpResponse
from rango.models import Category, Page, Area, Munro
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime


def area(request):
    area_list = Area.objects.order_by('name')
    context_dict = {}
    context_dict['areas'] = area_list
    context_dict['prompt'] = 'Please select the area you would like to explore.'
    return render(request, 'rango/areas.html', context=context_dict)

def show_area(request, area_name_slug):
    context_dict = {}

    try:
        area = Area.objects.get(slug=area_name_slug)
        munros = Munro.objects.filter(area = area)
        context_dict['munros'] = munros
        context_dict['area'] = area
    except Area.DoesNotExist: 
        context_dict['area'] = None
        context_dict['munros'] = None
    
    return render(request, 'rango/show_area.html', context=context_dict)

#helper func
def get_server_side_cookie(request, cookie, default_val=None):
    val=request.session.get(cookie)
    if not val:
        val = default_val
    return val

#helper func
def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).seconds > 0:
        visits = visits + 1 
        request.session['last_visit'] = str(datetime.now())
    else:
                request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits

def index(request):
    #dictionary used to pass into template as context()
    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = pages_list
    
    visitor_cookie_handler(request)

    response = render(request, 'rango/index.html', context=context_dict)
    return response

def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by William'}
    context_dict['visits'] = request.session['visits']
    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):
    #create a context dictionary(will be passed to html file)
    context_dict = {}

    try:
        #try to find category name slug with given name(prameter passed)
        category = Category.objects.get(slug=category_name_slug)

        #retrieve all pages associated
        pages = Page.objects.filter(category = category)
        
        #add these pages to the dictionary
        context_dict['pages'] = pages

        #this used to verify category exists
        context_dict['category'] = category
    except Category.DoesNotExist: #throw exception if no such category
        #avoid doing anything, disaply no category message
        context_dict['category'] = None
        context_dict['pages'] = None
    
    return render(request, 'rango/category.html', context=context_dict)

@login_required
def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('rango:index'))
        
        else: print (form.errors)

    return render(request, 'rango/add_category.html', {'form': form})

@login_required
def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except:
        category = None

    if category is None:
        return redirect(reverse('rango:index'))

    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                print("HERE")
                return redirect(reverse('rango:show_category', kwargs={'category_name_slug': category_name_slug}))
            else:
                print(form.error)

    context_dict = {'form' : form, 'category': category}

    return render(request, 'rango/add_page.html', context = context_dict)

@login_required
def restricted(request):
    return render(request, 'rango/restricted.html')

'''def register(request):

    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user=user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'rango/register.html',
                            context= {  'user_form': user_form,
                                        'profile_form': profile_form,
                                        'registered': registered})'''

'''def user_login(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('rango:index'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else: 
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details provided")
    else:
        return render(request, 'rango/user_login.html')'''

'''def user_logout(request):
    logout(request)
    return redirect(reverse('rango:index'))'''

