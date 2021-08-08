from django.db import models

# Create your models here.
''' 班级表 '''
class Class(models.Model):
    classID = models.CharField(primary_key=True, max_length=20)
    className = models.CharField(max_length=20)

''' 学生表 '''
class Student(models.Model):
     studentID = models.CharField(primary_key=True, max_length=20)
     name = models.CharField(max_length=20)
     classID = models.CharField(max_length=20)


''' 教师表 '''
class Teacher(models.Model):
    teacherID = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=20)
    classID = models.CharField(max_length=20)
    isHeadmaster = models.BooleanField()

''' 课程表 '''
class Subject(models.Model):
    subjectID = models.IntegerField(primary_key=True)
    subjectName = models.CharField(max_length=20)
    teacherID = models.CharField(max_length=20)

''' 选课表 '''
class ChooseSub(models.Model):
    subjectID = models.CharField(max_length=20)
    studentID = models.CharField(max_length=20)
    isChoose = models.BooleanField()

''' 成绩表 '''
class Score(models.Model):
    studentID = models.CharField(max_length=20)
    subjectID = models.IntegerField()
    classID = models.CharField(max_length=20)
    score = models.FloatField(max_length=3, default=0)

''' 登录账号表 '''
class User(models.Model):
    account = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    sex = models.BooleanField()
    birthday = models.DateField(auto_now_add=True)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=50)
    roleID = models.IntegerField()


