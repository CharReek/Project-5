from django.db import models

# Create your models here.


class ContactModel(models.Model):
    """" customer contact form  """
    name = models.CharField(max_length=50, null=False, blank=False)
    contact_email = models.EmailField(max_length=50, null=False, blank=False)
    message = models.CharField(max_length=250)

    class Meta:
        """ verbose name"""
        verbose_name = 'Contact Form'

    def __str__(self):
        return f"{self.name} - {self.contact_email}"
