from django.contrib import admin

# Register your models here.
# Taskモデルをインポート
from .models import Task

# 管理サイトへのモデルを登録
admin.site.register(Task)