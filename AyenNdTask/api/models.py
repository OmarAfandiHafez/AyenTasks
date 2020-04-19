from django.db import models
from django_fsm import FSMIntegerField, transition


class Task(models.Model):
    NEW = 0
    IN_PROGRESS = 1
    DONE = 2
    STATES_CHOICES = (
        (NEW, 'New'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    state = FSMIntegerField(choices=STATES_CHOICES, default=NEW)
    linked_task = models.OneToOneField('self', null=True, blank=True,  on_delete=models.SET_NULL)

    @transition(field=state, source=NEW, target=IN_PROGRESS)
    def in_progress(self):
        return 'In progress'

    @transition(field=state, source=IN_PROGRESS, target=DONE)
    def done(self):
        return 'Done'

    class Meta:
        indexes = [models.Index(fields=('title',))]
        ordering = ('title',)
