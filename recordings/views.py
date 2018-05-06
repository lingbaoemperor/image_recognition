from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django import forms
from recordings.models import Recordings
import datetime as dt

# Create your views here.

class UploadForm(forms.Form):
	img = forms.FileField()

def start_page(req):
	req.session['flag'] = "true"
	return render(req,'start.html')

def to_main_page(req):
	flag = req.session.get('flag','')
	#从start页面过来
	if flag == "true":
		#上传
		if req.method == "POST":
			uf = UploadForm(req.POST,req.FILES)
			if uf.is_valid():
				#保存数据到数据库
				recording = Recordings()
				recording.img = uf.cleaned_data['img']
				recording.date = dt.datetime.now()
				
				#classfy
				#...
				recording.type = 'kind'
				recording.save()
				img = uf.cleaned_data['img'];
				print(img)
				#跳转到结果
				return render(req,'result.html',{'img':img,'result':'cat'})
		uf = UploadForm()
		return render(req,'main.html',{'uf':uf})
	else:
		return HttpResponseRedirect('/')
