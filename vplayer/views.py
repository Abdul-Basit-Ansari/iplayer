from unicodedata import name
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .form import Aform,Vform
from django.core.exceptions import ValidationError
from django.contrib.auth  import authenticate,  login, logout
from .models import Mvideo,Maudio,Vcomment,Acomment
from django.db.models import Q 
# Create your views here.
def index(request):

	return render(request,"index.html")

def vplayer(request):
	u = request.user
	if request.method == "GET":
		
		s = request.GET.get('search')
		
		
		if s:
			se = s.strip()
			search = se.title()
			print(search)
			user = request.user
			v= Mvideo.objects.filter( Q(title__icontains=search) | Q(name__icontains=search)& Q(ondelete=False)&Q(onhide=False))
			dic={'videos':v}	
			# print("GET")
		
			return render(request,'vplayer/index.html',dic)
	videos = Mvideo.objects.filter(onhide=False,ondelete = False).order_by('-date')
	if u.is_authenticated:
		vform=Vform(request.POST,request.FILES)
		
		vform.name =u.first_name+" "+u.last_name
		vform.email =u.email
		vform.user = request.user
		dic = {'videos':videos,'form':vform,'user':u}
		return render(request,"vplayer/index.html",dic)

	dic = {'videos':videos,'user':u}
	# print("hgretgfd")
	return render(request,"vplayer/index.html",dic)
def aplayer(request):
	u = request.user
	if request.method == "GET":
		
		s = request.GET.get('search')
		
		
		if s:
			se = s.strip()
			search = se.title()
			print(search)
			user = request.user
			a= Maudio.objects.filter( Q(title__icontains=search) | Q(name__icontains=search)& Q(ondelete=False)&Q(onhide=False))
			dic={'audios':a}	
			# print("GET")
		
			return render(request,'aplayer/index.html',dic)
	audios = Maudio.objects.filter(onhide=False,ondelete = False)
	if u.is_authenticated:
		aform=Aform(request.POST,request.FILES)
		
		aform.name =u.first_name+" "+u.last_name
		aform.email =u.email
		aform.user = request.user
		dic = {'audios':audios,'form':aform,'user':u}
		return render(request,"aplayer/index.html",dic)

	dic = {'audios':audios,'user':u}
	return render(request,"aplayer/index.html",dic)


def signup(request):
	u=request.user
	if u.is_authenticated:
		return redirect("index")
	elif not u.is_authenticated :	
		if request.method == "POST":
			fname = request.POST.get('fname')
			lname = request.POST.get('lname')
			uname = request.POST.get('uname')
			phone = request.POST.get('phone')
			email = request.POST.get('email')
			pass1 = request.POST.get('pass1')
			pass2 = request.POST.get('pass2')
			# print(fname,lname,uname,phone,email,pass1,pass2)
			if pass1 != pass2 :
				messages.error(request,"Passwords Is Diffrent")
			user = 	User.objects.create_user(uname,email,pass1)
			user.first_name = fname
			user.last_name = lname

			user.save()
			messages.success(request,"Your Account Is Created")
			return redirect("index")
	print("signup")

	dic={'user':u}
	if not u.is_authenticated:
		return redirect("index",dic)
	if u.is_authenticated:
		return redirect("index")


def ulogin(request):
	user = request.user
	if request.method == "POST":
			uname=request.POST.get('uname')
			password=request.POST.get('password')
			user=authenticate(username= uname, password=password)
			print(uname,password)
			if user is not None:
				login(request, user)
				messages.success(request, "Successfully Logged In")
				dic={'user':request.user}
				if not user.is_authenticated:
					return redirect("index",dic)
				if user.is_authenticated:
					return redirect("index")



			else:
				messages.error(request, "Invalid credentials! Please try again")
				# return redirect("home")
	
	return redirect("index")

			
		# # login(request,user)

def ulogout(request):
	user=request.user
	if user.is_authenticated:
		logout(request)
		messages.success(request, "Successly Logout..!")
	return redirect("index")


