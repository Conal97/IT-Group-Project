import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Area, Munro 

def populate():

    fort_william_munros = [
        {'name' : 'Ben Nevis',
        'difficulty' : 1,
        'elevation': 1345,
        'coordinates': '56.7969° N, 5.0036° W',
        'description': 'Generic description',}
    ]

    cairngorms_munros = [
        { 'name' : 'Ben Macdui',
        'difficulty' : 2,
        'elevation': 1309,
        'coordinates': '57.0704° N, 3.6691° W',
        'description': 'Generic description',}

    ]

    loch_lomond_munros = [
        {'name' : 'Ben Lomond',
        'difficulty' : 5,
        'elevation': 974,
        'coordinates': '56.7969° N, 5.0036° W',
        'description': 'Generic description',},

        {'name' : 'Ben Vane',
        'difficulty' : 4,
        'elevation': 915,
        'coordinates': '56.2499° N, 4.7817° W',
        'description': 'Generic description',}
    ]

    areas = {'Fort William' : {'munros': fort_william_munros}, 
            'Cairngorms' : {'munros': cairngorms_munros},
            'Loch Lomond' : {'munros': loch_lomond_munros}}


    for area, area_data in areas.items():
        a = add_area(area)
        for m in area_data['munros']:
            add_munro(a, m['name'], m['difficulty'], m['elevation'], m['coordinates'], m['description'])

    for a in Area.objects.all():
        for m in Munro.objects.filter(area=a):
            print(f'- {a}: {m}')

def add_munro(area, name, diff, ele, coords, desc):
    m = Munro.objects.get_or_create(area = area, name=name)[0] 
    m.difficulty = diff
    m.elevation = ele
    m.coordinates = coords
    m.description = desc
    m.save()
    return m

def add_area(name):
    a = Area.objects.get_or_create(name=name)[0]
    a.save()
    return a

if __name__=='__main__':
    print('Starting Rango Population Script...')
    populate()