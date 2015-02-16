from django.test import TestCase

from django.contrib.auth import get_user_model
from.models import entry

class blogposttest(TestCase):
	def setUp(self):
		self.user = get_user_model().objects.create(username="testuser")
	def test_create_unpublished(self):
		Entry = entry(title="Title Me", body=" ", publish=False)
		Entry.save()
		self.assertEqual(entry.objects.all().count(), 1)
		self.assertEqual(entry.objects.published().count(), 0)
		Entry.publish = True
		Entry.save()
		self.assertEqual(entry.objects.published().count(), 1)

class blogviewtests(TestCase):
	def test_feed_url(self):
		response = self.client.get('/feed/')
		self.assertIn("xml", response['Content-Type'])
		raise NotImplementedError
# Create your tests here.
