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
		latest = stock_data[0]
		previous = ""
		for i in stock_data[1:]:
			previous = i
			stock = {}
			diffrence = latest.stock_close - previous.stock_close
			percentage = float(diffrence / previous.stock_close * 100)
			stock_dif = format(percentage,'.2f')
			stock['open'] = latest.stock_open
			stock['close'] = latest.stock_close
			stock['change'] = stock_dif
			stock['date'] = latest.stock_date
			data.append(stock)
			latest = previous
		data.append({
			"open":previous.stock_open,
			"close":previous.stock_close,
			"date": previous.stock_date,
			"change":"",
		})

		return Response({
			'status':'OK',
			'data':data[::-1]
		},status=status.HTTP_200_OK)	