from django import forms 
from .models import Video,Comment

class VideoForm(forms.ModelForm):
     class Meta:
        model =Video
        fields =['title','url','description']
        widgets = {
             'title':forms.TextInput(
                attrs={ 'class':'form-control',
                        'placeholder': 'title',
                        'title' :'title'
                        }  ),
            'url':forms.FileInput(
                attrs={ 'class':'form-control',
                        } ),
            'description':forms.TextInput(
                attrs={ 'class':'form-control',
                        'placeholder': 'description',
                        'description' :'description'
                        }  ),
                
                        
                        }
       
      
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
      