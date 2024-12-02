from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

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
    owner = models.ForeignKey(User, related_name='owner_job',on_delete=models.CASCADE)
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
    slug = models.SlugField(unique=True,blank=True, null=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)

    # we will override save to get slug
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Apply(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='apply_job')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField()
    cv = models.FileField(upload_to='applies/')
    coverletter = models.TextField(max_length=1000)

    def __str__(self):
        return self.name