from django.test import TestCase


class ViewsTestCase(TestCase):
    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/index.html')

    def test_login_view(self):
        response = self.client.get('/accounts/login')
        self.assertEqual(response.status_code, 200)

    def test_admin_view(self):

        response = self.client.get('/admin')
        self.assertEqual(response.status_code, 301)

        response = self.client.get('/admin/login/?next=/admin/')
        self.assertEqual(response.status_code, 200)
