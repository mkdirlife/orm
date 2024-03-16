# view.py 에 정의된 함수는 애플리케이션의 view 역할을 수행
# Django 에서 view 는 웹 요청을 받아서 처리하고, 그 결과로
# 웹 응답을 반환하는 컴포넌트 이다.
# 각 뷰 함수는 특정 URL에 대한 요청을 처리하며, 데이터베이스에서
# 데이터를 조회하거나 수정하는 로직을 실행한 후 최종적으로 사용자에게
# 보여줄 HTML 페이지를 생성하여 반환힌다.
# 이 때 Django의 템플릿 시스템을 사용하여 동적으로 HTML을 생성할 수 있다.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Tag
from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required


# 사이트의 게시물 목록을 보여주는 뷰
def tube_list(request):
    # 검색 q가 있을 경우 title과 content에서 해당 내용이 있는지 검색
    # 사용자가 제출한 GET 요청의 쿼리 파라미터 중 'q'의 값을 가져온다.
    # 만약 'q' 값이 없다면 기본값으로 빈 문자열 "" 을 사용한다.
    # 이는 사용자가 검색어를 입력하여 제출했을때 검색어를 처리하기 위한 부분이다.
    q = request.GET.get("q", "")
    # 사용자가 검색어를 입력했다면
    if q:
        # Post 모델의 title 필드와 content 필드에서 검색어(q)를 포함하는 
        # 게시물을 필터링한다. | 연산자를 OR 조건을 의미하며 title 과 content
        # 중 하나라도 조건을 만족하는 게시물을 찾는다.
        posts = Post.objects.filter(title__contains=q) | Post.objects.filter(
            content__contains=q
        )
        # 검색 결과에 해당하는 게시물(posts)과 검색어 'q'를 컨텍스트로
        # tube/tube_list.html 템플릿에 전달하며 이를 렌더링한 HTML을 
        # 사용자에게 반환한다.
        return render(request, "tube/tube_list.html", {"posts": posts, "q": q})    
    # 데이터베이스에서 모든 'Post' 인스턴스를 가져온다.
    posts = Post.objects.all()
    # render 함수를 사용하여 tube/tube_list.html 템플릿을 렌더링 하고,
    # 템플릿에 posts 변수로 모든 게시물을 전달한다. 
    return render(request, "tube/tube_list.html", {"posts": posts})

# 특정 게시물의 세부 정보를 보여주는 뷰
def tube_detail(request, pk):
    # URL 에서 'pk' 값을 받아 해당하는 'Post' 인스턴스를 가져온다.
    post = Post.objects.get(pk=pk)
    # 'CommentForm' 인스턴스를 생성하여 사용자에게 댓글 입력 폼을 제공한다.
    form = CommentForm()
    # 요청 메소드가 'POST'인 경우 즉 사용자가 폼을 제출했을 때, 
    if request.method == "POST":
        # 제출된 데이터를 'CommentForm' 인스턴스에 바인딩 한다.
        form = CommentForm(request.POST)
        # form이 유효한 데이터를 포함하고 있으면
        if form.is_valid():
            # 요청한 사용자를 변수 author 에 넣고
            author = request.user
            # form 에서 'message' 를 꺼내서 변수 message 에 넣고
            message = form.cleaned_data["message"]
            # 이 변수들에 맞게 새 Comment 인스턴스를 생성하고
            c = Comment.objects.create(author=author, message=message, post=post)
            # 데이터베이스에 저장한다.
            c.save()
    return render(request, "tube/tube_detail.html", {"post": post, "form": form})

# 특정 태그가 지정된 모든 게시물을 보여주는 뷰
def tube_tag(request, tag):
    # URL에서 tag 값을 받아 해당 태그 이름을 가진 Post 인스턴스를 필터링 한다.
    posts = Post.objects.filter(tags__name__iexact=tag)
    # render 함수를 사용하여 tube/tube_list.html 템플릿을 렌더링하고, 
    # 필터링된 게시물을 posts 변수로 템플릿에 전달
    return render(request, "tube/tube_list.html", {"posts": posts})



# 게시글을 생성하는 뷰
@login_required
def tube_create(request):
    # 사용자가 폼을 제출했을 때
    if request.method == "POST":
        # request.POST 에서 제목과 내용을 가져온 후 
        title = request.POST["title"]
        content = request.POST["content"]
        # author_id를 추가
        # 현재 로그인한 사용자를 게시글의 작성자로 설정
        author = request.user
        # 새로운 게시글 객체를 데이터베이스에 생성
        post = Post.objects.create(title=title, content=content, author=author)
        # 데이터베이스에 저장.
        post.save()
        # 게시글 생성 후 사용자를 게시글 목록페이지로 리다이렉트 한다.
        return redirect("tube_list")
    # POST 요청이 아닌 경우(예: 처음 페이지에 접근했을 때)
    # 게시글 생성 폼이 담긴 HTML 페이지를 렌더링하여 보여준다.
    return render(request, "tube/tube_create.html")

# 특정 게시글을 수정하는 뷰
@login_required
def tube_update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # 권한 검사: 글쓴이와 로그인한 사용자가 다르면 목록 페이지로 리다이렉트
    if post.author != request.user:
        return redirect('tube_list')

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)  # instance=post로 기존 인스턴스를 폼에 바인딩
        if form.is_valid():
            form.save()  # 폼의 데이터로 Post 모델 인스턴스를 업데이트
            return redirect('tube_detail', pk=post.pk)  # 성공 시 상세 페이지로 리다이렉트
    else:
        form = PostForm(instance=post)  # GET 요청 시 폼을 해당 post 인스턴스로 초기화

    return render(request, 'tube/tube_update.html', {'form': form, 'post': post})

