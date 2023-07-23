import os
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import  render, redirect
from .forms import NewUserForm, UploadFileForm
from .models import Unit
from .functions import get_level, get_percent_till_next_level, get_done_level, get_total_level
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings

class Unif:

	def __init__(self, idx, done, link, name, solutions):

		self.idx = idx
		self.done = done
		self.link = link
		self.name = name
		self.solutions = solutions

def get_fpath(unit):

	if unit.solutions in [None, '']:
		return '#'
	
	return unit.solutions.path

def index(request):

	ALGEBRA_LIST = [5, 11, 17]
	COMBINATORICS_LIST = [5, 11, 17]
	GEOMETRY_LIST = [3, 7, 11]
	NUMBERTHEORY_LIST = [3, 6, 9]

	if request.user.is_authenticated:
		algebra_done = Unit.objects.filter(user = request.user, subject = 'Algebra').exclude(solutions__in = ['', None]).count()
		combinatorics_done = Unit.objects.filter(user = request.user, subject = 'Combinatorics').exclude(solutions__in = ['', None]).count()
		geometry_done = Unit.objects.filter(user = request.user, subject = 'Geometry').exclude(solutions__in = ['', None]).count()
		numbertheory_done = Unit.objects.filter(user = request.user, subject = 'Number Theory').exclude(solutions__in = ['', None]).count()
		context = {
			"algebra_level": get_level(ALGEBRA_LIST, algebra_done),
			"algebra_percent": get_percent_till_next_level(ALGEBRA_LIST, algebra_done),
			"algebra_done": get_done_level(ALGEBRA_LIST, algebra_done),
			"algebra_total": get_total_level(ALGEBRA_LIST, algebra_done),
			"combinatorics_level": get_level(COMBINATORICS_LIST, combinatorics_done),
			"combinatorics_percent": get_percent_till_next_level(COMBINATORICS_LIST, combinatorics_done),
			"combinatorics_done": get_done_level(COMBINATORICS_LIST, combinatorics_done),
			"combinatorics_total": get_total_level(COMBINATORICS_LIST, combinatorics_done),
			"geometry_level": get_level(GEOMETRY_LIST, geometry_done),
			"geometry_percent": get_percent_till_next_level(GEOMETRY_LIST, geometry_done),
			"geometry_done": get_done_level(GEOMETRY_LIST, geometry_done),
			"geometry_total": get_total_level(GEOMETRY_LIST, geometry_done),
			"numbertheory_level": get_level(NUMBERTHEORY_LIST, numbertheory_done),
			"numbertheory_percent": get_percent_till_next_level(NUMBERTHEORY_LIST, numbertheory_done),
			"numbertheory_done": get_done_level(NUMBERTHEORY_LIST, numbertheory_done),
			"numbertheory_total": get_total_level(NUMBERTHEORY_LIST, numbertheory_done),
			"units": [Unif(unit.idx, unit.solutions not in [None, ''], os.path.join("media", os.path.relpath(unit.pdf.path, start = settings.MEDIA_ROOT)), unit.name, os.path.join("media", os.path.relpath(get_fpath(unit), start = settings.MEDIA_ROOT))) for unit in Unit.objects.filter(user = request.user)],
			"id": request.user.id,
		}
	else:
		context = dict()
	return render(request = request, template_name = "main/index.html", context = context)

def register_request(request):

	if request.method == "POST":

		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:index")
		messages.error(request, "Unsuccessful registration. Invalid information.")

	form = NewUserForm()
	return render(request = request, template_name = "main/register.html", context = {"register_form": form})

def login_request(request):

	if request.method == "POST":

		form = AuthenticationForm(request, data = request.POST)

		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username = username, password = password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:index")
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")

	form = AuthenticationForm()
	return render(request = request, template_name = "main/login.html", context = {"login_form": form})

def logout_request(request):

	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("main:")

def submit_request(request):

	if request.method == "POST":
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES["file"], request.GET["uid"])
			return HttpResponseRedirect("/")
	else:
		form = UploadFileForm()
	return render(request = request, template_name = "main/submit.html", context = {"submit_form": form})

def handle_uploaded_file(f, uid):

	unit = Unit.objects.get(idx = uid)
	unit.solutions = f
	unit.save()