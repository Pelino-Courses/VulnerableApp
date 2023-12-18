from django.db import models

class ExampleModel(models.Model):
    name = models.CharField(max_length=255, help_text="Enter a secure name")

    def save(self, *args, **kwargs):
        
        self.name = self.name.strip()  
        super().save(*args, **kwargs)

