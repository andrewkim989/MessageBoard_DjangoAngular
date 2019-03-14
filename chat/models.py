from django.db import models

class ThreadManager (models.Manager):
    def thread(self, data):
        e = []

        if (len(data["subject"]) < 3):
            e.append("Thread subject must be at least 3 characters long")
        if (len(data["post"]) < 5):
            e.append("Post must be at least 5 characters long")

        return e

class Thread (models.Model):
    name = models.CharField(max_length = 50)
    subject = models.CharField(max_length = 255)
    #image = models.CharField(max_length = 255)
    post = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ThreadManager()

class Comment (models.Model):
    name = models.CharField(max_length = 50)
    #image = models.CharField(max_length = 255)
    post = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    thread = models.ForeignKey(Thread, on_delete = models.CASCADE, related_name = "comments")
    objects = models.Manager()