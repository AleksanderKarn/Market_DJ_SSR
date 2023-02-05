from django import forms

from products.models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

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


#def _chek(product_id):
#    a = Version.objects.get(product_id=product_id).filter(status_version=True)
#    return len(a)

class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

   # def clean_product_id(self):
   #     product_id = self.cleaned_data['product_id']
   #     return product_id
#
   # def clean_status_version(self):
   #     status_version = self.cleaned_data['status_version']
#
   #     if status_version is True:
   #         res = self.clean_product_id()
   #         if _chek(res) > 0:
   #             raise forms.ValidationError('Ошибка')
#
   #     return status_version
#


