from django.db import models

# Create your models here.
class Account(models.Model):
    student_num = models.IntegerField(verbose_name = '학번')
    username = models.CharField(max_length=64, verbose_name = '이름')
    password = models.CharField(max_length=64, verbose_name = '비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,verbose_name='등록시간')

    def __str__(self):
        return self.username

    class Meta: #메타 클래스를 이용하여 테이블명 지정
        db_table = 'accounts'