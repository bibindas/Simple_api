# RDT-Django-round

## Instalation:
	 - pip install -r requirements.txt

## How to run:
	 - run following commands from root directory
	 - python manage.py runserver

## Documentation:
###### Urls for top five stock volume 

	- http://127.0.0.1:8000/topfive/?stock_name=Apple
	- http://127.0.0.1:8000/topfive/?stock_name=Microsoft
	- http://127.0.0.1:8000/topfive/?stock_name=BlackBerry

###### Response body:

	- Url for request: http://127.0.0.1:8000/topfive/?stock_name=Apple

		{
	    "status": "Success",
	    "data": [
	        {
	            "stock_date": "2017-02-01T00:00:00Z",
	            "stock_volume": 111985040
	        },
	        {
	            "stock_date": "2017-06-12T00:00:00Z",
	            "stock_volume": 72307330
	        },
	        {
	            "stock_date": "2017-06-09T00:00:00Z",
	            "stock_volume": 64882657
	        },
	        {
	            "stock_date": "2017-05-17T00:00:00Z",
	            "stock_volume": 50767678
	        },
	        {
	            "stock_date": "2017-06-16T00:00:00Z",
	            "stock_volume": 50361093
	        }
	    ]
	}	

##### Url for the individual company’s share.
	
	- http://127.0.0.1:8000/companyshare/?stock_name=Apple
	- http://127.0.0.1:8000/companyshare/?stock_name=Microsoft
	- http://127.0.0.1:8000/companyshare/?stock_name=BlackBerry

###### Response body::
	-{
    "status": "OK",
    "data": [
        {
            "date": "2017-01-03T00:00:00Z",
            "close": 62.58,
            "open": 62.79,
            "change": ""
        },
        {
            "date": "2017-01-04T00:00:00Z",
            "close": 62.3,
            "open": 62.48,
            "change": "-0.45"
        },...}