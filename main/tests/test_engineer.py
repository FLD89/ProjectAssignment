from django.test import TestCase
from home.models import SoftwareEngineer


class EngineerTestClass(TestCase):
    @classmethod
    # Sets up required data for following tests, which is temporarily added to a new test database
    def setUpTestData(cls):
        cls.software_engineer = SoftwareEngineer.objects.create(engineer_id="TST123", engineer_name="Joe Test")

# INITIAL TESTS

    def test_engineer_read_loads_successfully(self):
        response = self.client.get('/engineer_read/engineer_read/')
        self.assertEqual(response.status_code, 200)

    def test_engineer_create_loads_successfully(self):
        response = self.client.get('/engineer_create/engineer_create/')
        self.assertEqual(response.status_code, 200)

    def test_engineer_update_loads_successfully(self):
        response = self.client.get('/engineer_read/engineer_update/TST123')
        self.assertEqual(response.status_code, 200)

# VALIDATION TESTS

    def test_cannot_create_engineer_if_engineer_id_too_short(self):
        response = self.client.post(
            '/engineer_create/engineer_create/',
            data={
                'engineer_id': "1",
                'engineer_name': "Joe Short",
            }
        )
        self.assertContains(
            response,
            "Engineer ID is shorter than the minimum: 2 characters",
            html=True
        )

    def test_cannot_create_engineer_if_engineer_name_too_long(self):
        response = self.client.post(
            '/engineer_create/engineer_create/',
            data={
                'engineer_id': "TST456",
                'engineer_name': "Joseph Too Long Joseph Too Long Joseph Too Long Joseph Too Long Joseph Too Long Joseph Too Long Joseph Too Long Joseph Too Long",
            }
        )
        self.assertContains(
            response,
            "Engineer Name is longer than the maximum: 100 characters",
            html=True
        )

    def test_cannot_create_engineer_id_already_exists(self):
        response = self.client.post(
            '/engineer_create/engineer_create/',
            data={
                'engineer_id': "TST123",
                'engineer_name': "Joe Duplicate",
            }
        )
        self.assertContains(
            response,
            "An Engineer with ID TST123 already exists",
            html=True
        )

    def test_cannot_update_engineer_if_engineer_name_too_long(self):
        response = self.client.post(
            '/engineer_read/engineer_update/TST123',
            data={
                'engineer_name': "Joseph Too Long Joseph Too Long Joseph Too Long Joseph Too Long Joseph Too Long Joseph Too Long Joseph Too Long Joseph Too Long",
            }
        )
        self.assertContains(
            response,
            "Engineer Name is longer than the maximum: 100 characters",
            html=True
        )

# OPERATIONAL TESTS

    def test_engineer_read_displays_engineer_id_test_data(self):
        response = self.client.get('/engineer_read/engineer_read/')
        self.assertContains(
            response,
            "TST123",
            html=True
        )

    def test_engineer_read_displays_engineer_name_test_data(self):
        response = self.client.get('/engineer_read/engineer_read/')
        self.assertContains(
            response,
            "Joe Test",
            html=True
        )

    def test_new_engineer_is_created_successfully(self):
        response = self.client.get('/engineer_read/engineer_read/')
        self.assertNotContains(
            response,
            "Jane Test",
            html=True
        )
        self.client.post(
            '/engineer_create/engineer_create/',
            data={
                'engineer_id': "TST456",
                'engineer_name': "Jane Test",
            }
        )
        response = self.client.get('/engineer_read/engineer_read/')
        self.assertContains(
            response,
            "Jane Test",
            html=True
        )

    def test_engineer_is_updated_successfully(self):
        response = self.client.get('/engineer_read/engineer_read/')
        # Converts HTTPResponse object to string so variable values, not names, can be compared with expected output
        response_string = response.content.decode('utf-8')
        self.assertNotIn(
            "John Test",
            response_string
        )
        self.client.post(
            '/engineer_read/engineer_update/TST123',
            data={'engineer_name': "John Test"}
        )
        response = self.client.get('/engineer_read/engineer_read/')
        response_string = response.content.decode('utf-8')
        self.assertIn(
            "John Test",
            response_string
        )
