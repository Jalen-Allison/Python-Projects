from django.db import models

# Create your models here.

class UniversityCampus(models.Model):
    campus = models.CharField(max_length=60, default="", blank=True, null=False)
    campus_id = models.IntegerField(default="", blank=True, null=False)
    state = models.CharField(max_length=60, default="", blank=True, null=False)

    # Displays the object output values in the form of a string
    def __str__(self):
        display_place = '{0.campus}: {0.state}'
        return display_place.format(self)

    # class Meta creates meta data for the UniversityClasses model
    # verbose_name_plural allows you to set the exact text you would like displayed in the browser..
    # ..and removes the plural form of the model name.
    class Meta:
        verbose_name_plural ="University Campus"