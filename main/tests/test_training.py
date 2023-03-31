from django.test import TestCase
from home.models import Project, ProjectEngineerLookup, SoftwareEngineer, SoftwareTraining


class TrainingTestClass(TestCase):
    @classmethod
    # Sets up required data for following tests, which is temporarily added to a new test database
    def setUpTestData(cls):
        cls.software_engineer = SoftwareEngineer.objects.create(engineer_id="TST123", engineer_name="Joe Test")
        cls.software_training = SoftwareTraining.objects.create(engineer_id_id="TST123", software="Python")
        cls.software_engineer = SoftwareEngineer.objects.create(engineer_id="TST456", engineer_name="Jane Test")
        cls.software_training = SoftwareTraining.objects.create(engineer_id_id="TST456", software="Django")
        cls.project = Project.objects.create(project_name="Python Test Project", software="Python")
        cls.project_engineer_lookup = ProjectEngineerLookup.objects.create(project_id_id="1", engineer_id_id="TST123")

# INITIAL TESTS

    def test_training_read_loads_successfully(self):
        response = self.client.get('/training_read/training_read/')
        self.assertEqual(response.status_code, 200)

    def test_training_create_loads_successfully(self):
        response = self.client.get('/engineer_read/training_create/TST123')
        self.assertEqual(response.status_code, 200)

    def test_training_update_loads_successfully(self):
        response = self.client.get('/training_read/training_update/1')
        self.assertEqual(response.status_code, 200)

# VALIDATION TESTS: TRAINING CREATE

    def test_cannot_create_training_if_software_too_short(self):
        response = self.client.post(
            '/engineer_read/training_create/TST123',
            data={
                'engineer_id': "TST123",
                'software': "A",
            }
        )
        self.assertContains(
            response,
            "Software is shorter than the minimum: 2 characters",
            html=True
        )

    def test_cannot_create_training_if_software_too_long(self):
        response = self.client.post(
            '/engineer_read/training_create/TST123',
            data={
                'engineer_id': "TST123",
                'software': "What a very very very very very very very very very very very very very very very very very very very very very very very long software name",
            }
        )
        self.assertContains(
            response,
            "Software is longer than the maximum: 100 characters",
            html=True
        )

    def test_cannot_create_training_if_engineer_already_has_training(self):
        response = self.client.post(
            '/engineer_read/training_create/TST123',
            data={
                'engineer_id': "TST123",
                'software': "Python",
            }
        )
        self.assertContains(
            response,
            "This Engineer already has training in Python",
            html=True
        )

# VALIDATION TESTS: TRAINING UPDATE

    def test_cannot_update_training_if_software_too_short(self):
        response = self.client.post(
            '/training_read/training_update/1',
            data={
                'training_id': "1",
                'engineer_id': "TST123",
                'software': "A",
            }
        )
        self.assertContains(
            response,
            "Software is shorter than the minimum: 2 characters",
            html=True
        )

    def test_cannot_update_training_if_software_too_long(self):
        response = self.client.post(
            '/training_read/training_update/1',
            data={
                'training_id': "1",
                'engineer_id': "TST123",
                'software': "What a very very very very very very very very very very very very very very very very very very very very very very very long software name",
            }
        )
        self.assertContains(
            response,
            "Software is longer than the maximum: 100 characters",
            html=True
        )

    def test_cannot_update_training_if_engineer_id_does_not_exist(self):
        response = self.client.post(
            '/training_read/training_update/2',
            data={
                'training_id': "2",
                'engineer_id': "NONE",
                'software': "Django",
            }
        )
        self.assertContains(
            response,
            "This Engineer ID does not exist",
            html=True
        )

    def test_cannot_update_training_if_engineer_already_has_training(self):
        response = self.client.post(
            '/training_read/training_update/1',
            data={
                'training_id': "1",
                'engineer_id': "TST123",
                'software': "Python",
            }
        )
        self.assertContains(
            response,
            "Engineer TST123 already has training in Python",
            html=True
        )

    def test_cannot_update_training_if_engineer_requires_training_for_assigned_project(self):
        response = self.client.post(
            '/training_read/training_update/1',
            data={
                'training_id': "1",
                'engineer_id': "TST123",
                'software': "Django",
            }
        )
        self.assertContains(
            response,
            "Engineer TST123 requires Training in Python for assigned Project Python Test Project",
            html=True
        )

# OPERATIONAL TESTS: TRAINING READ

    def test_project_read_displays_engineer_detail(self):
        response = self.client.get('/training_read/training_read/')
        self.assertContains(
            response,
            "Joe Test",
            html=True
        )

    def test_assignment_read_displays_software_detail(self):
        response = self.client.get('/training_read/training_read/')
        self.assertContains(
            response,
            "Python",
            html=True
        )

# OPERATIONAL TESTS: TRAINING CREATE

    def test_assignment_create_shows_engineer_name(self):
        response = self.client.get('/engineer_read/training_create/TST123')
        # Converts HTTPResponse object to string so variable values, not names, can be compared with expected output
        response_string = response.content.decode('utf-8')
        self.assertIn(
            "Joe Test",
            response_string
        )

    def test_new_training_is_created_successfully(self):
        response = self.client.get('/training_read/training_read/')
        # Converts HTTPResponse object to string so variable values, not names, can be compared with expected output
        response_string = response.content.decode('utf-8')
        self.assertNotIn(
            "HTML",
            response_string
        )
        self.client.post(
            '/engineer_read/training_create/TST123',
            data={
                'engineer_id': "TST123",
                'software': "HTML",
            }
        )
        response = self.client.get('/training_read/training_read/')
        response_string = response.content.decode('utf-8')
        self.assertIn(
            "HTML",
            response_string
        )

# OPERATIONAL TESTS: TRAINING UPDATE

    def test_training_software_is_updated_successfully(self):
        response = self.client.get('/training_read/training_read/')
        # Converts HTTPResponse object to string so variable values, not names, can be compared with expected output
        response_string = response.content.decode('utf-8')
        self.assertNotIn(
            "JavaScript",
            response_string
        )
        self.client.post(
            '/training_read/training_update/1',
            data={
                'training_id': "1",
                'engineer_id': "TST456",
                'software': "JavaScript",
            }
        )
        response = self.client.get('/training_read/training_read/')
        response_string = response.content.decode('utf-8')
        self.assertIn(
            "JavaScript",
            response_string
        )
