from .models import StreammingNvideo
from django import forms
class VideoForm(forms.ModelForm):
    class Meta:
        model= StreammingNvideo
        fields= ["nvideo", "nid"]
