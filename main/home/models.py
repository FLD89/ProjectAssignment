from django.db import models


class SoftwareEngineer(models.Model):
    engineer_id = models.CharField(max_length=20, primary_key=True)
    engineer_name = models.CharField(max_length=100)

    def __str__(self):
        return self.engineer_name


class SoftwareTraining(models.Model):
    training_id = models.AutoField(primary_key=True)
    engineer_id = models.ForeignKey(SoftwareEngineer, on_delete=models.CASCADE)
    software = models.CharField(max_length=100)

    def __str__(self):
        return f"Software: {self.software} - Engineer: {self.engineer_id}"


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    software = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)

    def __str__(self):
        return self.project_name


class ProjectEngineerLookup(models.Model):
    lookup_id = models.AutoField(primary_key=True)
    engineer_id = models.ForeignKey(SoftwareEngineer, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"Project: {self.project_id} - Engineer: {self.engineer_id}"
