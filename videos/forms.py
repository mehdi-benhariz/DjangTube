from django import forms 
from .models import Video,Comment

class VideoForm(forms.ModelForm):
     class Meta:
        model =Video
        fields =['title','description','url']
      
class CommentForm(forms.ModelForm):
    class Meta :
        model = Comment
        fields =('text',)
        widgets = {
             'text':forms.TextInput(
                attrs={ 'class':'form-control',
                        'placeholder': 'text',
                        'text' :'text'
                        }  )}
      