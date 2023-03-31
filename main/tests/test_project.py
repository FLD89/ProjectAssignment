from django.test import TestCase
from home.models import Project, ProjectEngineerLookup, SoftwareEngineer, SoftwareTraining


class ProjectTestClass(TestCase):
    @classmethod
    # Sets up required data for following tests, which is temporarily added to a new test database
    def setUpTestData(cls):
        cls.software_engineer = SoftwareEngineer.objects.create(engineer_id="TST123", engineer_name="Joe Test")
        cls.software_training = SoftwareTraining.objects.create(engineer_id_id="TST123", software="Python")
        cls.project = Project.objects.create(project_name="Python Test Project", software="Python")
        cls.project_engineer_lookup = ProjectEngineerLookup.objects.create(project_id_id="1", engineer_id_id="TST123")

# INITIAL TESTS

    def test_project_read_loads_successfully(self):
        response = self.client.get('/project_read/project_read/')
        self.assertEqual(response.status_code, 200)

    def test_project_create_loads_successfully(self):
        response = self.client.get('/project_create/project_create/')
        self.assertEqual(response.status_code, 200)

    def test_project_update_loads_successfully(self):
        response = self.client.get('/project_read/project_update/1')
        self.assertEqual(response.status_code, 200)

# VALIDATION TESTS: PROJECT CREATE

    def test_cannot_create_project_if_software_too_short(self):
        response = self.client.post(
            '/project_create/project_create/',
            data={
                'software': "A",
                'project_name': "Project A",
            }
        )
        self.assertContains(
            response,
            "Software is shorter than the minimum: 2 characters",
            html=True
        )

    def test_cannot_create_project_if_project_name_too_long(self):
        response = self.client.post(
            '/project_create/project_create/',
            data={
                'software': "Python",
                'project_name': "What a very very very very very very very very very very very very very very very very very very very very very long project name"
            }
        )
        self.assertContains(
            response,
            "Project Name is longer than the maximum: 100 characters",
            html=True
        )

    def test_cannot_create_project_if_duplicate_project_name(self):
        response = self.client.post(
            '/project_create/project_create/',
            data={
                'software': "Python",
                'project_name': "Python Test Project"
            }
        )
        self.assertContains(
            response,
            "There is another Project with that name",
            html=True
        )

# VALIDATION TESTS: PROJECT UPDATE

    def test_cannot_update_project_if_software_too_long(self):
        response = self.client.post(
            '/project_read/project_update/1',
            data={
                'project_id': "1",
                'software': "What a very very very very very very very very very very very very very very very very very very very very very long software name",
                'project_name': "Project Long"
            }
        )
        self.assertContains(
            response,
            "Software is longer than the maximum: 100 characters",
            html=True
        )

    def test_cannot_update_project_if_project_name_too_short(self):
        response = self.client.post(
            '/project_read/project_update/1',
            data={
                'project_id': "1",
                'software': "Python",
                'project_name': "Prj"
            }
        )
        self.assertContains(
            response,
            "Project Name is shorter than the minimum: 5 characters",
            html=True
        )

    def test_cannot_update_project_if_assigned_engineer_does_not_have_training(self):
        response = self.client.post(
            '/project_read/project_update/1',
            data={
                'project_id': "1",
                'software': "Django",
                'project': "Django Test Project",
            }
        )
        self.assertContains(
            response,
            "Engineer TST123 is already assigned to this project and does not have training in Django",
            html=True
        )

# OPERATIONAL TESTS

    def test_project_read_displays_engineer_id_test_data(self):
        response = self.client.get('/project_read/project_read/')
        self.assertContains(
            response,
            "TST123",
            html=True
        )

    def test_project_read_displays_project_name_test_data(self):
        response = self.client.get('/project_read/project_read/')
        self.assertContains(
            response,
            "Python Test Project",
            html=True
        )

    def test_new_project_is_created_successfully(self):
        response = self.client.get('/project_read/project_read/')
        self.assertNotContains(
            response,
            "JavaScript Test Project",
            html=True
        )
        self.client.post(
            '/project_create/project_create/',
            data={
                'software': "JavaScript",
                'project_name': "JavaScript Test Project",
            }
        )
        response = self.client.get('/project_read/project_read/')
        self.assertContains(
            response,
            "JavaScript Test Project",
            html=True
        )

    def test_project_software_is_updated_successfully(self):
        software_training = SoftwareTraining.objects.create(engineer_id_id="TST123", software="Django")
        software_training.save()
        response = self.client.get('/project_read/project_read/')
        self.assertNotContains(
            response,
            "Django",
            html=True
        )
        self.client.post(
            '/project_read/project_update/1',
            data={
                'project_id': "1",
                'software': "Django",
                'project_name': "Python Test Project",
            }
        )
        response = self.client.get('/project_read/project_read/')
        self.assertContains(
            response,
            "Django",
            html=True
        )

    def test_project_name_is_updated_successfully(self):
        response = self.client.get('/project_read/project_read/')
        self.assertNotContains(
            response,
            "Django Test Project",
            html=True
        )
        self.client.post(
            '/project_read/project_update/1',
            data={
                'project_id': "1",
                'software': "Python",
                'project_name': "Django Test Project",
            }
        )
        response = self.client.get('/project_read/project_read/')
        self.assertContains(
            response,
            "Django Test Project",
            html=True
        )
