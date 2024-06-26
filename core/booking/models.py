from django.db import models
from accounts.models import CustomerProfile, BarberProfile
# local
from .utils import Dateslotgenerator


class TimeRange(models.Model):
    DAYS_OF_WEEK = (
        (0, "Saturday"),
        (1, "Sunday"),
        (2, "Monday"),
        (3, "Tuesday"),
        (4, "Wednesday"),
        (5, "Thursday"),
        (6, "Friday"),
    )

    barber = models.ForeignKey(BarberProfile, on_delete=models.CASCADE)

    Days = models.IntegerField(
        choices=DAYS_OF_WEEK,
    )

    workstart = models.TimeField()
    workfinish = models.TimeField()
    reststart = models.TimeField()
    restfinish = models.TimeField()
    duration = models.IntegerField(
        choices=(
            (15, "15 minute"),
            (30, "30 minute"),
            (45, "45 minute"),
            (60, "60 minute"),
        )
    )
    number_timeslots = models.IntegerField(null=True, blank=True)
    

    class Meta:
        unique_together = (
            "barber",
            "Days",
        )  # you can't have multiple appointments with the same barber on the same date and timeslot.


    def __str__(self):
        day_name = self.get_Days_display()
        return " {} ".format(
            day_name,
        )

    def get_day_name(self):
        return dict(self.DAYS_OF_WEEK).get(self.Days, "Unknown")

class Booking(models.Model):
    barber = models.ForeignKey(BarberProfile, on_delete=models.CASCADE)
    date = models.DateField(choices=Dateslotgenerator())
    time = models.TimeField()
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE,)
    status = models.BooleanField(default=True)

    class Meta:
        unique_together = (
            "barber",
            "date",
            "time",
        )



    def __str__(self):
        return "{} {} {}. customer: {}".format(
            self.date, self.time, self.barber, self.customer
        )



class ExcludedDates(models.Model):
    barber = models.ForeignKey(BarberProfile, on_delete=models.CASCADE)

    date = models.DateField()

    class Meta:
        unique_together = (
            "date",
            "barber",
        )

    def __str__(self) -> str:
        return "{}".format(self.date, self.barber)
