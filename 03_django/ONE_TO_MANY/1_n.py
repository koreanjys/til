a = Article()
a.title = 'asdf'
a.content = 'qwer'
a.save()

c1 = Comment()
c.content = '1234'
c.article = a
c.save()

c2 = Comment.objects.create(content='4567', article=a)

c1.article == c2.article

a.article_set.all()