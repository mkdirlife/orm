# forms.py에서 우리가 작성한 models와 forms를 연결하는 작업

from django import forms
from .models import Post

class PostForm(forms.ModelForm):  # PostForm은 여러분이 원하는 이름으로 바꿔도 됩니다. forms.Form은 기본 form입니다. 이는 추후 forms.ModelForm로 바뀌어야 합니다.
    title = forms.CharField(max_length=100)
    contents = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ["title", "contents", "main_image"]
        #fields = '__all__'