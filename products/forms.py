from django import forms
from django.contrib.auth.models import User

from products.models import Product, Version, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name_product', 'description', 'image', 'unit_price', 'category_name')



    cannot_words = ['Казино', 'Криптовалюта', 'Крипта', 'Биржа', 'Дешево', 'Бесплатно', 'Обман', 'Полиция', 'Радар']

    def clean_name_product(self):
        name_product = self.cleaned_data['name_product'].title()

        for word in self.cannot_words:
            if word in name_product:
                raise forms.ValidationError(f'{word} - запрещенное слово')
        return name_product

    def clean_description(self):
        description = self.cleaned_data['description'].title()

        for word in self.cannot_words:
            if word in description:
                raise forms.ValidationError(f'{word} - запрещенное слово')
        return description




class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


