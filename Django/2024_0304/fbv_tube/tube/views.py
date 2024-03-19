from django.shortcuts import render, redirect
from .models import Post, Comment, Tag, Subscription  # 추가
from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User  # 추가


def tube_list(request):
    # 검색 q가 있을 경우 title과 content에서 해당 내용이 있는지 검색
    q = request.GET.get("q", "")
    if q:
        # 쿼리를 두번 날리는 것임. 게시물이 많아지면 비효율적임. 좋은 코드 아님. 수정필요.
        posts = Post.objects.filter(title__contains=q) | Post.objects.filter(
            content__contains=q
        )
        return render(request, "tube/tube_list.html", {"posts": posts, "q": q})
    posts = Post.objects.all()
    return render(request, "tube/tube_list.html", {"posts": posts})


def tube_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    is_subscribed = False  # 구독 여부를 확인하는 변수 초기화
    if request.user.is_authenticated:
        # 현재 사용자가 이 포스트의 저자를 구독하고 있는지 확인
        is_subscribed = Subscription.objects.filter(
            subscriber=request.user, channel=post.author
        ).exists()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            author = request.user
            message = form.cleaned_data["message"]
            c = Comment.objects.create(author=author, message=message, post=post)
            c.save()
    if request.method == "GET":
        post.view_count += 1
        post.save()
    return render(
        request,
        "tube/tube_detail.html",
        {"post": post, "form": form, "is_subscribed": is_subscribed},
    )

@login_required
def tube_create(request):
    if request.method == "GET":
        # 모델이랑 연결되어 있음을 알 수 있음.
        form = PostForm()
        context = {"form": form}
        return render(request, "tube/tube_create.html", context)
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # 리다이렉트 할때 뭔가 값을 주기 위해 관습적으로 post 사용함.
            post = form.save()
            return redirect("tube_list")
        else:
            context = {"form": form}
            return render(request, "tube/tube_create.html", context)
    #else:
        #?? 왜 없을까요? get 과 post 밖에 안들어옴. 해커는 put 으로 들어올 수 있음.
        # 잘못된 접근입니다. 라고 표시해줘야 함.


@login_required
def tube_update(request, pk):
    # URL로 접근 했을때는 오류 메시지 줘야 할 수 있다.
    post = get_object_or_404(Post, pk=pk)
    # 내가 쓴 게시물만 업데이트 가능, 저자만 수정 가능
    if post.author != request.user:
        return redirect("tube_list")

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("tube_detail", pk=post.pk)
    else:
        # form 의 instance 는 post 로 전달.
        # 수정버튼 눌렀을때 새로 작성할 순 없어요. 기존 값을 보여줘야줘.
        form = PostForm(instance=post)
        context = {"form": form, "pk": pk}
        return render(request, "tube/tube_update.html", context)


@login_required
def tube_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 내가 쓴 게시물만 삭제 가능
    if post.author != request.user:
        return redirect("tube_list")

    if request.method == "POST":
        post.delete()
    return redirect("tube_list")


def tube_tag(request, tag):
    posts = Post.objects.filter(tags__name__iexact=tag)
    return render(request, "tube/tube_list.html", {"posts": posts})


def tube_comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect("tube_detail", post_pk)


@login_required
def tube_subscribe(request, post_id, user_id):
    """구독 추가 뷰"""
    user = request.user  # 현재 로그인한 사용자
    channel = get_object_or_404(User, pk=user_id)  # 구독할 채널(사용자), user_id 는 post의 author

    # 이미 구독한 경우 추가하지 않습니다.
    if Subscription.objects.filter(subscriber=user, channel=channel).exists():
        return redirect("tube_detail", pk=post_id)

    # 구독 객체 생성
    q = Subscription.objects.create(subscriber=user, channel=channel)
    q.save()

    return redirect("tube_detail", pk=post_id)



@login_required
def tube_unsubscribe(request, post_id, user_id):
    """구독 취소 뷰"""
    user = request.user  # 현재 로그인한 사용자
    channel = get_object_or_404(User, pk=user_id)  # 구독 취소할 채널(사용자)

    # 구독 객체가 존재하면 삭제합니다.
    Subscription.objects.filter(subscriber=user, channel=channel).delete()
    return redirect("tube_detail", pk=post_id)