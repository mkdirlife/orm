from django import forms
from .models import Post

# forms.py 파일은 Django 폼(forms) 클래스를 정의하는 곳이다.
# 폼클래스는 사용자 입력을 처리 하기 위한 폼을 생성하고, 이를 검증하는데 사용 한다.
# CommentForm 클래스는 사용자로부터 댓글을 입력 받기 위한 폼을 나타낸다

# 이 클래스는 Django 의 내장 클래스인 forms.Form 을 상속받아 폼과 관련된
# 기본적인 기능(필드정의, 데이터 검증 등)을 사용할 수 있게 해준다.
class CommentForm(forms.Form):
    # CharField 는 텍스트 입력을 받는 필드 유형을 나타낸다.
    # 여기서는 사용자의 댓글 메시지를 입력 받는데 사용된다.
    # widget=forms.Textarea 은 필드의 입력 위젯을 Textarea 로 지정한다.
    # 위젯은 HTML 폼에서 필드가 어떻게 렌더링될지를 결정한다.
    # <input type="text">을 사용하지만, Textarea 위젯을 사용함으로써 
    # 여러 줄의 텍스트 입력이 가능한 <textarea> 태그로 렌더링 된다.
    message = forms.CharField(widget=forms.Textarea)

class PostForm(forms.ModelForm):  # PostForm은 여러분이 원하는 이름으로 바꿔도 됩니다. forms.Form은 기본 form입니다. 이는 추후 forms.ModelForm로 바뀌어야 합니다.
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ["title", "content"]
        #fields = '__all__'