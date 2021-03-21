from django import forms
from django.forms import ModelForm
from Application.models import Product

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=20)

class SignUpForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=20)

class StoreForm(forms.Form):
    title = forms.CharField(widget=forms.HiddenInput())
    app = forms.CharField(widget=forms.HiddenInput())
    functions = forms.CharField(widget=forms.HiddenInput())


TEMPLATES_CHOICES=[
    ('online_store','Online Store'),
    ('task_manager','Task Manager'),
    ('wallpapers','Wallpapers'),
    ('ringtones', 'Ringtones'),
    ('recipe','Recipe'),
    ('inspire','Inspire'),
    ('music','Music'),
    ('fashion','Fashion'),
    ('education','Education'),
    ('news','News'),
    ('local_business','Local Business'),
    ('event','Event'),
    ('health_&_wellness','Health & Wellness'),
    ('dating','Dating'),
    ('places','Places'),
]

class TemplatesForm(forms.Form):
    wanted_template = forms.CharField(label='What template you want to crate?', widget=forms.Select(choices=TEMPLATES_CHOICES))
    app_name = forms.CharField(label='What is your website name?', max_length=50)

    def __init__(self, *args, **kwargs):
        super(TemplatesForm, self).__init__(*args, **kwargs)
        visibles = self.visible_fields()
        visibles[0].field.widget.attrs['class'] = 'custom-select mb-3'

class ProductForm(forms.Form):
    cont_banca = forms.CharField(label="Contul de Banca", max_length=16)

class ProductCreationForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'created_by', 'title', 'author', 'description', 'image', 'slug', 'price', 'in_stock', 'is_active']