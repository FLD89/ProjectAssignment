from django.test import TestCase
from home.models import Project, ProjectEngineerLookup, SoftwareEngineer, SoftwareTraining


class AssignmentTestClass(TestCase):
    @classmethod
    # Sets up required data for following tests, which is temporarily added to a new test database
    def setUpTestData(cls):
        cls.software_engineer = SoftwareEngineer.objects.create(engineer_id="TST123", engineer_name="Joe Test")
        cls.software_training = SoftwareTraining.objects.create(engineer_id_id="TST123", software="Python")
        cls.software_engineer = SoftwareEngineer.objects.create(engineer_id="TST456", engineer_name="Jane Test")
        cls.software_training = SoftwareTraining.objects.create(engineer_id_id="TST456", software="Django")
        cls.software_engineer = SoftwareEngineer.objects.create(engineer_id="TST789", engineer_name="John Test")
        cls.software_training = SoftwareTraining.objects.create(engineer_id_id="TST789", software="Python")
        cls.project = Project.objects.create(project_name="Python Test Project", software="Python")
        cls.project = Project.objects.create(project_name="Django Test Project", software="Django")
        cls.project_engineer_lookup = ProjectEngineerLookup.objects.create(project_id_id="1", engineer_id_id="TST123")

# INITIAL TESTS

    def test_assignment_read_loads_successfully(self):
        response = self.client.get('/assignment_read/assignment_read/')
        self.assertEqual(response.status_code, 200)

    def test_assignment_create_loads_successfully(self):
        response = self.client.get('/project_read/assignment_create/1')
        self.assertEqual(response.status_code, 200)

    def test_assignment_update_loads_successfully(self):
        response = self.client.get('/assignment_read/assignment_update/1')
        self.assertEqual(response.status_code, 200)

# VALIDATION TESTS: PROJECT CREATE

    def test_cannot_create_assignment_if_engineer_id_does_not_exist(self):
        response = self.client.post(
            '/project_read/assignment_create/1',
            data={
                'engineer_id': "NONE",
                'project_id': "1",
            }
        )
        self.assertContains(
            response,
            "This Engineer ID does not exist",
            html=True
        )

    def test_cannot_create_assignment_if_engineer_does_not_have_training(self):
        response = self.client.post(
            '/project_read/assignment_create/1',
            data={
                'engineer_id': "TST456",
                'project_id': "1",
            }
        )
        self.assertContains(
            response,
            "Engineer TST456 does not have training in Python",
            html=True
        )

    def test_cannot_create_assignment_if_engineer_already_assigned(self):
        response = self.client.post(
            '/project_read/assignment_create/1',
            data={
                'engineer_id': "TST123",
                'project_id': "1",
            }
        )
        self.assertContains(
            response,
            "Engineer TST123 is already assigned to this project",
            html=True
        )

# VALIDATION TESTS: PROJECT UPDATE

    def test_cannot_update_assignment_if_engineer_id_does_not_exist(self):
        response = self.client.post(
            '/assignment_read/assignment_update/1',
            data={
                'engineer_id': "NONE",
                'project_id': "1",
            }
        )
        self.assertContains(
            response,
            "This Engineer ID does not exist",
            html=True
        )

    def test_cannot_update_assignment_if_engineer_does_not_have_training(self):
        response = self.client.post(
            '/assignment_read/assignment_update/1',
            data={
                'engineer_id': "TST456",
                'project_id': "1",
            }
        )
        self.assertContains(
            response,
            "Engineer TST456 does not have the required training in Python",
            html=True
        )

    def test_cannot_update_assignment_if_engineer_already_assigned(self):
        response = self.client.post(
            '/assignment_read/assignment_update/1',
            data={
                'engineer_id': "TST123",
                'project_id': "1",
            }
        )
        self.assertContains(
            response,
            "This Engineer TST123 is already assigned to project 1",
            html=True
        )

# OPERATIONAL TESTS: PROJECT READ

    def test_assignment_read_displays_engineer_detail(self):
        response = self.client.get('/assignment_read/assignment_read/')
        self.assertContains(
            response,
            "TST123",
            html=True
        )

    def test_assignment_read_displays_project_detail(self):
        response = self.client.get('/assignment_read/assignment_read/')
        self.assertContains(
            response,
            "Python Test Project",
            html=True
        )

# OPERATIONAL TESTS: PROJECT CREATE

    def test_assignment_create_shows_available_engineer(self):
        response = self.client.get('/project_read/assignment_create/1')
        # Converts HTTPResponse object to string so variable values, not names, can be compared with expected output
        response_string = response.content.decode('utf-8')
        self.assertIn(
            "TST789",
            response_string
        )

    def test_assignment_create_does_not_show_unavailable_engineer(self):
        response = self.client.get('/project_read/assignment_create/1')
        # Converts HTTPResponse object to string so variable values, not names, can be compared with expected output
        response_string = response.content.decode('utf-8')
        self.assertNotIn(
            "TST456",
            response_string
        )

    def test_new_assignment_is_created_successfully(self):
        response = self.client.get('/assignment_read/assignment_read/')
        self.assertNotContains(
            response,
            "John Test",
            html=True
        )
        self.client.post(
            '/project_read/assignment_create/1',
            data={
                'engineer_id': "TST789",
                'project_id': "1",
            }
        )
        response = self.client.get('/assignment_read/assignment_read/')
        self.assertContains(
            response,
            "John Test",
            html=True
        )

# OPERATIONAL TESTS: PROJECT UPDATE

    def test_assignment_is_updated_successfully(self):
        response = self.client.get('/assignment_read/assignment_read/')
        # Converts HTTPResponse object to string so variable values, not names, can be compared with expected output
        response_string = response.content.decode('utf-8')
        self.assertNotIn(
            "John Test",
            response_string
        )
        self.client.post(
            '/assignment_read/assignment_update/1',
            data={
                'engineer_id': "TST789",
                'project_id': "1",
            }
        )
        response = self.client.get('/assignment_read/assignment_read/')
        response_string = response.content.decode('utf-8')
        self.assertIn(
            "John Test",
            response_string
        )