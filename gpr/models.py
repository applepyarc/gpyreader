'''
Created on Aug 2, 2013

@author: wguo
'''

from google.appengine.ext import db

class Item (db.Model):
    title = db.StringProperty()
    link = db.StringProperty()
    description = db.TextProperty()
    date = db.StringProperty()
    
    def __unicode__(self):
        return self.title
    
class FeedInfo (db.Model):
    title = db.StringProperty()
    link = db.StringProperty()
    description = db.StringProperty()
    