from django import forms
from .models import Post

# 모델하고 연결할 수 있음. forms.ModelForm 이 구현해둠.
class PostForm(forms.ModelForm):    
    class Meta:
        model = Post
        fields = "__all__"


# form.save 를 작동 시킬 수 없음. ModelForm 이 자식임.
# commentform 도 modelform 으로 하는게 좋음.
# model은 잘 안 만짐. form 에 더 엄격하고 설정하고, form에서 제한을 거는게 좋음.
class CommentForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)