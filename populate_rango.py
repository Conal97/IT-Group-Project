import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page #this must be imported after lines 1-6

def populate():

    python_pages = [
        {'title' : 'Official Python Tutorial',
        'url' : 'http://docs.python.org/3/tutorial/',
        'views': 2000},

        {'title' : 'How to Think like a Computer Scientist',
        'url' : 'http://www.greenteapress.com/thinkpython/',
        'views': 807},

        {'title' : 'Learn Python in 10 Minutes',
        'url' : 'http://www.korokithakis.net/tutorials/python/',
        'views': 600},
    ]

    django_pages = [
        {'title' : 'Official Django Tutorial',
        'url' : 'http://docs.djangoproject.com/en/2.1/intro/tuttorial01/',
        'views': 398},

        {'title' : 'Django Rocks',
        'url' : 'http://www.djangorocks.com/',
        'views': 500},

        {'title' : 'How to Tango with Django',
        'url' : 'hhtp://www.tangowithdjango.com/',
        'views': 50}
    ]

    other_pages = [
        {'title':'Bottle',
        'url':'http://bottlepy.org/docs/dev',
        'views': 123},

        {'title':'Flask',
        'url':'http://flask.pocoo.org',
        'views': 200},
    ]

    cats = {'Python' : {'pages': python_pages, 'views': 128, 'likes': 64}, 
            'Django' : {'pages': django_pages, 'views': 64, 'likes': 32},
            'Other Frameworks' : {'pages': other_pages, 'views': 32, 'likes': 16},
            }


    for cat, cat_data in cats.items():
        c = add_cat(cat, views = cat_data['views'], likes = cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], views = p['views'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name) [0]
    c.views = views
    c.likes = likes
    c.save()
    return c

if __name__=='__main__':
    print('Starting Rango Population Script...')
    populate()