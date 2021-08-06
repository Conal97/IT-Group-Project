from rango.bing_search import run_query
from django.db.models.query import prefetch_related_objects
from rango.forms import HikeReportForm, HikerProfileForm, HikerBaggedMunrosForm
from typing import OrderedDict
from django.core.exceptions import NON_FIELD_ERRORS
from django.shortcuts import redirect, render
from rango.models import Area, Hiker, Image, Munro, UserLikeArea, UserLikeMunro
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    #dictionary used to pass into template as context()
    area_list = Area.objects.all().order_by('-likes')[:3]
    munro_list = Munro.objects.all().order_by('-likes')[:3]

    context_dict = {}
    context_dict['pageheading'] = 'Rango'
    context_dict['areas'] = area_list
    context_dict['munros'] = munro_list
    
    visitor_cookie_handler(request)

    response = render(request, 'rango/index.html', context=context_dict)
    return response

def about(request):
    context_dict = {'pageheading': 'About Rango'}
    return render(request, 'rango/about.html', context=context_dict)

# For using the bing API to search the web
def search(request):
    result_list = []

    if request.method == 'POST':
        query = request.POST['query'].strip()

        # Use the bing search function
        if query:
            result_list = run_query(query)

    return render(request, 'rango/search.html', {'result_list':result_list})

def photo_gallery(request):
    images = Image.objects.all()

    context_dict = {}
    context_dict['pageheading'] = 'Photo Gallery'
    context_dict['images'] = images
    
    return render(request, 'rango/photo_gallery.html', context = context_dict)


def munro(request, munro_name_slug):
    context_dict = {}
    context_dict['details'] = "Details: "
    context_dict['reviews'] = "View community hike reports here"
    try:
        munro = Munro.objects.get(slug=munro_name_slug)
        context_dict['munro'] = munro
    except Munro.DoesNotExist: 
        context_dict['munro'] = None
    return render(request, 'rango/munro.html', context=context_dict)

@login_required
def hike_report(request):
    if request.method == "POST":
        form = HikeReportForm(request.POST) 
        if form.is_valid(): 
            post = form.save(commit=False) 
            post.date = timezone.now() 
            post.author = request.user 
            post.save() 
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    else: 
         form=HikeReportForm() 
    return render(request, 'rango/post_report.html', {'form': form}) 


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
        context_dict['pageheading'] = area
        context_dict['munros'] = munros
        context_dict['area'] = area
    except Area.DoesNotExist:
        context_dict['pageheading'] = None 
        context_dict['area'] = None
        context_dict['munros'] = None

    current_user = request.user
    if request.user.is_authenticated:
        try:
            userlikearea = UserLikeArea.objects.get(area = area , user = current_user)
            context_dict['userlikearea'] = userlikearea
        except UserLikeArea.DoesNotExist:
            context_dict['userlikearea'] = None

    return render(request, 'rango/area.html', context=context_dict)

def show_munro(request, munro_name_slug):
    context_dict = {}

    try:
        munro = Munro.objects.get(slug = munro_name_slug)
        images = munro.images.all()
        context_dict['pageheading'] = munro
        context_dict['munro'] = munro
        context_dict['images'] = images
    except Munro.DoesNotExist:
        context_dict['pageheading'] = None
        context_dict['munro'] = None
        context_dict['images'] = None 
    
    current_user = request.user
    if request.user.is_authenticated:
        try:
            userlikemunro = UserLikeMunro.objects.get(munro = munro , user = current_user)
            context_dict['userlikemunro'] = userlikemunro
        except UserLikeMunro.DoesNotExist:
            context_dict['userlikemunro'] = None

    return render(request, 'rango/munro.html', context=context_dict)

# For searching munros in search bar
def search_munros(request):

    if request.method == "POST":

        # Filter munro model for what was searched
        searched = request.POST['searched']
        munros = Munro.objects.filter(name__contains=searched)

        return render(request, 'rango/search_munros.html', {'searched':searched, 'munros': munros})
    
    else:
        return render(request, 'rango/search_munros.html', {})

# URL tracking view - to keep track of clicks
def goto_url(request):
    if request.method == 'GET':
        page_name = request.GET.get('page_name')
        try:
            selected_page = Munro.objects.get(slug=page_name)
            url = '/rango/munros/' + selected_page.slug
        except Munro.DoesNotExist:
            try:
                selected_page = Area.objects.get(slug=page_name)
                url = '/rango/area/' + selected_page.slug
            except Area.DoesNotExist:
                return redirect(reverse('rango:index'))
        
        print(selected_page)
        selected_page.views = selected_page.views + 1
        
        selected_page.save()
        
        return redirect(url)
    else:
        return redirect(reverse('rango:index')) 

