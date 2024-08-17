from django.db import models

class GradeChoices(models.IntegerChoices):
    AA = 10,'AA'
    AB = 9, 'AB'
    BB = 8, 'BB'
    BC = 7, 'BC'
    CC = 6, 'CC'
    CD = 5, 'CD'
    DD = 4, 'DD'
    FF = 0, 'FF'
    
class SemesterSlots(models.IntegerChoices):
    pass
    