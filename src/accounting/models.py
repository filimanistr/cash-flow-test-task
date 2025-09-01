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


class Status(models.Model):
    name = models.CharField(unique=True, max_length=64)

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self):
        return self.name

    @staticmethod
    def verbose_name_pos():
        return "Статуса"


class Type(models.Model):
    name = models.CharField("Тип", unique=True, max_length=64)

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"

    def __str__(self):
        return self.name

    @staticmethod
    def verbose_name_pos():
        return "Типа"


class Category(models.Model):
    name = models.CharField(unique=True, max_length=64)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    @staticmethod
    def verbose_name_pos():
        return "Категории"


class SubCategory(models.Model):
    name = models.CharField(unique=True, max_length=64)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

    def __str__(self):
        return self.name

    @staticmethod
    def verbose_name_pos():
        return "Подкатегории"
