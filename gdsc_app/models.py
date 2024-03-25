from django.db import models

# Create your models here.


class RegisterGDSC(models.Model):
    EDUCATION_CHOICES = [
        ('Graduate', 'Graduate'),
        ('Non-Graduate', 'Non-Graduate'),
    ]

    name = models.CharField(max_length=100)
    education = models.CharField(max_length=100, choices=EDUCATION_CHOICES)
    school = models.CharField(max_length=100, blank=True, null=True)
    whatsapp_number = models.CharField(max_length=13)
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
        verbose_name = 'GDSC Registration'
        verbose_name_plural = 'Registrations'
