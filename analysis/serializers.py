from rest_framework import serializers
from analysis.models import *
"""
Serializer for StockName
"""
class StockNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockName
        fields = '__all__'
"""
Serializer for StockPrices
"""
class StockPricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockPrices
        fields = ('stock_date','stock_volume')