from rest_framework import serializers
from todo.models import Todo
class TodoSerializer(serializers.ModelSerializer): # forms.ModelForm
    class Meta:
        model = Todo
        fields = [
            'pk',
            'name',
        ]
        read_only_fields = ['pk']