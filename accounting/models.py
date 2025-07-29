from django.db import models
from django.utils import timezone

# Create your models here.


class Transaction(models.Model):
    created_at = models.DateField("создана", default=timezone.now)
    status = models.ForeignKey('Status', on_delete=models.CASCADE, verbose_name="статус")
    type = models.ForeignKey('Type', on_delete=models.CASCADE, verbose_name="тип")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="категория")
    subcategory = models.ForeignKey('SubCategory', on_delete=models.CASCADE, verbose_name="подкатегория")
    amount = models.DecimalField("сумма", max_digits=10, decimal_places=2)
    comment = models.TextField("комментарий", blank=True, default='', max_length=4096)

    class Meta:
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"

    @staticmethod
    def verbose_name_pos():
        return "Транзакции"

    def get_absolute_url(self):
        return '/'


class Status(models.Model):
    name = models.CharField(unique=True, max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    @staticmethod
    def verbose_name_pos():
        return "Статуса"

    def get_absolute_url(self):
        return '/references/'


class Type(models.Model):
    name = models.CharField("Тип", unique=True, max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


    @staticmethod
    def verbose_name_pos():
        return "Типа"

    def get_absolute_url(self):
        return '/references/'


class Category(models.Model):
    name = models.CharField(unique=True, max_length=64)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


    @staticmethod
    def verbose_name_pos():
        return "Категории"

    def get_absolute_url(self):
        return '/references/'


class SubCategory(models.Model):
    name = models.CharField(unique=True, max_length=64)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


    @staticmethod
    def verbose_name_pos():
        return "Подкатегории"

    def get_absolute_url(self):
        return '/references/'
