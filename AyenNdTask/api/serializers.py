from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(TaskSerializer, self).__init__(*args, **kwargs)
        request = kwargs['context']['request']
        if request.method == 'GET':
            self.fields['state'] = serializers.IntegerField(read_only=True)
            self.fields['linked_task'] = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def get_linked_task(instance):
        return {
            'pk': instance.linked_task.pk,
            'title': instance.linked_task.title,
            'description': instance.linked_task.description
        } if instance.linked_task else None

    class Meta:
        model = Task
        fields = ('pk', 'title', 'description')
