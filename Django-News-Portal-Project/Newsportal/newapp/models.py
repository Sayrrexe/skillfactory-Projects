from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.SmallIntegerField(default=0)
    
    def update_rating(self):
        PostRate = self.post_set.aggregate(postRating = Sum('post_rating'))
        pRat = 0
        pRat += PostRate.get('postRating')        
        
        CommentRat = self.author_user.comment_set.aggregate(CommentRating = Sum('rating'))
        cRat = 0
        cRat += CommentRat.get('CommentRating')
        
        self.author_rating = pRat * 3 + cRat
        self.save()
        
    
        
class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICEC = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')
    )
    category_type = models.CharField(max_length=2, choices=CATEGORY_CHOICEC, default=ARTICLE)
    date_creation = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through ='PostCategory')
    title = models.CharField(max_length=128)
    text = models.TextField()
    post_rating = models.SmallIntegerField(default=0)
    
    def like(self):
        self.post_rating += 1
        self.save()
        
    def dis_like(self):
        self.post_rating -= 1
        self.save()
    
    def preview(self):
        return self.text[0:20] + '...'
    
    def __str__(self):
        return f"{self.title} by {self.author.author_user.username}"

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.postThrough.title} in {self.categoryThrough.name}"

class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)
        
    def like(self):
        self.rating += 1
        self.save()
        
    def dis_like(self):
        self.rating -= 1
        self.save()
    
class Subscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )