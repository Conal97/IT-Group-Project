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
        'description': 'Ben Nevis is the highest mountain of the British Isles. It is situated in the Highland council area, Scotland. Its summit, reaching an elevation of 4,406 feet (1,343 metres), is a plateau of about 100 acres (40 hectares), with a slight slope to the south and a sheer face to the northeast',
        'image_1' : 'Ben_Nevis_1.jpg',
        'image_2' : 'Ben_Nevis_2.jpg',
        'image_3' : 'Ben_Nevis_3.jpg',
        }
    ]

    cairngorms_munros = [
        { 'name' : 'Ben Macdui',
        'difficulty' : 2,
        'elevation': 1309,
        'coordinates': '57.0704° N, 3.6691° W',
        'description': 'Generic description',
        'image_1' : 'Ben_Macdui_1.jpg',
        'image_2' : 'Ben_Macdui_2.jpg',
        'image_3' : 'Ben_Macdui_3.jpg',
        }
    ]

    loch_lomond_munros = [
        {'name' : 'Ben Lomond',
        'difficulty' : 5,
        'elevation': 974,
        'coordinates': '56.7969° N, 5.0036° W',
        'description': 'Generic description',
        'image_1' : 'Ben_Lomond_1.jpg',
        'image_2' : 'Ben_Lomond_2.jpg',
        'image_3' : 'Ben_Lomond_3.jpg',
        },

        {'name' : 'Ben Vane',
        'difficulty' : 4,
        'elevation': 915,
        'coordinates': '56.2499° N, 4.7817° W',
        'description': 'Generic description',
        'image_1' : 'Ben_Vane_1.jpg',
        'image_2' : 'Ben_Vane_2.jpg',
        'image_3' : 'Ben_Vane_3.jpg',
        }
    ]

    areas = {'Fort William' : {'munros': fort_william_munros}, 
            'Cairngorms' : {'munros': cairngorms_munros},
            'Loch Lomond' : {'munros': loch_lomond_munros}}


    for area, area_data in areas.items():
        a = add_area(area)
        for m in area_data['munros']:
            add_munro(a, m['name'], m['difficulty'], m['elevation'], m['coordinates'], m['description'], m['image_1'], m['image_2'], m['image_3'])

    for a in Area.objects.all():
        for m in Munro.objects.filter(area=a):
            print(f'- {a}: {m}')

def add_munro(area, name, diff, ele, coords, desc, img1, img2, img3):
    m = Munro.objects.get_or_create(area = area, name=name)[0] 
    m.difficulty = diff
    m.elevation = ele
    m.coordinates = coords
    m.description = desc
    m.image_1 = img1
    m.image_2 = img2
    m.image_3 = img3
    m.save()
    return m

def add_area(name):
    a = Area.objects.get_or_create(name=name)[0]
    a.save()
    return a

if __name__=='__main__':
    print('Starting Rango Population Script...')
    populate()