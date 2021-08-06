from django.test import TestCase
from rango.models import Munro, Area
from django.urls import reverse

#helper to create area
def add_area(name, views = 0, likes = 0):
    area = Area.objects.get_or_create(name=name)[0]
    area.views = views
    area.likes = likes

    area.save()
    return area

#tests associated with munro pages/ objects
class MunroTests(TestCase):

    #test to ensure views aren't negative
    def test_ensure_munro_views_positive(self):
        area = add_area("test", 1, 1)
        munro = Munro (name='test', views = -1, area = area)
        munro.save()
        self.assertEqual((munro.views >= 0), True)

    #test to ensure likes aren't negative
    def test_ensure_munro_likes_positive(self):
        area = add_area("test", 1, 1)
        munro = Munro (name='test', likes = -1, area = area)
        munro.save()
        self.assertEqual((munro.likes >= 0), True)

    #test to ensure slugify has worked
    def test_ensure_munro_slug_creation(self):
        area = add_area("test", 1, 1)
        munro = Munro (name='Test Munro Name', area = area)
        munro.save()
        self.assertEqual(munro.slug, 'test-munro-name')

#tests to ensure area objects are valied
class AreaTests(TestCase):

    #test to ensure area views positive
    def test_ensure_area_views_positive(self):
        area = add_area("test", 1, 1)
        self.assertEqual((area.views >= 0), True)

    #test to ensure area likes positive
    def test_ensure_area_likes_positive(self):
        area = add_area("test", 1, 1)
        self.assertEqual((area.likes >= 0), True)

    #test to ensure area slug valid
    def test_ensure_area_slug_creation(self):
        area = add_area("Test Area Slug 1", 1, 1)
        self.assertEqual(area.slug, 'test-area-slug-1')

#methods to check the homepage(index) is valid 
class IndexViewTests(TestCase): 

    #ensure that if no areas exist the sites displays approp. message
    def test_index_view_with_no_areas(self):
        response = self.client.get(reverse('rango:index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no areas present.')
        self.assertQuerysetEqual(response.context['areas'], [])

    #ensure that if areas exist, index is correct
    def test_index_view_with_areas(self):

        add_area("test area 1" , 1, 1 )
        add_area("test area 2" , 1, 1 )
        add_area("test area 3" , 1, 1 )

        response = self.client.get(reverse('rango:index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test area 1')
        self.assertContains(response, 'test area 2')
        self.assertContains(response, 'test area 3')

        num_area = len(response.context['areas'])
        self.assertEquals(num_area, 3)

