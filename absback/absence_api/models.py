from django.db import models

# Create your models here.


class EtsABS(models.Model):
    '''
        Database des absences des étudiants ETS
    '''
    idStudent = models.IntegerField()
    beginABS = models.DateTimeField()
    endABS = models.DateTimeField()
    motif = models.CharField(max_length=50)
    status = models.CharField(max_length=2)