class UserLikesArea(View):
    #Only can like area if logged in
    @method_decorator(login_required)
    def get(self, request):

        area_slug = request.GET['area_slug']
        user_name = request.GET['user_name']
        like_unlike = request.GET['like_unlike']
        
        try:
            area = Area.objects.get(slug=area_slug)
        except Area.DoesNotExist:
            return None

        try:
            user = User.objects.get(username=user_name)
        except User.DoesNotExist:
            return None

        try:
            user_likes_area = UserLikeArea.objects.get_or_create(area = area, user = user)[0]
        except UserLikeArea.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)

        if like_unlike == 'like':
            user_likes_area.has_liked = True
        else:
            user_likes_area.has_liked = False

        user_likes_area.save()

        return HttpResponse(user_likes_area.has_liked)

class UserLikesMunro(View):
    #Only can like area if logged in
    @method_decorator(login_required)
    def get(self, request):

        munro_slug = request.GET['munro_slug']
        user_name = request.GET['user_name']
        like_unlike = request.GET['like_unlike']

        try:
            munro = Munro.objects.get(slug=munro_slug)
        except Munro.DoesNotExist:
            return None

        try:
            user = User.objects.get(username=user_name)
        except User.DoesNotExist:
            return None

        try:
            user_likes_munro = UserLikeMunro.objects.get_or_create(munro = munro, user = user)[0]
        except UserLikeMunro.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)

        if like_unlike == 'like':
            user_likes_munro.has_liked = True
        else:
            user_likes_munro.has_liked = False

        user_likes_munro.save()

        return HttpResponse(user_likes_munro.has_liked)

class LikeAreaView(View):
    #Only can like area if logged in
    @method_decorator(login_required)
    def get(self, request):
        area_slug = request.GET['area_slug']
        like_unlike = request.GET['like_unlike']

        try:
            area = Area.objects.get(slug = area_slug)
        except Area.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)

        if like_unlike == 'like':
            area.likes = area.likes + 1
        else:
            area.likes = area.likes - 1

        area.save()

        return HttpResponse(area.likes)

class LikeMunroView(View):
    #Only can like area if logged in
    @method_decorator(login_required)
    def get(self, request):
        munro_slug = request.GET['munro_slug']
        like_unlike = request.GET['like_unlike']

        try:
            munro = Munro.objects.get(slug = munro_slug)
        except Munro.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)

        if like_unlike == 'like':
            munro.likes = munro.likes + 1
        else:
            munro.likes = munro.likes - 1

        munro.save()

        return HttpResponse(munro.likes)

# For updating profile
class ProfileView(View):
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        
        # User details and forms required for updating the user profile
        hiker_profile = Hiker.objects.get_or_create(user=user)[0]
        profile_form = HikerProfileForm({'picture': hiker_profile.picture})
        bagged_form = HikerBaggedMunrosForm({'bagged': hiker_profile.bagged})
        
        return (user, hiker_profile, profile_form, bagged_form)
    
    @method_decorator(login_required)
    def get(self, request, username):
        try:
            (user, hiker_profile, profile_form, bagged_form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('rango:index'))

        # Require munros for options selection
        munros = Munro.objects.all()
        
        context_dict = {'hiker_profile': hiker_profile,
                        'selected_user': user,
                        'profile_form': profile_form,
                        'bagged_form': bagged_form,
                        'munros': munros}
        
        return render(request, 'rango/profile.html', context_dict)
    
    @method_decorator(login_required)
    def post(self, request, username):
        try:
            (user, hiker_profile, profile_form, bagged_form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('rango:index'))

         # Require munros for options selection
        munros = Munro.objects.all()
        
        # If the user chooses to update their profile picture
        if 'Update Picture' in request.POST:
            profile_form = HikerProfileForm(request.POST, request.FILES, instance=hiker_profile)

            if profile_form.is_valid():
                profile_form.save(commit=True)
                return redirect(reverse('rango:profile', kwargs={'username': username}))
            else:
                print(profile_form.errors)

        # If the user chooses to update their bagged munros
        elif 'Update Bagged' in request.POST:
            bagged_form = HikerBaggedMunrosForm(request.POST, instance=hiker_profile)
            if bagged_form.is_valid():
                bagged_form.save(commit=True)
                return redirect(reverse('rango:profile', kwargs={'username': username}))
            else:
                print(bagged_form.errors)
        
        context_dict = {'hiker_profile': hiker_profile,
                        'selected_user': user,
                        'profile_form': profile_form,
                        'bagged_form': bagged_form,
                        'munros': munros}
        
        return render(request, 'rango/profile.html', context_dict)

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

#helper func
def get_server_side_cookie(request, cookie, default_val=None):
    val=request.session.get(cookie)
    if not val:
        val = default_val
    return val

