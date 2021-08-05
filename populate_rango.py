import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Area, Image, Munro 

def populate():

    lochaber_munros = [
        {'name' : 'Ben Nevis',
        'difficulty' : 4,
        'elevation': 1345,
        'coordinates': '56.7969° N, 5.0036° W',
        'duration' : '5 - 8 hours',
        'length' : 17,
        'description': 'Ben Nevis is the highest mountain of the British Isles. It is situated in the Highland council area, Scotland. Its summit, reaching an elevation of 4,406 feet (1,343 metres), is a plateau of about 100 acres (40 hectares), with a slight slope to the south and a sheer face to the northeast',
        }
    ]

    cairngorms_munros = [
        { 'name' : 'Ben Macdui',
        'difficulty' : 5,
        'elevation': 1309,
        'coordinates': '57.0704° N, 3.6691° W',
        'duration' : '6 - 7 hours',
        'length' : 17.5,
        'description': 'Ben Macdui is the second highest mountain in Scotland (and all of the British Isles) after Ben Nevis, and the highest in the Cairngorm Mountains and the wider Cairngorms National Park. The summit elevation is 1,309 metres. Ben Macdui lies on the southern edge of the Cairngorm plateau, on the boundary between the historic counties of Aberdeenshire and Banffshire.',
        }
    ]

    loch_lomond_munros = [
        {'name' : 'Ben Lomond',
        'difficulty' : 3,
        'elevation': 974,
        'coordinates': '56.7969° N, 5.0036° W',
        'duration' : '4.5 - 5.5 hours',
        'length' : 12,
        'description': 'Ben Lomonond is situated on the eastern shore of Loch Lomond, it is the most southerly of the Munros. Ben Lomond lies within the Ben Lomond National Memorial Park and the Loch Lomond and The Trossachs National Park, property of the National Trust for Scotland.Its accessibility from Glasgow and elsewhere in central Scotland, together with the relative ease of ascent from Rowardennan, makes it one of the most popular of all the Munros.',
        },

        {'name' : 'Ben Vane',
        'difficulty' : 3,
        'elevation': 915,
        'coordinates': '56.2499° N, 4.7817° W',
        'duration' : '4.5 - 6.5 hours',
        'length' : 11,
        'description': 'Ben Vane is situated in the southern Highlands. It is one of the Arrochar Alps and stands slightly separate from the other mountains of the group being connected on its western side to the neighbouring Beinn Ìme. Ben Vane itself just qualifies as a Munro reaching a height of 915 metresand is characterised by steep and rugged slopes which fall away to the Inveruglas Water to the east and the Allt Coiregroigan to the south.',
        }
    ]

    areas = {'Lochaber' : {'munros': lochaber_munros}, 
            'Cairngorms' : {'munros': cairngorms_munros},
            'Loch Lomond' : {'munros': loch_lomond_munros}}

    ben_nevis_images = [
        {'name' : 'Ben_Nevis_1.jpg',
        'title' : 'Ben Nevis',
        'description' : 'First Ben Nevis pic',
        },

        {'name' : 'Ben_Nevis_2.jpg',
        'title' : 'Ben Nevis',
        'description' : 'Second Ben Nevis pic',
        },

        {'name' : 'Ben_Nevis_3.jpg',
        'title' : 'Ben Nevis',
        'description' : 'Third Ben Nevis pic',
        },
    ]

    ben_macdui_images = [
        {'name' : 'Ben_Macdui_1.jpeg',
        'title' : 'Ben Macdui',
        'description' : 'First Ben Macdui pic',
        },

        {'name' : 'Ben_Macdui_2.jpg',
        'title' : 'Ben Macdui',
        'description' : 'Second Ben Macdui pic',
        },

        {'name' : 'Ben_Macdui_3.jpg',
        'title' : 'Ben Macdui',
        'description' : 'Third Ben Macdui pic',
        },
    ]


    ben_lomond_images = [
        {'name' : 'Ben_Lomond_1.jpg',
        'title' : 'Ben lomond',
        'description' : 'First Ben lomond pic',
        },

        {'name' : 'Ben_Lomond_2.jpg',
        'title' : 'Ben lomond',
        'description' : 'Second Ben lomond pic',
        },

        {'name' : 'Ben_Lomond_3.jpg',
        'title' : 'Ben lomond',
        'description' : 'Third Ben lomond pic',
        },
    ]

    ben_vane_images = [
        {'name' : 'Ben_Vane_1.jpg',
        'title' : 'Ben vane',
        'description' : 'First Ben vane pic',
        },

        {'name' : 'Ben_Vane_2.jpg',
        'title' : 'Ben vane',
        'description' : 'Second Ben vane pic',
        },

        {'name' : 'Ben_Vanes_3.jpg',
        'title' : 'Ben vane',
        'description' : 'Third Ben vane pic',
        },
    ]

    munro_images = {'Ben Nevis' : ben_nevis_images, 
        'Ben Macdui' : ben_macdui_images,
        'Ben Lomond' : ben_lomond_images,
        'Ben Vane' : ben_vane_images}

    for area, area_data in areas.items():
        a = add_area(area)
        for m in area_data['munros']:
            mun = add_munro(a, m['name'], m['difficulty'], m['elevation'], m['coordinates'], m['duration'], m['length'], m['description'])
            for munro, image_data in munro_images.items(): 
                for i in image_data:
                    add_image(i['name'], i['title'], i['description'], mun) 

    for a in Area.objects.all():
        for m in Munro.objects.filter(area=a):
            for i in Image.objects.filter(munro=m):
                print(f'- {a}: {m}: {i}')

def add_image(name, title, desc, munro):
    i = Image.objects.get_or_create(munro = munro, name = name)[0]
    i.title = title
    i.description = desc
    i.save()
    return i

def add_munro(area, name, diff, ele, coords, dur, len, desc):
    m = Munro.objects.get_or_create(area = area, name=name)[0] 
    m.difficulty = diff
    m.elevation = ele
    m.coordinates = coords
    m.duration = dur
    m.length = len
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