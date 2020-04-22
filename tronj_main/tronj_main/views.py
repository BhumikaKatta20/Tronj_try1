from django.shortcuts import redirect,render

def login_redirect(request):
	return redirect('index')


def index(request):
	return render(request,'index.html')
	
