<<<<<<< HEAD
from django import forms
from .models import Todo

class CreateForm(forms.ModelForm):
    class Meta:
        model= Todo
=======
from django import forms
from .models import Todo

class CreateForm(forms.ModelForm):
    class Meta:
        model= Todo
>>>>>>> d508546 (first commit)
        fields = ('title','description','start_date','end_date',)