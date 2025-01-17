from django.forms import ModelForm , ModelMultipleChoiceField , DateField , CheckboxSelectMultiple
from .models import Medicine , Client , Sale

class MedicineForm(ModelForm ) : 
    class Meta : 
        model = Medicine 
        fields = '__all__' 
    def __init__(self,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        classes = "form-control"
        self.fields["name"].widget.attrs.update({"class" : classes , "id" : "name" , "place-holder" : "enter the medicine name"}) 
        self.fields["category"].widget.attrs.update({"class" : classes , "id" : "category" , "place-holder" : "enter the medicine category"}) 
        self.fields["price"].widget.attrs.update({"class" : classes , "id" : "price" , "place-holder" : "enter the medicine price"}) 
        self.fields["stock"].widget.attrs.update({"class" : classes , "id" : "stock" , "place-holder" : "enter the medicine stock"}) 
        self.fields["requires_prescription"].widget.attrs.update({"class" : "form-check" , "id" : "requires_prescription" , "placeholder" : "enter the medicine requires prescription"}) 

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

class SaleForm(ModelForm) : 
    medicines = ModelMultipleChoiceField(
        queryset=Medicine.objects.all() , 
        widget=CheckboxSelectMultiple , 
        required=True 
    )
    date = DateField(required=False)
    class Meta :
        model = Sale  
        fields = '__all__'

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["medicines"].widget.attrs.update({'class' : "p-3 d-flex justify-content-between rounded border align-items-center" , "id" : "medicines"})
        self.fields["client"].widget.attrs.update({'class' : "form-select" , "id" : "client"})