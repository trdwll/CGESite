from django.shortcuts import render
from django.views.generic import View
from django.db.models import Q

from .models import HomeData


class HomeView(View):
	template_name = 'home-page.html'

	def get(self, request):

		return render(request, self.template_name, {
			'homedata': HomeData.objects.get(),
		})


def handler404(request, exception, template_name='error_pages/404.html'):
	return render(request, 'error_pages/404.html', {}, status=404)

def handler500(request, exception, template_name='error_pages/500.html'):
	return render(request, 'error_pages/500.html', {}, status=500)