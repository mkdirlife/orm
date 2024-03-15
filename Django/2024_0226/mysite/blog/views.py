from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Post
from .forms import PostForm


def blog_list(request):
    if request.GET.get("q"):
        db = Post.objects.filter(
            Q(title__contains=request.GET.get("q"))
            | Q(contents__contains=request.GET.get("q"))
        ).distinct()
        # sqlite3에서는 대소문자 구분이 안됩니다. 나중에 배울 postgresql에서는 대소문자 구분이 됩니다.
        # namefield__icontains는 대소문자를 구분하지 않고
        # namefield__contains는 대소문자를 구분합니다.
    else:
        db = Post.objects.all()
    context = {"db": db}
    return render(request, "blog/blog_list.html", context)


def blog_details(request, pk):
    db = Post.objects.get(pk=pk)
    context = {"db": db}
    return render(request, "blog/blog_details.html", context)


def blog_create(request):
    if request.method == "GET":
        print("GET으로 들어왔습니다!")
        form = (
            PostForm()
        )  # 이렇게 생성된 form은 자동으로 form을 만들어주는 기능을 가지고 있습니다.
        # 이렇게 안하면 일일이 form을 하나씩 만들어야 합니다. 이해하긴 일일이 만드는 것이 더 좋을 수도 있습니다.
        context = {"form": form}
        return render(request, "blog/blog_create.html", context)
    elif request.method == "POST":
        print("POST로 들어왔습니다!")
        print(request.POST)
        form = PostForm(request.POST, request.FILES)    # 수정
        if form.is_valid():
            # form.is_valid()를 통과하면 form.cleaned_data를 통해 데이터를 가져올 수 있습니다. form.is_valid() 이걸 안하면 form.cleaned_data 사용할 수 없습니다. 호출도 불가합니다!
            print(form)
            print(form.data)
            print(form.cleaned_data["title"])
            print(type(form))
            print(dir(form))
            """
            'add_error', 'add_initial_prefix', 'add_prefix', 'as_div', 'as_p', 'as_table', 'as_ul', 'auto_id', 'base_fields', 'changed_data', 'clean', 'cleaned_data', 'data', 'declared_fields', 'default_renderer', 'empty_permitted', 'error_class', 'errors', 'field_order', 'fields', 'files', 'full_clean', 'get_context', 'get_initial_for_field', 'has_changed', 'has_error', 'hidden_fields', 'initial', 'is_bound', 'is_multipart', 'is_valid', 'label_suffix', 'media', 'non_field_errors', 'order_fields', 'prefix', 'render', 'renderer', 'template_name', 'template_name_div', 'template_name_label', 'template_name_p', 'template_name_table', 'template_name_ul', 'use_required_attribute', 'visible_fields'
            """
            post = form.save()
            # detail 로 가야한다! 이거 때문에 post = form.save() 해준다.
            # pk=post.pk 안할거면 form.save() 만 해줘도 된다.
            #return redirect('blog_details', pk=post.pk)
            return redirect('blog_list')
        else:
            context = {
                "form": form, 
                "error": "입력이 잘못되었습니다. 알맞은 형식으로 다시 입력해주세요!"
            }
            return render(request, "blog/blog_create.html", context)


def blog_update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog_details", pk=post.pk)
    else:
        form = PostForm(instance=post)
        context = {"form": form, "pk": pk}
        return render(request, "blog/blog_update.html", context)



def blog_delete(request, pk):
    #post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
    return redirect("blog_list")
