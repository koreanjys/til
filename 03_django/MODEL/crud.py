## 모듈 불러오기

from board.models import Article

## Create (생성)

# 데이터베이스 작성하는 방법
# 1.
article = Article()
article.title = '첫번째 글'
article.content = '와 내가 처음이야'
article.author = '신주용'
article.save()

# 2.
article = Article(title='2번글', content='까비', author='김재석')
article.save()

# 3.
Article.objects.create(title='3번글', content='까비', author='김재석')
article.save()


## Read / Retrieve (조회)
# 단일 조회
article = Article.objects.get(id=1)  # id=1 혹은 pk=1도 가능
article.id
article.title
article.content
article.author

# 전체 조회
articles = Article.objects.all()
for article in articles:
    print(article.title)


## Update (수정)

article = Article.objects.get(id=1)  # 먼저 수정할 게시글을 고르고,
article.title = '수정한 글'
article.content = '바뀌어라얍'
article.save()


## Delete / Destroy (삭제)

article = Article.objects.get(id=1)
article.delete()