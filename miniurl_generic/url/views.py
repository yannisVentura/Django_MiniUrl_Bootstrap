from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.http import HttpResponseRedirect
import random
import string
from url.forms import *
from datetime import date
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.core.urlresolvers import reverse_lazy


def AccessUrl(request, code):
    """
        Increment the number of acess to the link and redirect the user to the complete url.
    """
    my_url = get_object_or_404(MiniUrl, code=code)
    my_url.nb_acces += 1
    my_url.save()
    return HttpResponseRedirect(my_url.url_complete)


def Generate():
    """
    Generate a random int between 1 and 1000
    """
    return random.randint(1, 10000)


class FAQView(TemplateView):
    """
    Redirect the user to the FAQ.
    """
    template_name = "url/faq.html"


class CreateUrlView(CreateView):
    """
    Allow user to create a new url according to the model.
    """
    model = MiniUrl
    template_name = "url/miniurl_form.html"
    fields = ['url_complete', 'pseudo']

    def form_valid(self, form):
        """
        Generate the code random code and add it to the object before saving.
        """
        self.object = form.save(commit=False)
        self.object.code = Generate()
        self.object.save()
        return super(CreateUrlView, self).form_valid(form)


class ListRedirection_view(ListView):
    """
    Display a list of all urls store in the database paginate by 10.
    """
    model = MiniUrl
    context_object_name = "liste"
    template_name = "url/liste_url.html"
    paginate_by = 10


'''
class DetailUrl(DetailView):
    """
    Redirect the user to a detail page about a specific url.
    NOT USE ACTUALLY
    """
    model = MiniUrl
    context_object_name = "my_url"
    template_name = "url/detail_url.html"
'''
