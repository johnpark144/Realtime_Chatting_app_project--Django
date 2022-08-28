from django.db import models

class Chatting(models.Model):
    username = models.CharField(max_length=20)
    content = models.CharField(max_length=500)
    create_date = models.DateTimeField() # 날짜와 시간에 관계 = DateTimeField를 사용