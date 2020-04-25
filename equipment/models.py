from django.db import models
from account.models import Account
from datetime import datetime
from random import randint
# Create your models here.
equipment_category = (
    ('CPU','CPU'),
    ('Monitor', 'MONITOR'),
    ('Printer','PRINTER'),
    ('UPS','POWER SUPPLY'),
    ('Others', 'OTHERS'),
)
equipment_status = (
    ('open','Open'),
    ('progress','Progress'),
    ('ready','Ready'),
    ('taken', 'Taken'),
)


class Equipment(models.Model):
    user = models.ForeignKey(Account, blank=False, null=False, on_delete=models.CASCADE)
    equipment_type = models.CharField(max_length=20, choices=equipment_category)
    #equipment_num = models.CharField(max_length=15)
    serial_number = models.CharField(max_length=20)
    #equipment_description = models.TextField(max_length=100, choices=equipment_category)
    station = models.CharField(max_length=20)
    user_assesment = models.TextField(max_length=100)
    current_condition = models.TextField(max_length=100)
    recommendation = models.TextField(max_length=100)
    current_location = models.CharField(max_length=50)
    delivered_by = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    status = models.CharField(max_length=10, choices=equipment_status)
    created_at = models.DateTimeField(verbose_name='when created', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="when updated", auto_now_add=True)

    @staticmethod
    def random_num():
        rand_num = str(randint(10,1000))
        return rand_num
    
    @property
    def equipment_num(self):
        myDate = datetime.now().strftime("%Y")
        #random_string = random_num
        rand_num = randint(10,1000)
        return "%s-%s-%s" % (self.equipment_type, rand_num, myDate)

    def __str__(self):
        return self.equipment_num

    
