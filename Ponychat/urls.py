from django.conf.urls import url, include
from chat.views import Threads, MoreThreads, SingleThread

urlpatterns = [
    url(r'^thread$', Threads.as_view()),
    url(r'^thread/page/(?P<num>\d+)$', MoreThreads.as_view()),
    url(r'^thread/(?P<id>\d+)$', SingleThread.as_view())
]