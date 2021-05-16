from django.db import models
from utils.uuid_helper import generate_lrtid

# Create your models here.


class LongRunningTask(models.Model):
    PROCESSING_STATE = 1
    COMPLETE_STATE = 2
    FAILED_STATE = 3

    STATE_CHOICES = (
        (PROCESSING_STATE, 'Processing'),
        (COMPLETE_STATE, 'Complete'),
        (FAILED_STATE, 'Failed'),
    )

    lrtid = models.CharField(
        max_length=100,
        unique=True,
        default=generate_lrtid
    )
    state = models.IntegerField(default=1, choices=STATE_CHOICES)
    result = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Long Running Tasks'