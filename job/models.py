from django.db import models

'''
django model field :: give us (models.Model)

- a html widget
- b validation
- c db size
'''

'''
relationships in django

'one to many -    user --> posts    '' forinkey
'many to many -  user --> groups 
'one to one -    user --> profile
'''

# Create your models here.
JOP_TYPE = (
    ("Full Time", "Full Time"),
    ("Part Time", "Part Time"),
)


def img_upload(instance, filename):
    imgname, ext = filename.split('.')
    return f'jobs/{instance.id}.{ext}'


class Job(models.Model):  # table
    title = models.CharField(max_length=104)  # column
    jop_type = models.CharField(max_length=104, choices=JOP_TYPE)
    description = models.TextField(max_length=1000)
    Published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    salary = models.DecimalField(max_digits=6, decimal_places=2, default=100.00)
    # create model first then migrate and add row the add this field that you had id = 1 use it when you run
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=img_upload)

    # location = models.CharField(max_length=104)
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
