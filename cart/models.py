from django.db import models
from django.utils.timezone import datetime, now


class Cart(models.Model):
    Product_Id = models.CharField(max_length=50, default='')
    Product_Name = models.CharField(max_length=50, default='')
    Product_Category = models.CharField(max_length=50, default='')
    Product_Price = models.CharField(max_length=50, default='')
    Product_Discount = models.CharField(max_length=50, default='')
    Product_SellingPrice = models.CharField(max_length=50, default='')
    Product_ImgUrl = models.TextField(max_length=300, default='')
    Product_Status = models.CharField(max_length=50, default='')
    Product_Quantity = models.CharField(max_length=50, default='')
    Product_Description = models.TextField(max_length=300, default='')
    Pub_Date = models.DateTimeField(blank=True, default=datetime.now)
    VendorID = models.CharField(max_length=50, default='')

    def __str__(self):
        return str(self.id)


class OrderPlaced(models.Model):
    Product_Id = models.CharField(max_length=50, default='')
    Product_Name = models.CharField(max_length=50, default='')
    Product_Category = models.CharField(max_length=50, default='')
    Product_Price = models.CharField(max_length=50, default='')
    Product_Discount = models.CharField(max_length=50, default='')
    Product_SellingPrice = models.CharField(max_length=50, default='')
    Product_ImgUrl = models.TextField(max_length=300, default='')
    Product_Status = models.CharField(max_length=50, default='')
    Product_Quantity = models.CharField(max_length=50, default='')
    Product_Description = models.TextField(max_length=300, default='')
    Ordered_Date = models.DateTimeField(blank=True, default=datetime.now)
    Status = models.CharField(default='Pending', max_length=50)

    def __str__(self):
        return self.Product_Name

    @property
    def Total_Cost(self):
        return self.Product_Quantity * self.Product_SellingPrice


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=10000)
    items_total = models.CharField(max_length=5, default='')
    name = models.CharField(max_length=90)
    mobile = models.CharField(max_length=10, default='')
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    payment_id = models.CharField(max_length=100,default='Not_Paid')
    confirm = models.BooleanField(default=False)
    def __str__(self):
        return str(self.order_id)


class Payment(models.Model):
   name = models.CharField(max_length=100)
   amount = models.CharField(max_length=100)
   payment_id = models.CharField(max_length=100)
   paid = models.BooleanField(default=False)
   def __str__(self):
        return str(self.id)