from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from demo.forms import SignUpForm
from demo.forms import DetailForm
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User
from demo.models import Detals
from django.shortcuts import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import PBKDF2PasswordHasher

# Create your views here.
def home(request):
	return HttpResponseRedirect('/basic')
def signup(request):
	args={}
	args.update(csrf(request))
	if request.method=='POST':
		email=request.POST.get('email','')
		password=request.POST.get('password','')
		hasher = PBKDF2PasswordHasher()
		passwrd = hasher.encode(password=password,salt='salt',iterations=5000)
		try:
			l=User.objects.get(username=email)
			return HttpResponse('you had choose a invalid username and password')
		except:

			
			form=SignUpForm(request.POST)
			if form.is_valid():
				user=User.objects.create_user(username=email,password=password,email=email)
				user.save()
				
				form.save()
				
				
				return render_to_response('sucess.html',args)
				#return HttpResponse(form.fields['email'])
			else:
				return HttpResponse('chu')
		
	
	args['form']=SignUpForm()
	return render_to_response('sign.html',args)
def auth_view(request):
	email=request.POST.get('username','')
	password=request.POST.get('password','')
	user=auth.authenticate(username=email,password=password)
	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/game')
	else:
		return HttpResponse('username and password is invalid')
@login_required
def game(request):
	return render_to_response('search.html',{'full_name':request.user.username},context_instance=RequestContext(request))
@login_required
def history(request):
	detail=Detals.objects.get(email=request.user.username)
	
	args={}
	args.update(csrf(request))
	if request.method=="POST":
		form=DetailForm(request.POST,instance=detail)
		if form.is_valid():
			form.save()
			u=User.objects.get(username=request.user.username)
			l=request.POST.get('password','')
			e=request.POST.get('email','')
			u.email=e
			u.username=e
			u.set_password(l)
			u.save()
			return HttpResponse('you had edit the Detals')
		else:
			return HttpResponse('the email_id you had entered is not unique or you had not filled all the field')
	args['form']=DetailForm(initial={'name':detail.name,'email':detail.email,'password':detail.password,'phone_number':detail.phone_number})
	return render_to_response('history.html',args)
@login_required
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/basic')
