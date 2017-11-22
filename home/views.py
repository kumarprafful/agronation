from django.shortcuts import render
# from .models import Team
# Create your views here.
def index(request):
	# team = Team.objects.all()
	return render(request, 'home/index.html')