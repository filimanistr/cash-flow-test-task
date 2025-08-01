from django import forms
from django.utils import timezone, dateformat

from config.settings import DATE_INPUT_FORMATS
from . import models


class TransactionForm(forms.ModelForm):
    created_at = forms.DateField(
        input_formats=DATE_INPUT_FORMATS,
        initial=dateformat.format(timezone.now(), 'd.m.Y'))

    class Meta:
        model = models.Transaction
        fields = '__all__'  #

    def clean(self):
        cleaned_data = super().clean()
        type = cleaned_data.get('type')
        category = cleaned_data.get('category')
        subcategory = cleaned_data.get('subcategory')

        if type and category:
            if category.type != type:
                raise forms.ValidationError("Выбранная категория не принадлежит выбранному типу.")

        if category and subcategory:
            if subcategory.category != category:
                raise forms.ValidationError("Выбранная подкатегория не принадлежит выбранной категории.")

        return cleaned_data
