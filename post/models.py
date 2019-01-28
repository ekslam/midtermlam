from django.db import models

class Post(models.Model):
    title= models.CharField(max_length=100)
    date_created = models.DateTimeField('date created')
    date_updated = models.DateTimeField('date updated')
    content = models.TextField()
    is_active = models.NullBooleanField()

    def __str__(self):
        return 'Post: {}'.format(self.title)
        
class Comment(models.Model):
    date_created = models.DateTimeField('Date Created')
    content = models.TextField()
    post = models.ForeignKey('Post', on_delete = models.CASCADE, null = True, blank = True)
