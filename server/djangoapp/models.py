import datetime
from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='car')
    description = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.name)

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    BIKE = "Bike"
    COUPE = "Coupe"
    MINIVAN = "Mini"
    OTHER = "Other"
    PICKUP = "Pickup"
    SCOOTER = "Scooter"
    SEDAN = "Sedan"
    SPORT = "Sport"
    SUV = "SUV"
    TRUCK = "Truck"
    VAN = "Van"
    WAGON = "Wagon"

    CHOICES = [
        (BIKE, "Motor Bike"), (COUPE, "Coupe"), (MINIVAN, "Mini Van"), (PICKUP, "Pick-up Truck"), (SCOOTER, "Scooter"),
        (SEDAN, "Sedan"), (SPORT, "Sports Car"), (SUV, "SUV"), (TRUCK, "Truck"), (VAN, "Van"), (WAGON, "Wagon"), (OTHER, 'Other'),
    ]

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer = models.IntegerField()
    name = models.CharField(max_length=60)
    car_type = models.CharField(max_length=15, choices=CHOICES, default=SUV)
    year = models.DateField()

    def __str__(self):
        return str(self.name)

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
