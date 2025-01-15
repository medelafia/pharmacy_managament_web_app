from django.forms import ModelForm 
from .models import Client

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        classes = "form-control"
        self.fields["name"].widget.attrs.update({"class": classes, "id": "name", "placeholder": "Enter client name" })
        self.fields["email"].widget.attrs.update({"class": classes, "id": "email", "placeholder": "Enter client email"})
        self.fields["phone"].widget.attrs.update({"class": classes, "id": "phone", "placeholder": "Enter client phone number" })
