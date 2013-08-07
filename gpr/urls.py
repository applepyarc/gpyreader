'''
Created on Aug 2, 2013

@author: wguo
'''

from django.conf.urls.defaults import *
from gpr.views import main_page

urlpatterns = patterns('',
    (r'^$', main_page),
)