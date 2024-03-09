from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Mission, Vision, ActivityImage, Announcement, Course, FooterLink, MenuItem, News, Event, Contact
from .serializers import (
    MissionSerializer, VisionSerializer, ActivityImageSerializer,
    AnnouncementSerializer, CourseSerializer, FooterLinkSerializer, MenuItemSerializer
)

class MissionAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.mission_url = reverse('mission-api')

    def test_get_mission_list(self):
        response = self.client.get(self.mission_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_mission(self):
        data = {'content': 'Sample mission content'}
        response = self.client.post(self.mission_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Add more tests for updating, deleting mission objects

class VisionAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vision_url = reverse('vision-api')

    def test_get_vision_list(self):
        response = self.client.get(self.vision_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_vision(self):
        data = {'content': 'Sample vision content'}
        response = self.client.post(self.vision_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Add more tests for updating, deleting vision objects

class ActivityImageAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.activity_image_url = reverse('activity-images-api')

    def test_get_activity_image_list(self):
        response = self.client.get(self.activity_image_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_activity_image(self):
        # Add logic to handle image upload in your test data
        data = {'image': 'path/to/sample/image.jpg'}
        response = self.client.post(self.activity_image_url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Add more tests for updating, deleting activity image objects

class AnnouncementViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.announcement_url = reverse('announcement-list')

    def test_get_announcement_list(self):
        response = self.client.get(self.announcement_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_announcement(self):
        data = {'text': 'Sample announcement text'}
        response = self.client.post(self.announcement_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_single_announcement(self):
        announcement = Announcement.objects.create(text='Test announcement')
        response = self.client.get(reverse('announcement-detail', args=[announcement.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_announcement(self):
        announcement = Announcement.objects.create(text='Test announcement')
        updated_data = {'text': 'Updated announcement text'}
        response = self.client.put(reverse('announcement-detail', args=[announcement.id]), updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_announcement(self):
        announcement = Announcement.objects.create(text='Test announcement')
        response = self.client.delete(reverse('announcement-detail', args=[announcement.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CourseViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.course_url = reverse('course-list')

    def test_get_course_list(self):
        response = self.client.get(self.course_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_course(self):
        data = {'title': 'Sample Course', 'description': 'Sample course description'}
        response = self.client.post(self.course_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_single_course(self):
        course = Course.objects.create(title='Test Course', description='Test course description')
        response = self.client.get(reverse('course-detail', args=[course.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_course(self):
        course = Course.objects.create(title='Test Course', description='Test course description')
        updated_data = {'title': 'Updated Course', 'description': 'Updated course description'}
        response = self.client.put(reverse('course-detail', args=[course.id]), updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_course(self):
        course = Course.objects.create(title='Test Course', description='Test course description')
        response = self.client.delete(reverse('course-detail', args=[course.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class FooterLinkViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.footer_link_url = reverse('footerlink-list')

    def test_get_footer_links(self):
        response = self.client.get(self.footer_link_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_footer_link(self):
        data = {'title': 'Sample Footer', 'items': 'Sample footer items'}
        response = self.client.post(self.footer_link_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class MenuAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_url = reverse('menu-api')

    def test_get_menu_items(self):
        response = self.client.get(self.menu_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_menu_item(self):
        data = {'name': 'Sample Menu Item', 'link': '/sample-link/'}
        response = self.client.post(self.menu_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class NewsEventAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        News.objects.create(img='news.png', title='Coding/Artificial Intelligence', dis='Notice regarding 10 days Short term course on "Coding/Artificial Intelligence"')
        Event.objects.create(text='Coding/Artificial Intelligence')

    def test_news_api(self):
        response = self.client.get(reverse('news-api'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_events_api(self):
        response = self.client.get(reverse('events-api'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ContactAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.contact_data = {
            'email': 'itgopeshwar@gmail.com',
            'address': 'Institute of Technology, Gopeshwar, Chamoli Uttarakhand-246424',
            'aicte_feedback_link': 'http://example.com/aicte-feedback',
            'helpline_number': '9389658483',
        }
        self.contact = Contact.objects.create(**self.contact_data)

    def test_get_contact_info(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['email'], self.contact_data['email'])

    def test_create_contact_info(self):
        new_contact_data = {
            'email': 'new_email@example.com',
            'address': 'New Address',
            'aicte_feedback_link': 'http://example.com/new-feedback',
            'helpline_number': '9876543210',
        }
        response = self.client.post('/contact/', new_contact_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Contact.objects.count(), 2)
        self.assertEqual(Contact.objects.last().email, new_contact_data['email'])
class TopHeaderLinkTests(TestCase):
    def test_topheader_api(self):
        url = reverse('topheader-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)