from django.db import models

# Create your models here.

class NombreABSPerModulesEts(models.Model):
    '''
        Modeles des modules
    '''
    idStudent = models.IntegerField(default=0)
    mod202A = models.IntegerField(default=0)
    mod216A = models.IntegerField(default=0)
    mod214 = models.IntegerField(default=0)
    mod204 = models.IntegerField(default=0)
    messe = models.IntegerField(default=0)
    mod213 = models.IntegerField(default=0)
    mod218 = models.IntegerField(default=0)
    mod212A = models.IntegerField(default=0)
    mod209 = models.IntegerField(default=0)
    mod215 = models.IntegerField(default=0)
    mod203A = models.IntegerField(default=0)
    mod207A = models.IntegerField(default=0)
    mod222 = models.IntegerField(default=0)
    mod205 = models.IntegerField(default=0)
    mod201A = models.IntegerField(default=0)
    formationhumaine = models.IntegerField(default=0)

    class Meta:
        db_table = "nombreabspermoduleets" 

        


