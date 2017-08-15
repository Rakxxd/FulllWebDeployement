from django.conf.urls import url
from first_app import views

urlpatterns = [
url(r'^$',views.index,name='index'),  #www.wbsitename.com/first_app/  whis is same as index page = www.websitename.com
url(r'^help/$',views.help,name='help'),   #www.websitename.com/first_app/help
]
