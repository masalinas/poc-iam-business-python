# PocOliveBusinessPython/models.py
from django.db import models

class Product(models.Model):
    code = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=512, null=True)
    price = models.FloatField(null=False)
    active = models.BooleanField(null=False, default=True)

    def __init__(self, code, description, price, active):
        super(Product, self).__init__(self)

        self.code = code
        self.description = description
        self.price = price
        self.active = active

    def __str__(self):
        return self.code

    def as_json(self):
        return dict(
            code = self.code,
            description = self.description,
            price = self.price,
            active = self.active)

    class Meta:
        db_table = 'Product'        