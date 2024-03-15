from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    # main_image = models.ImageField(upload_to='blog/', blank=True, null=True) # upload_to='blog/' : blog 폴더 안에 저장
    # upload 규정 만드는게 중요함.
    # 폴더 트리는 오히려 깊이가 깊을 수록 탐색하는데 시간이 적게 걸립니다.
    # 함수로 만들기도 함.
    main_image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# * blank=True는 '이 필드는 필수가 아니다'라는 내용입니다.
# * null=True는 '이 필드는 새로 생성되어도 DB 비어있어도 된다.'
# 1번게시물 - 이미지 없음
# 2번게시물 - 이미지 없음
# 3번게시물 => main_image 필드 추가, 그러면 1번게시물? 2번게시물?은 어떻게 하죠?
# -> django가 입력을 하라고 얘기를 합니다. 입력을 거기서 해줍니다.
# -> null=True를 주셔서 이전 게시물이 비어있어도 된다라고 명시해줍니다.