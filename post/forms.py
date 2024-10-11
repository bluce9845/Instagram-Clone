from django import forms
from post.models import Post



class NewPostform(forms.ModelForm):
    image = forms.ImageField(required=True)
    caption = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Caption'}), required=True)
    tags =  forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Tags | Seperate with comma' }), required=True)
    
    class Meta:
        model = Post
        fields = ['image', 'caption', 'tags']