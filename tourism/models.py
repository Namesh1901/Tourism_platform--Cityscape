from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class TourismPlace(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='places')
    name = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.city.name})"

class Venue(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='venues')
    name = models.CharField(max_length=200)
    address = models.TextField()
    capacity = models.PositiveIntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(blank=True, null=True)
    def __str__(self):
        return f"{self.name} - {self.city.name}"

class Hotel(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hotels')
    name = models.CharField(max_length=200)
    address = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(blank=True, null=True)
    def __str__(self):
        return f"{self.name} - {self.city.name}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings')
    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings')
    place = models.ForeignKey('TourismPlace', on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    number_of_persons = models.PositiveIntegerField(default=1)
    time_of_visit = models.TimeField(null=True, blank=True)
    extra_amenities = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user.username} from {self.start_date} to {self.end_date}"
