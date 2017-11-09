# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render
from analysis.models import StockName,StockPrices
from analysis.serializers import (
   StockNameSerializer,
   StockPricesSerializer,
   )

# Create your views here.

class TopFive(APIView):
	"""
	Return top five for a specific company

	Request parameters:
	{'stock_name': <string>}

	Response body:
	{
	'status': <string>,
	'data':[
		{
       	"stock_date": <string_date>,
        "stock_volume": <integer_volume>
        },...
	]}

	"""
	def get(self,request):
		stock_name = request.query_params.get("stock_name")
		volumes = StockPrices.objects.filter(stock_id__name=stock_name).order_by('-stock_volume')[:5]
		if volumes:
			data = StockPricesSerializer(volumes,many=True).data
			return Response({
				'status':'Success',
				'data':data,
				},status=status.HTTP_200_OK)
		return Response({
			'status':'Failed',
			},status=status.HTTP_200_OK)

class CompanyShare(APIView):
	"""
	Return percentage of stock open and stock close

	Request body:
	{'stock_name': <string>}

	Response body:
	{
	'status': <string>,
	'data':[
		{
       	"date": <date_string>,
        "close": <float>,
        "open": <float>,
        "change": <string>,
        },...
	]}

	"""

	def get(self,request):
		stock_name = request.query_params.get('stock_name')
		stock_data = StockPrices.objects.filter(stock_id__name=stock_name)
		data = []
		for i in stock_data:
			stock = {}
			diffrence = i.stock_close - i.stock_open
			percentage = float(diffrence / i.stock_open * 100)
			stock_dif = format(percentage,'.2f')
			stock['open'] = i.stock_open
			stock['close'] = i.stock_close
			stock['change'] = stock_dif
			stock['date'] = i.stock_date
			data.append(stock)
		return Response({
			'status':'OK',
			'data':data
		},status=status.HTTP_200_OK)	