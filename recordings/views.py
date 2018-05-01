from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def start_page(req):
	req.session['flag'] = "true"
	return render(req,'start.html')

def to_main_page(req):
	flag = req.session.get('flag','')
	if flag == "true":
		return render(req,'main.html')
	else:
		return HttpResponseRedirect('/')
