from django.db import models

'''
django model field :: give us
- a html widget
- b validation
- c db size
'''

# Create your models here.
JOP_TYPE = (
    ("Full Time", "Full Time"),
    ("Part Time", "Part Time"),
)


class Job(models.Model):  # table
    title = models.CharField(max_length=104)  # column
    jop_type = models.CharField(max_length=104, choices=JOP_TYPE)
    description = models.TextField(max_length=1000)
    Published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    salary = models.DecimalField(max_digits=6, decimal_places=2, default=100.00)

    # location = models.CharField(max_length=104)
    # category = models.CharField(max_length=104)

    def __str__(self):
        return self.title