# 특정 게시글을 삭제하는 뷰
@login_required
def tube_delete(request, pk):
    # 삭제할 게시글 객체를 데이터베이스에서 조회
    post = Post.objects.get(pk=pk)
    # 내가 쓴 게시물만 삭제 가능
    # 현재 로그인한 사용자가 게시글의 작성자가 아니면 게시글 목록 
    # 페이지로 리다이렉트 한다.
    if post.author != request.user:
        return redirect("tube_list")
    # 사용자가 삭제 요청을 제출했을 때 실행
    if request.method == "POST":
        # 게시글을 데이터베이스에서 삭제
        post.delete()
    # 게시글 삭제 후, 게시글 목록 페이지로 리다이렉트 한다.
    return redirect("tube_list")




# request는 Django 뷰 함수에 전달되는 HttpRequest 객체입니다. 
# HttpRequest 객체는 현재 웹 요청에 대한 모든 정보를 담고 있으며, 
# 사용자가 서버에 보낸 데이터(예: 폼 데이터, URL 파라미터 등)를 
# 접근하는 데 사용됩니다. 
# Django에서는 클라이언트 (사용자의 웹 브라우저)로부터 서버로 전송되는 
# 모든 HTTP 요청을 처리하기 위해 이 request 객체를 사용합니다.

# request 객체의 주요 속성과 메서드:
# request.method: 현재 요청의 HTTP 메소드를 나타냅니다. 
# 예를 들어, "GET" 또는 "POST"가 될 수 있습니다.
# request.GET: GET 요청에서 URL 쿼리 문자열(query string) 파라미터에 접근하기 
# 위한 딕셔너리와 유사한 객체입니다.
# request.POST: POST 요청에서 폼 데이터에 접근하기 위한 딕셔너리와 유사한 객체입니다.
# request.FILES: 파일 업로드에 접근하기 위한 딕셔너리와 유사한 객체입니다.
# request.user: 현재 요청을 한 사용자에 대한 정보를 포함합니다. 
# Django의 인증 시스템과 통합되어, 로그인한 사용자의 인스턴스를 반환합니다.
# request.session: 현재 사용자의 세션에 접근하기 위한 방법을 제공합니다.
# request.path: 현재 요청 URL의 경로 부분을 나타냅니다.
# request.COOKIES: 요청과 함께 전송된 모든 쿠키에 접근하기 위한 딕셔너리입니다.
# request 객체는 Django가 HTTP 요청을 추상화한 방식을 제공하여, 
# 개발자가 클라이언트와 서버 간의 상호작용을 쉽게 처리할 수 있게 도와줍니다. 
# 예를 들어, tube_list 함수에서는 request 객체를 사용하지 않지만, 이 객체는 요청에
# 대한 메타데이터를 포함하고 있으며, 필요한 경우 요청의 세부 정보에 접근하는 데 
# 사용될 수 있습니다.

# GET 메소드
# GET 메소드는 서버로부터 정보를 조회하기 위해 사용된다.
# 데이터를 URL의 일부로 전송한다. 
# 예를 들어, https://example.com/search?q=query는 q라는 이름의 쿼리 파라미터에 
# query라는 값을 전달한다.
# GET 요청은 데이터를 가져오는 데 사용되므로, 데이터베이스의 상태를 변경하지 않는 
# 읽기 전용 작업에 적합하다.
# 브라우저 주소창에 URL을 입력하거나, 링크를 클릭하는 것과 같은 간단한 방법으로 
# GET 요청을 발생시킬 수 있다.

# POST 메소드
# POST 메소드는 서버에 데이터를 제출하기 위해 사용된다.
# 데이터는 요청 본문(request body)에 포함되어 전송되므로, GET 메소드보다 더 많은 
# 양의 데이터를 안전하게 전송할 수 있다.
# 사용자가 폼(form)을 작성하고 제출(submit)할 때 주로 사용된다.
# POST 요청은 서버의 상태나 데이터베이스의 데이터를 변경할 수 있으므로, 
# 데이터를 생성, 수정, 삭제하는 작업에 사용된다.

# Django에서의 사용 예시
# GET 요청: 웹 페이지나 폼을 처음 로드할 때 주로 사용된다. 
# 예를 들어, tube_update 함수에서 request.method == "GET" 조건은 사용자가 
# 특정 게시글을 수정하기 위한 폼을 요청할 때 해당 폼을 렌더링하는 데 사용된다.
# POST 요청: 사용자가 폼에 데이터를 입력하고 제출 버튼을 클릭했을 때 사용된다. 
# 예를 들어, tube_create 함수에서 request.method == "POST" 조건은 사용자가 
# 새 게시글을 생성하기 위해 폼을 제출했을 때 해당 데이터를 처리하고 게시글을 
# 데이터베이스에 저장하는 데 사용된다.
# Django 뷰에서 request.method를 확인함으로써, 뷰가 처리해야 할 요청의 
# 유형(GET 또는 POST)을 결정하고, 그에 따른 적절한 작업을 수행할 수 있다.