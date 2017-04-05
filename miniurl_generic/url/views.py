from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.http import HttpResponseRedirect
import random
import string
from url.forms import *
from datetime import date
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.core.urlresolvers import reverse_lazy


def redirected_view(request, code):
    my_url = get_object_or_404(MiniUrl, code=code)
    context = {
        'mon_url': my_url,
    }
    return render(request, 'url/redirected_url.html', context)


def access_url(request, code):
    my_url = get_object_or_404(MiniUrl, code=code)
    my_url.nb_acces += 1
    my_url.save()
    return HttpResponseRedirect(my_url.url_complete)


def generer():
    return random.randint(1, 10000)


class FAQView(TemplateView):
    template_name = "url/faq.html"

class CreateUrlView(CreateView):
    model = MiniUrl
    template_name = "url/miniurl_form.html"
    fields = ['url_complete', 'pseudo']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.code = generer()
        self.object.save()
        return super(CreateUrlView, self).form_valid(form)


class ListRedirection_view(ListView):
    model = MiniUrl
    context_object_name = "liste"
    template_name = "url/liste_url.html"
    paginate_by = 10


class DetailUrl(DetailView):
    model = MiniUrl
    context_object_name = "my_url"
    template_name = "url/detail_url.html"
