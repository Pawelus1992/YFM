from django.db import models
from django.utils  import timezone

# Create your models here.
class PageSection(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.title
    
class Opinion(models.Model):
    author = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

class TimeSlot(models.Model):
    date = models.DateField()
    time = models.TimeField()
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.date} {self.time}"

class Booking(models.Model):
    slot = models.OneToOneField(TimeSlot, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"Rezerwacja: {self.slot}"
