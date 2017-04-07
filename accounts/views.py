from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User

def sign_up(request):
	if request.method == "POST":
		try:
			username = request.POST['username']
			password = request.POST['password']
			email = request.POST['email']
			first_name = request.POST['first_name']
			last_name = request.POST['last_name']
			user = User.objects.create_user(username, email, password)
			user.first_name = first_name
			user.last_name = last_name
			user.save()
			user = authenticate(username=username, password=password)
			if user is not None:
				auth_login(request, user)
			else:
				render(request, 'accounts/login.html', {'errors' : 'Não foi possível realizar o login'})
		except ValueError:
			return render(request, 'accounts/sign_up.html', {'error_message' : 'Preencha todos os campos!'})

		return HttpResponseRedirect('/home/')
	else:
		return render(request, 'accounts/sign_up.html', {})

def login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			auth_login(request, user)
			return HttpResponseRedirect('/home/')
		else:
			return render(request, 'accounts/login.html', {'errors' : 'Login e/ou Senha inválido.'})

	else:
		if request.user.is_authenticated():
			return HttpResponseRedirect('/home/')
		else:
			return render(request, 'accounts/login.html', {})

	

def logout(request):
	auth_logout(request)
	return HttpResponseRedirect('/')