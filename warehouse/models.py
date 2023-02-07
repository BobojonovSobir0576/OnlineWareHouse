from django.db import models

class ProductBarcode(models.Model):
    name_product = models.CharField(max_length=150)
    barcode = models.CharField(max_length=150)
    warehouse = models.CharField(max_length=150)
    cryer = models.CharField(max_length=150)
    party = models.IntegerField()
    unit_of_measure = models.CharField(max_length=150)
    number_of_entries  = models.IntegerField()
    number_remaining_stack = models.IntegerField()
    input_price = models.IntegerField()
    sale_price = models.IntegerField()
    total_income_amount = models.IntegerField()
    delivery_date = models.CharField(max_length=150)
    other_costs = models.CharField(max_length=150)
    comment_amount = models.IntegerField()
    commodity_cost = models.IntegerField()
    amount = models.IntegerField(default = 0,null=True,blank=True)
    
class Scanproduct(models.Model):
    name_product = models.CharField(max_length=150)
    barcode = models.CharField(max_length=150)
    amount = models.IntegerField(default = 1,null=True,blank=True)
    def __str__(self):
        return self.name_product