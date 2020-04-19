from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView, Response
from .models import Task
from .serializers import TaskSerializer
from django_fsm import can_proceed


class TasksListCreateAPIView(ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskRetrieveAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskRetrieveUpdateAPIView(APIView):

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, context={'request': request})
        return Response(serializer.data, status=200)

    def put(self, request, pk):
        """
        Request body example
        {
            "title": "title",
            "description": "description"
        }
        """
        task = get_object_or_404(Task, pk=pk)
        if not can_proceed(task.in_progress):
            raise PermissionDenied

        data = request.data
        serializer = TaskSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response({'message': 'Please Provide valid data'}, status=400)


class ChangeTaskState(APIView):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)

        if can_proceed(task.in_progress):
            message = task.in_progress()
            task.save()
        elif can_proceed(task.done):
            message = task.done()
            task.save()
        else:
            message = f'Task "{task.title}" can\'t be modified because it is in "done" state!'
            return Response({'message': message}, status=400)
        return Response({'message': f'Task "{task.title}" has moved to in "{message}" state.'}, status=200)


class LinkTasksAPIView(APIView):
    def post(self, request, first_task_pk, second_task_pk):
        if first_task_pk == second_task_pk:
            return Response({'message': 'You can\'t link task to itself!'}, status=400)

        first_task = get_object_or_404(Task, pk=first_task_pk)
        second_task = get_object_or_404(Task, pk=second_task_pk)
        if can_proceed(first_task.done) and can_proceed(second_task.done):
            if first_task.linked_task:
                return Response(
                    {'message': f'Task {first_task.title} is already linked to {first_task.linked_task.title}'},
                    status=400
                )
            if second_task.linked_task:
                return Response(
                    {'message': f'Task {second_task.title} is already linked to {second_task.linked_task.title}'},
                    status=400
                )
            first_task.linked_task = second_task
            second_task.linked_task = first_task
            first_task.save()
            second_task.save()
            return Response(
                {'message': f'Task {first_task.title} and task {second_task.title} have been linked successfully'},
                status=200
            )
        else:
            raise PermissionDenied


class UnlinkTasksAPIView(APIView):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        if can_proceed(task.done):
            if task.linked_task:
                linked_task = task.linked_task
                linked_task.linked_task = None
                linked_task.save()
            task.linked_task = None
            task.save()
            return Response({'message': f'Task {task.title} has been unlinked successfully'}, status=200)
        else:
            raise PermissionDenied
