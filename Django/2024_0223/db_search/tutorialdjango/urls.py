# tutorialdjango > urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from django.conf.urls.static import static 는 static() 함수를 임포트함.
# 이 함수는 개발 환경에서 정적 파일과 미디어 파일을 제공하기 위한 URL 패턴을 생성하는데 사용됨.

# from django.conf import settings 는 Django 의 설정 변수를 임포트함.
# `setting` 모듈은 `setting.py` 파일에 정의된 모든 설정을 포함함.

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 기존의 URL패턴 리스트인 `urlpatterns` 에 미디어 파일을 제공하기 위한 URL 패턴을 추가함.

# settings.MEDIA_URL 은 사용자가 업로드한 미디어 파일을 참조할때 사용되는 URL임.
# 예를 들어 `/media/` 와 같이 설정될 수 있음.
# document_root=settings.MEDIA_ROOT 는 미디어 파일이 저장되는 서버 내의 실제 디렉토리 경로임.

# MEDIA_URL = "/media/"
# MEDIA_ROOT = BASE_DIR / "media"
# 실제 setting.py 에 위와 같은 경로가 있음.
