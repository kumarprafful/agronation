from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy


from .forms import UserForm
from cart.models import Cart


# Create your views here.
def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			registered = True
			Cart.objects.create(user=user)
			return HttpResponseRedirect(reverse('accounts:login'))
	else:
		user_form = UserForm()

	return render(request, 'accounts/user_register.html', {'registered':registered, 'user_form':user_form })