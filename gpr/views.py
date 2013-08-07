'''
Created on Aug 2, 2013

@author: wguo
'''

from gpr.models import Item
from gpr.models import FeedInfo
from django.template import loader, Context
from django.http import HttpResponse
from gpr import feedparser
import os

def main_page(request):
    
    _BASE_PATH = os.path.abspath(os.path.dirname(__file__))  
    config_file = os.path.join(_BASE_PATH, "rss_feed.config")
    fHandler = open ( config_file )  
    fileList = fHandler.readlines()
    for fileLine in fileList:
        
        feeds = feedparser.parse( fileLine )
        if (len(feeds.entries) <= 0 or feeds.bozo == 1):
            continue
    
        feedInfo = FeedInfo()
        querryFeedInfo = FeedInfo.gql("WHERE link = :1", feeds.feed.link)
        if (querryFeedInfo.count() == 0):        
            feedInfo.title = feeds.feed.title
            feedInfo.link = feeds.feed.link
            feedInfo.description = feeds.feed.description
            feedInfo.put()
    
        for feed in feeds[ "items" ]:
            querry = Item.gql("WHERE link = :1", feed[ "link" ])
            if(querry.count() == 0):
                item = Item()
                item.title = feed[ "title" ]
                item.link = feed[ "link" ]
                item.date = feed[ "published" ]
                item.description = feed["description"]
                item.put()
                
    fHandler.close()
            
    myFeeds = FeedInfo.all()
    items =Item.all()
    
    t = loader.get_template("gpr/main_page.html")
    c = Context({ 'myFeeds': myFeeds, 'items': items })
    return HttpResponse(t.render(c))
