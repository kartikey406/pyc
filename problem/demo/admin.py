from django.contrib import admin
from demo.models import Detals
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.
admin.site.unregister(User)
@admin.register(User)
class UserAdmin(UserAdmin):
	def save_model(self,request,obj,form,change):
		user=request.POST.get('username','')
		password=request.POST.get('password','')
		try:
			usr=User.objects.get(id=obj.id)
			m=usr.email
			d=Detals.object.get(email=m)
			d.password=password
			d.email=email
			d.save()
			usr.save()
			obj.save()
		except:
			s=Detals.objects.create(email=user,password=password)
			s.save()
			obj.save()
@admin.register(Detals)
class ArticleAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		u=request.POST.get('email','')
		p=request.POST.get('password','')
		try:
			s=Detals.objects.get(id=obj.id)
			k=s.email
			j=User.objects.get(email=k)
			j.username=u
			j.email=u
			j.set_password(p)	
			j.save()
			obj.save()
		except:	
			s= User.objects.create_user(username=u,password=p,email=u)
			s.save()
			obj.save()
