from django.forms import ModelForm 
from .models import Medicine 

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
