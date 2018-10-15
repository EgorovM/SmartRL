from __future__                     import unicode_literals
from django.utils.encoding          import python_2_unicode_compatible
from django.db                      import models
from django.contrib.auth.models     import User
from django.utils 					import timezone
from django 						import forms

class Profile(models.Model):
    user      = models.OneToOneField(User)
    name      = models.CharField(max_length = 30)
    grade     = models.CharField(max_length = 30)
    telephone = models.CharField(max_length = 30)
    liras     = models.IntegerField(default = 0)
    mais      = models.IntegerField(default = 0)
    status    = models.CharField(max_length = 30, default = "pupil")
    
    photo     = models.ImageField(upload_to = "images", default = "images/default.jpg")

    def __str__(self):
        return str(self.user)

@python_2_unicode_compatible
class Post(models.Model):
	data   = models.DateTimeField('date published')
	text   = models.TextField()
	status = models.CharField(max_length = 30)
	author = models.ForeignKey(Profile)

	def __str__(self):
		return str(self.data)
