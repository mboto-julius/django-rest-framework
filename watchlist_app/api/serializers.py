from rest_framework import serializers
from watchlist_app.models import Movie 


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ['id', 'name', 'description']
        # exclude = ['active']
        
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and description must be different')
        return data
    
    def validate_name(self, value):
        value = value.strip()
        if len(value) < 2:
            raise serializers.ValidationError('Name must be at least 2 characters long')
        return value

    
