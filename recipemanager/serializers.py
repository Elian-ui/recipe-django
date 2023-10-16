from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'completed')

    def validate_title(self, value):
        # Add custom validation logic here
        if len(value) < 5:
            raise serializers.ValidationError(
                "Title must be at least 5 characters long.")
        return value

    def validate_completed(self, value):
        # Add custom validation logic here
        if value and not self.instance:
            raise serializers.ValidationError(
                "A new task cannot be completed.")
        return value
