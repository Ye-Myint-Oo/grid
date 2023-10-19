from django.db import models

class QueueMessage(models.Model):
    queue_name = models.CharField(max_length=100)
    request_number = models.IntegerField()
    mail_number = models.IntegerField()
    subject_id = models.IntegerField()
    data_length = models.IntegerField()
    aggregate_number = models.IntegerField(blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return f"QueueMessage - {self.queue_name} - {self.request_number}"