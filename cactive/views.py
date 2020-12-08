from django.views import generic


class HomePage(generic.TemplateView):
	template_name = 'home_page.html'