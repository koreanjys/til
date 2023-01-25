a = Article()
a.title = 'asdf'
a.content = 'qwer'
a.save()

c1 = Comment()
c1.content = '1234'
c1.article = a
c1.save()

c2 = Comment.objects.create(content='4567', article=a)

c1.article == c2.article

a.comment_set.all()