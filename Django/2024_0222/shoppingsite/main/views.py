from django.shortcuts import render
from product.data import product_database

def index(request):

    # product_list를 sell_count에 따라 내림차순 정렬
    sorted_product_list = sorted(product_database, key=lambda x: x['sell_count'], reverse=True)
    
    # 상위 6개 상품만 선택
    top_selling_products = sorted_product_list[:6]

    # 정렬된 상품 리스트를 템플릿에 전달
    context = {'product_list': top_selling_products}
    return render(request, "main/index.html", context)


def about(request):
    return render(request, "main/about.html")