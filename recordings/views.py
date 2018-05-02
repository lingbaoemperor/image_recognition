from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django import forms
from image_recognition.settings import BASE_DIR

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
				with open(BASE_DIR+'/img/'+uf.cleaned_data['img'].name,'wb') as f:
					dt = uf.cleaned_data['img'].read()
					f.write(dt)
				#跳转到结果
				return HttpResponse('ok')
		uf = UploadForm()
		return render(req,'upload.html',{'uf':uf})
	else:
		return HttpResponseRedirect('/')
