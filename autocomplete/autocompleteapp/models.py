from django.db import models

# ShortCuts
class Shortcuts(models.Model):
    Shortcut_id = models.BigAutoField(primary_key=True)
    Name = models.CharField(null=True, max_length=30)
    Description = models.TextField(null=True, max_length=255)
    Is_Enable =  models.IntegerField(null=True)
    Created_on = models.DateTimeField(null=True)
    Created_by = models.IntegerField(null=True)
    Updated_on = models.DateTimeField( null=True)
    Updated_by = models.IntegerField(null=True)
