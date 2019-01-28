from django.forms import ModelForm
from .models import Post, Comment

class PostModelForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['id']
