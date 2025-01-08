from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(default="")
    done = models.BooleanField(default=False)
    deadline = models.DateField()
    def __str__(self):
        return f"{self.title} - {self.deadline} - {self.done}"

    def status(self):
        return self.done
    status.short_description = "Done"
    status.boolean = True