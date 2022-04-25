from cProfile import label
from django import forms
from .models import Maudio,Mvideo

class Aform(forms.ModelForm):
	"""Form definition for Af"""

	class Meta:
		"""Meta definition for Aform."""

		model = Maudio
		exclude = ('user','name','email','ondelete','onhide','like')
		labels = {'title':'','cover':'Put Your Audio Cover Here','audio':'Put Your Audio Here'}
		widgets={
			'name':forms.TextInput(attrs={'class':'form-control   text-success bg-dark border-success' , 'placeholder':'Enter Your Name'}),

			'user':forms.TextInput(attrs={'class':'form-control  text-success bg-dark border-success'}),

			'email':forms.EmailInput(attrs={'class':'form-control  text-success bg-dark border-success', 'placeholder':'Enter Your Email'}),

			'title':forms.TextInput(attrs={'class':'form-control  text-success my-2 bg-dark border-success',
			'placeholder':'Enter Audio Title'}),

			'audio':forms.FileInput(attrs={'class':'form-control file  text-success my-2 bg-dark border-success'}),

			'cover':forms.FileInput(attrs={'class':'form-control file  text-success my-2 bg-dark border-success','placeholder':'Enter Audio Title'}),
		}



class Vform(forms.ModelForm):
	"""Form definition for Af"""

	class Meta:
		"""Meta definition for Put Your Audioform."""

		model = Mvideo
		fields = ('title','cover','video')
		labels = {'title':'','video':'Put Video Here','cover':'Put Thumbnail Here '}
		widgets={

			'name':forms.TextInput(attrs={'class':'form-control   text-success bg-dark border-success' , 'placeholder':'Enter Your Name'}),

			'user':forms.TextInput(attrs={'class':'form-control  text-success bg-dark border-success'}),

			'email':forms.EmailInput(attrs={'class':'form-control  text-success bg-dark border-success', 'placeholder':'Enter Your Email'}),

			'title':forms.TextInput(attrs={'class':'form-control  text-success my-2 bg-dark border-success',
			'placeholder':'Enter Video Title'}),

			'video':forms.FileInput(attrs={'class':'form-control file  text-success my-2 bg-dark border-success'}),
			
			'cover':forms.FileInput(attrs={'class':'form-control file  text-success my-2 bg-dark border-success'}),

		}

	# def __init__(self, *args, **kwargs):
	# 		super(Vform, self).__init__(*args, **kwargs)
	# 		self.fields['cover'].required = False
# def form_valid(self, form):
# 	# form.instance.owner = self.request.user   #<------ This line will do the trick.
# 	return super().form_valid(form)		