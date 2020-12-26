from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime, date
# Create your models here.
class Asset(models.Model):
    Property_type = models.CharField(max_length=30)
    Property_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    Establishment_date = models.DateField("Establishment Date (mm/dd/yyy)",auto_now_add=False, auto_now=False, blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    export_to_CSV = models.BooleanField(default=False)
    def __str__(self):
       return self.Property_type
    def get_absolute_url(self):
        return reverse("Property_edit", kwargs={"id": self.id})
