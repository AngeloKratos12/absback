from django.db import models

# Create your models here.

#FOR ETS STUDENT
#---------------------------------------------------------
class EtsStudent(models.Model):
    '''
        DB Student ETS
    '''
    name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=30)
    mat_number = models.CharField(max_length=12)
    classe = models.CharField(max_length=3)


class EtsStudentPassWord(models.Model):
    '''
        BD Pass ETS Student
    '''
    idStudent = models.IntegerField()
    studentPassWordHashed = models.CharField(max_length=15)
#-------------------//----------------------------------------


#FOR SAMIS STUDENT
#-------------------------------------------------------------
class SamisStudent(models.Model):
    '''
        DB Student ETS
    '''
    name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=30)
    mat_number = models.CharField(max_length=12)
    classe = models.CharField(max_length=3)


class SamissStudentPassWord(models.Model):
    '''
        BD Pass ETS Student
    '''
    idStudent = models.IntegerField()
    studentPassWordHashed = models.CharField(max_length=15)