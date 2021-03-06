from django.conf import settings
from django.db import models
from django.shortcuts import reverse

CATEGORY_CHOICES=(
    ('S','Shirt'),
    ('SW','Sports wear'),
    ('OW','Out wear')
)

LABEL_CHOICES=(
    ('P','Primary'),
    ('S','Secondary'),
    ('D','Danger')
)


# Create your models here.
class Item(models.Model):
    title=models.CharField(max_length=100)
    price=models.FloatField()
    discountprice=models.FloatField(blank=True,null=True)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    label=models.CharField(choices=LABEL_CHOICES,max_length=1)
    slug=models.SlugField()
    description=models.TextField()
    
    def __str__self(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:products",kwargs={
            'slug':self.slug
        }
        )


class OrderItem(models.Model):
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    pass
    def __str__self(self):
        return self.title




class Order(models.Model):
    users=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ordered=models.BooleanField(default=False)
    items=models.ManyToManyField(OrderItem)
    start_date=models.DateTimeField(auto_now_add=True)
    ordered_date=models.DateTimeField()

    pass
    def __str__self(self):
        return self.user.username