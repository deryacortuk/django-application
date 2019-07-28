from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title =models.TextField()
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    article_image=models.FileField(blank=True,null =True,verbose_name="Article add")
    def __str__(self):
        return self.title
    class Meta:
        ordering =['-created_date']  
class Comment(models.Model):
    article =models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="article",related_name="comments")
    comment_author = models.TextField( verbose_name="name")
    comment_content = models.TextField (verbose_name="comment")
    comment_date =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']
    


    





