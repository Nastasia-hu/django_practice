import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question

# Create your tests here.
"""
python manage.py test polls命令会查找投票应用中所有的测试程序
发现一个django.test.TestCase的子类
为测试创建一个专用的数据库
查找名字以test开头的测试方法
"""
class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        在将来发布的问卷应该返回FAlSE
        """
        time = timezone.now()+datetime.timedelta(days=1)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(),False)

    def test_was_published_recently_with_Old_question(self):
        """
        已经发布超过1天的问卷，就返回False
        """
        time = timezone.now() + datetime.timedelta(days=1,seconds=1)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        最近1天的问卷，返回True
        """
        time = timezone.now() - datetime.timedelta(hours=23,minutes=59,seconds=59)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), True)
