from django.shortcuts import render, redirect
from .models import Post

#from django.template.loader import render_to_string
#from django.http import HttpResponse, JsonResponse
# from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404, HttpResponseForbidden

#def blog_test(request):
#    # request: 사용자 요청(HttpRequest)
#    # response: 서버의 응답(HttpResponse)
#    data = [
#        {"title": "Post 1", "text": "Text 1", "pk": 1},
#        {"title": "Post 2", "text": "Text 2", "pk": 2},
#        {"title": "Post 3", "text": "Text 3", "pk": 3},
#    ]
#    # return HttpResponse('hello world')
#    # return HttpResponse('<h1>hello world</h1>')
#
#    # 템플릿 태그는 아래처럼 해석되어 들어갑니다.
#    # 그렇기 때문에 css, js를 같은 폴더에서 읽어오지 못합니다.
#    # s = "<h1>{{title}}</h1><p>{{text}}</p>"
#    # return HttpResponse(
#    #     s.replace("{{title}}", data[0]["title"]).replace("{{text}}", data[0]#["text"])
#    # )
#
#    header = '<h2>hello world header</h2>'
#    main = render_to_string("blog/test.txt", {"data": data[0]})
#    footer = '<h2>hello world footer</h2>'
#    
#    '''
#
#    test.txt
#    <P>hello blog</p>
#    <P>{{data.title}}</p>
#    <P>{{data.text}}</p>
#
#    '''
#    return HttpResponse(header + main + footer)
#    
#    # return render(request, "blog_test.html")


def blog_list(request):
    blogs = Post.objects.all()
    context = {"db": blogs}
    return render(request, "blog/blog_list.html", context)


def blog_detail(request, pk):
    blog = Post.objects.get(pk=pk)
    context = {"db": blog}
    return render(request, "blog/blog_detail.html", context)


def blog_create(request, title):
    contents = f'hello world {title}'
    q = Post.objects.create(title=title, contents=contents)
    q.save()
    return redirect("blog_list")

def blog_delete(request, pk):
    q = Post.objects.get(pk=pk)
    q.delete()
    return redirect("blog_list")

def blog_test(request):
    return render(request, "blog/blog_test.html")