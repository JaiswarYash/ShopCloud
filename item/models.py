from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    # CharField for category name
    name = models.CharField(max_length=255)

    class Meta:
       ordering = ('name',)
       verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
# Model for an Item in the store
class Item(models.Model):
    # Foreign Key to Category model
    category = models.ForeignKey(Category, related_name='items',on_delete= models.CASCADE)    
    # Item name
    name = models.CharField(max_length=255)
    # Item description
    description = models.TextField(blank= True, null= True)
    # Item price
    price = models.FloatField()
    # Image of the item
    image= models.ImageField(upload_to='item_images', blank=True, null=True)
    # Flag for whether the item is sold
    is_sold = models.BooleanField(default= False)
    # Foreign Key to User model
    created_by = models.ForeignKey(User, related_name='items', on_delete= models.CASCADE)
    # Timestamp for when the item was created
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.name