def addvideo(request):
	def form_valid(self, form):
		form.instance.owner = self.request.user   #<------ This line will do the trick.
		return super.form_valid(form)		
	u=request.user
	if  u.is_authenticated:
		if request.method == "POST":

			vform=Vform(request.POST,request.FILES)
		
			if vform.is_valid():
				u = request.user
				task_list = vform.save(commit=False)
				task_list.user = request.user
				task_list.name = u.first_name+" "+u.last_name
				task_list.email = u.email
				task_list.save()
				messages.success(request,"Video Is Post...!")
				return redirect("vplayer")


			else:
				messages.error(request,"Please Choose Valid Video.!")
				return redirect("vplayer")


def addaudio(request):
	
	u=request.user
	if u.is_authenticated:
		if request.method == "POST":

			aform=Aform(request.POST,request.FILES)

			if aform.is_valid():
				u = request.user
				task_list = aform.save(commit=False)
				task_list.user = request.user
				task_list.name = u.first_name+" "+u.last_name
				task_list.email = u.email
				task_list.save()
				messages.success(request,"Audio Is Post...!")
				return redirect("aplayer")


			else:
				messages.error(request,"Please Choose Valid Audio Or Cover...!")
				return redirect("aplayer")
		
		else:
			messages.error(request,"Some Thing Went Wrong File Is Not Uploaded")
			return redirect("aplayer")

def uprofile(request):
	if request.method == "GET":
		
		s = request.GET.get('search')
		
		
		if s:
			se = s.strip()
			search = se.title()
			print(search)
			user = request.user
			v= Mvideo.objects.filter(Q(user=user)& Q(title__icontains=search) & Q(ondelete=False))
			a= Maudio.objects.filter(Q(user=user)& Q(title__icontains=search) & Q(ondelete=False))
			dic={'videos':v,'audios':a}	
			print("GET")
		
			return render(request,'vplayer/profile.html',dic)

	user=request.user
	if user.is_authenticated:
		uvideo=Mvideo.objects.filter(user=user,ondelete=False)
		uaudio=Maudio.objects.filter(user=user,ondelete=False)
		dic ={'videos':uvideo,'audios':uaudio,'user':user}
		return render(request,'vplayer/profile.html',dic)
	else:
		return redirect('index')	

def vdelete(request,sno):
	u = request.user
	v = Mvideo.objects.get(sno=sno)
	v.ondelete = True
	v.save()
	return redirect ('uprofile')

def vhide(request,sno):

	v = Mvideo.objects.get(sno=sno)
	v.onhide = True
	v.save()
	return redirect ('uprofile')

def vunhide(request,sno):

	v = Mvideo.objects.get(sno=sno)
	v.onhide = False
	v.save()
	return redirect ('uprofile')


def adelete(request,sno):
	u = request.user
	a = Maudio.objects.get(sno=sno)
	a.ondelete = True
	a.save()
	return redirect ('uprofile')

def ahide(request,sno):
	a = Maudio.objects.get(sno=sno)
	a.onhide = True
	a.save()
	return redirect ('uprofile')

def aunhide(request,sno):
	a = Maudio.objects.get(sno=sno)
	a.onhide = False
	a.save()
	return redirect ('uprofile')



def video(request,sno):
	
		
	video=Mvideo.objects.get(sno=sno)
	comments = Vcomment.objects.filter(video=video)
	otherv=Mvideo.objects.all()
	
	dic={'video':video,'otherv':otherv,'comments':comments}
	return render(request,'vplayer/video.html',dic)	



def vcomment(request,sno):
	u= request.user
	
	if request.method=='POST':
		if u.is_authenticated:
			video = Mvideo.objects.get(sno=sno)
			user = request.user
			comment = request.POST.get('vcomment')			
			comment = Vcomment(user=user,comment=comment,video=video)
			comment.save()
			return redirect(f'/video/{sno}')
    