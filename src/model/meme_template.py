import datetime

from google.appengine.ext import db
from google.appengine.api import users


class MemeTemplate(db.Model):
  creator = db.EmailProperty(required=True, indexed=True)
  create_datetime = db.DateTimeProperty(required=True, indexed=True, auto_now_add=True)
  name = db.StringProperty(required=True, indexed=False)
  width = db.IntegerProperty(required=True, indexed=False)
  height = db.IntegerProperty(required=True, indexed=False)
  image_data = db.BlobProperty(required=True, indexed=False)
  thumbnail_image_data = db.BlobProperty(required=True, indexed=False)
  last_used = db.DateTimeProperty(indexed=True, auto_now_add=False, default=0)


  def is_owner(self):
    user_email = users.get_current_user().email()
    return self.creator == user_email
