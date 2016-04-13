from django.shortcuts import render
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.models import User
from django.http import Http404,HttpResponseRedirect
from django.contrib import messages
from .models import *

def index(request):
	return render(request , 'home/index.html')

def owner_hoarding_list(request):
	return render(request, 'owner/hoarding_list.djt',{})
def owner_transaction(request):
	return render(request, 'owner/transaction.djt',{})
def upload_hoarding(request):
	lightening_type = LighteningType.objects.all()
	return render(request , 'hoarding/agency_hoarding.html',{'lightening_type':lightening_type})

def register(request):
	if request.method == 'POST':
		name = request.POST.get("name")
		email = request.POST.get("email")
		phone = request.POST.get("phone")
		password = request.POST.get("password")
		user = User.objects.create_user(username= email,email=email ,password=password)
		user.is_staff = False
		user.save()
		userprofile = UserProfile()
		userprofile.username = email
		userprofile.user_type = 'customer'
		userprofile.name = name
		userprofile.password = password
		userprofile.save()
		print name , email , phone , password
		return HttpResponseRedirect('/')
	return render(request , 'home/signup.html')

def login(request):
	name = "mani"
	print name
	if request.method == 'POST':
		print 'Welcome'
		username = request.POST.get('username')
		password = request.POST.get('password')
		print 'Welcome to login page'
		# newpassword = request.POST.get('newpassword')
		
		# if newpassword != None:
		# 	u = User.objects.get(username=username)
		# 	u.set_password(newpassword)
		# 	u.save()
		# 	print "resetpassword",u,newpassword
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				auth_login(request,user)
#				messages.info(request,"Welcome "+user.username)
				userCategory = UserProfile.objects.get(username=username).user_type
				if userCategory == 'sme':
					return HttpResponseRedirect('/')
				elif userCategory == 'owner':
					return HttpResponseRedirect('/upload')
				elif userCategory == 'transporter':
					return HttpResponseRedirect('/')
				elif userCategory == 'admin':
					return HttpResponseRedirect('/admin')
				else:
					return HttpResponseRedirect('/')
			else:
				messages.warning(request,"User is inactive. Contact manibhushan@aaho.in")
				return HttpResponseRedirect('/auth/login')
		else:
			messages.error(request,"Invalid username/password.")
			return HttpResponseRedirect('/auth/login')

def forgot(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		print username

# def register(request):
# 	if request.method == 'POST':

def logout(request):
	auth_logout(request)
	return HttpResponseRedirect('/')