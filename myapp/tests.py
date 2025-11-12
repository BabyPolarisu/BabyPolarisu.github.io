from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
	def test_home_status_code_and_template(self):
		"""Root URL should return 200 and render the homepage template."""
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)
		# ensure expected content appears
		self.assertContains(response, 'Welcome to the Homepage')
