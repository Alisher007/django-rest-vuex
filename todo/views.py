from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from rest_framework import generics, mixins
from todo.models import Todo
# from .permissions import IsOwnerOrReadOnly
from .serializers import TodoSerializer
class TodoCreateView(generics.CreateAPIView): #  CreateView 
    lookup_field = 'pk' # slug, id # url(r'?P<pk>\d+')
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

class TodoListView(generics.ListAPIView): # List
    lookup_field = 'pk' # slug, id # url(r'?P<pk>\d+')
    serializer_class = TodoSerializer
    #queryset = Todo.objects.all()
    def get_queryset(self):
        qs = Todo.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
            Q(name__icontains=query)
            ).distinct()
        return qs


class TodoRudView(generics.RetrieveUpdateDestroyAPIView): # DetailView Update  Delete

    lookup_field = 'pk' # slug, id # url(r'?P<pk>\d+')
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.all()