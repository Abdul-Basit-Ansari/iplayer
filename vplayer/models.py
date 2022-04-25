from email.policy import default
from pyexpat import model
from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.utils.timezone import now
def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
# Create your models here.
class Mvideo(models.Model):
	"""Model definition for Mvideo."""
	sno = models.AutoField(primary_key=True)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	title = models.CharField(max_length=200)
	cover = models.ImageField(upload_to='videoscover',validators=[validate_file_extension])
	email = models.EmailField()
	video = models.FileField(upload_to='myvideos', validators=[FileExtensionValidator(allowed_extensions=['mp4','mov','wmv','avi','mkv','flv','swf','webm','f4v','swf'])])
	ondelete = models.BooleanField(default=False)
	onhide = models.BooleanField(default=False)
	date = models.DateTimeField(default=now)
	like = models.IntegerField(blank=True,null=True,default=0)


	class Meta:
		"""Meta definition for Mvideo."""

		verbose_name = 'Mvideo'
		verbose_name_plural = 'Videos'

	def __str__(self):
		"""Unicode representation of Mvideo."""
		return self.user.username + self.title

class Maudio(models.Model):
	"""Model definition for Maudio."""
	sno = models.AutoField(primary_key=True)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	title = models.CharField(max_length=200)
	email = models.EmailField()
	audio = models.FileField(upload_to='myaudio', validators=[FileExtensionValidator(allowed_extensions=['mp3','ogg','wav'])])
	cover = models.ImageField(upload_to='mycover',validators=[validate_file_extension])
	ondelete = models.BooleanField(default=False)
	onhide = models.BooleanField(default=False)
	date = models.DateTimeField(auto_now_add=True)
	like = models.IntegerField(blank=True,null=True,default=0)

	class Meta:
		"""Meta definition for Maudio."""

		verbose_name = 'Maudio'
		verbose_name_plural = 'Audios'

	def __str__(self):
		"""Unicode representation of Maudio."""
		return self.name



class Vcomment(models.Model):

	sno = models.AutoField(primary_key=True)
	comment = models.TextField()
	user = models.ForeignKey(User , on_delete=models.CASCADE)
	video = models.ForeignKey(Mvideo , on_delete=models.CASCADE)
	parent = models.ForeignKey('self', on_delete=models.CASCADE , null=True)
	time = models.DateTimeField(auto_now_add=True)

	# img = models.ImageField()

	def __str__(self):
		return self.comment[0:13] + "..." + "by" + " " + self.user.username


class Acomment(models.Model):

	sno = models.AutoField(primary_key=True)
	comment = models.TextField()
	user = models.ForeignKey(User , on_delete=models.CASCADE)
	audio = models.ForeignKey(Maudio , on_delete=models.CASCADE)
	parent = models.ForeignKey('self', on_delete=models.CASCADE , null=True)
	time = models.DateTimeField(auto_now_add=True)

	# img = models.ImageField()

	def __str__(self):
		return self.comment[0:13] + "..." + "by" + " " + self.user.username

