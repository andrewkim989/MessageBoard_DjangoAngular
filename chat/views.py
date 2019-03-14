from django.http import JsonResponse
from django.views import View
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Thread, Comment

import json, os, time, base64 

ALLOWED_EXTENSIONS = ("jpg", "jpeg", "png", "gif") 

class Threads (View):
    def get(self, request):
        threads = list(Thread.objects.values().all())
        for i in range(1, len(Thread.objects.all()) + 1):
            comments = []
            c = list(Comment.objects.filter(thread_id = i).order_by("-id")[:3].values())
            c.reverse()
            comments.append(c)
            threads[i - 1]["comments"] = comments[0]
            count = len(Comment.objects.filter(thread_id = i).values())
            count = count - 3
            if (count < 0):
                count = 0
            threads[i - 1]["count"] = count
        return JsonResponse({"threads": threads})
    
    def post(self, request):
        thr = json.loads(request.body.decode())
        e = Thread.objects.thread(thr)
        name = thr["name"]
        subject = thr["subject"]
        #image = thr["image"]
        post = thr["post"]

        if len(e):
            return JsonResponse({"error": e})
        else:
            if (len(name) < 1):
                name = "Anonymous"

            Thread.objects.create(name = name, subject = subject, post = post)
            return JsonResponse({"status": "Thread created"})

class MoreThreads(View):
    def get(self, request, num):
        threads = list(Thread.objects.values().all())
        for i in range(1, len(Thread.objects.all()) + 1):
            comments = []
            c = list(Comment.objects.filter(thread_id = i).order_by("-id")[:3].values())
            c.reverse()
            comments.append(c)
            threads[i - 1]["comments"] = comments[0]
            count = len(Comment.objects.filter(thread_id = i).values())
            count = count - 3
            if (count < 0):
                count = 0
            threads[i - 1]["count"] = count
        page = request.GET.get("page", num)

        paginator = Paginator(threads, 5)
        try:
            threads = paginator.page(page)
        except PageNotAnInteger:
            threads = paginator.page(1)
        except EmptyPage:
            threads = paginator.page(paginator.num_pages)
        
        return JsonResponse({"threads": threads})

class SingleThread(View):
    def get(self, request, id):
        thread = Thread.objects.filter(id = id).values()[0]
        comments = Comment.objects.filter(thread_id = id).values()
        return JsonResponse({"thread": thread, "comments": list(comments)})
    
    def post(self, request, id):
        c = json.loads(request.body.decode())
        name = c["name"]
        #image = c["image"]
        post = c["post"]

        thread = Thread.objects.get(id = id)
        if (len(name) < 1):
            name = "Anonymous"
        Comment.objects.create(name = name, post = post, thread = thread)
        return JsonResponse({"status": "Comment created"})