from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField('タスク名', max_length=255)
    created_date = models.DateTimeField('作成日時', auto_now_add=True)
    update_date = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return self.name