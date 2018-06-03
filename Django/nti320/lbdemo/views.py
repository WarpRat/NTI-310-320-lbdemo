# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
import platform

# Create your views here.

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        node_name = platform.node()
        #node_name = "TEEEEEEEEST"
        return render(request, 'index.html', context={"host": node_name})
