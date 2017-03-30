from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View


class IndexView(View):
    template_name = 'index/index.html'

    def get(self, request):
        return render(request, self.template_name)
