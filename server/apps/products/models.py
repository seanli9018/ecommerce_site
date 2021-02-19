from django.db import models
from django.contrib.auth import get_user_model
from shortuuidfield import ShortUUIDField

ECUser = get_user_model()


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50)
    telephone = models.CharField(max_length=10)
    website = models.URLField(max_length=50, blank=True)
    logo = models.URLField(default='')
    description = models.CharField(max_length=200, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(ECUser, on_delete=models.SET_DEFAULT, default='V7ohnHG8s2WphFj978pyRr', related_name='brands')

    class Meta:
        db_table = 'brand_info'
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, blank=True)

    class Meta:
        db_table = 'category_info'
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class ItemAttributeKey(models.Model):
    attribute_key = models.CharField(max_length=20)

    class Meta:
        db_table = 'item_attrs_keys'


class ItemAttributeValue(models.Model):
    attribute_value = models.CharField(max_length=20)
    attribute_key = models.ForeignKey(ItemAttributeKey, on_delete=models.CASCADE, related_name='attribute_values')

    class Meta:
        db_table = 'item_attrs_values'


class Product(models.Model):
    uid = ShortUUIDField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_DEFAULT, default=0)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(ECUser, on_delete=models.SET_DEFAULT, default='V7ohnHG8s2WphFj978pyRr', related_name='products')
    description = models.TextField()

    class Meta:
        db_table = 'product_info'
        verbose_name = 'product'
        verbose_name_plural = 'products'


class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    barcode = models.CharField(max_length=30, blank=True)
    attributes = models.ManyToManyField(ItemAttributeValue, related_name='items')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sell_price = models.DecimalField(max_digits=6, decimal_places=2)
    stock_quantity = models.PositiveSmallIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    weight = models.FloatField(null=True, blank=True)
    length = models.FloatField(null=True, blank=True)
    width = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    feature_1 = models.CharField(max_length=50)
    feature_2 = models.CharField(max_length=50, blank=True)
    feature_3 = models.CharField(max_length=50, blank=True)
    feature_4 = models.CharField(max_length=50, blank=True)
    feature_5 = models.CharField(max_length=50, blank=True)

    class Meta:
        db_table = 'item_info'
        verbose_name = 'item'
        verbose_name_plural = 'items'


class ItemPicture(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='pictures')
    description = models.CharField(max_length=20, blank=True)
    url = models.URLField(default='')
    is_master = models.BooleanField(default=0)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = 'item_pictures'
        verbose_name = 'item picture'
        verbose_name_plural = 'item picture'
        ordering = ['-order']









