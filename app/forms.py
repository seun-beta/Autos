from django.forms import ModelForm
from app.models import Make

class MakeForm(ModelForm):
    class Meta:
        model = Make
        fields = '__all__'
