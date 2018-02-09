# Inserting data ( stocks from a certain company ) to NoSQL Cloudant DB offering from IBM.


## This blog tells how to create a NoSQL Database in Cloudant, and use python to insert data using Python.

The data being used for this demo is a daily prices of stock market data from Microsoft obtained from 
finance.yahoo.com and downloaded from there.

Pre-requisites:

Free account on IBM"s Cloud.
https://console.bluemix.net/

Go to Data and Analytics and Select Cloudant Lite.

Create

Click on Service and Credentials

New Credential
I created a new one called "Credentials-Demo" and Clicked on "View Credentials"

Copy the User name, password, port and the URL as you will need to plug this in to the Python Code later.

Should look something like this.

	{
  	"username": "69369b3a-9733-4e18-b34c-a741d22d2adb-bluemix",
  	"password": "f9b10338e4d2d36caff96cd018103eb20b6b0aba809b9b98c0fa6f9414ed4e6c",
  	"host": "69369b3a-9733-4e18-b34c-a741d22d2adb-bluemix.cloudant.com",
  	"port": 443,
  	"url": "https://69369b3a-9733-4e18-b34c-a741d22d2adb-bluemix:f9b10338e4d2d36caff96cd018103eb20b6b0aba809b9b98c0fa6f9414ed4e6c@69369b3a-9733-4e18-b34c-a741d22d2adb-bluemix.cloudant.com"
	}

Insert this credentials into the Python script during the connect() operation as shown.

```
	# Replace as appropriate, this is obtained when user creates the DB instance in IBMs Cloudant .

	client = Cloudant("69369b3a-9733-4e18-b34c-a741d22d2adb-bluemix", "f9b10338e4d2d36caff96cd018103eb20b6b0aba809b9b98c0fa6f9414ed4e6c", url="https://69369b3a-9733-4e18-b34c-a741d22d2adb-bluemix:f9b10338e4d2d36caff96cd018103eb20b6b0aba809b9b98c0fa6f9414ed4e6c@69369b3a-9733-4e18-b34c-a741d22d2adb-bluemix.cloudant.com")

```

Run the script :
```
	python createstockdb.py
```

Snapshot of the Dashboard where the database is created is shown below.


Click on Manage on the nav panel on the left and Launch the Cloudand Dashboard.

![screen shot 2018-02-09 at 3 38 46 pm](https://user-images.githubusercontent.com/14288989/36022884-a3b7e3aa-0db0-11e8-979d-923d4d9b185d.png)

![screen shot 2018-02-09 at 3 39 03 pm](https://user-images.githubusercontent.com/14288989/36022883-a380ede6-0db0-11e8-82d2-2f2ff5b0ba3c.png)

![screen shot 2018-02-09 at 3 42 07 pm](https://user-images.githubusercontent.com/14288989/36022882-a34a85f8-0db0-11e8-983d-e02c1e7c4283.png)

![screen shot 2018-02-09 at 3 43 07 pm](https://user-images.githubusercontent.com/14288989/36022881-a314724c-0db0-11e8-8e54-45d1a58e92dd.png)

![screen shot 2018-02-09 at 3 43 25 pm](https://user-images.githubusercontent.com/14288989/36022879-a2dd68b0-0db0-11e8-985c-0549e346c204.png)

![screen shot 2018-02-09 at 3 46 14 pm](https://user-images.githubusercontent.com/14288989/36022877-a2a3a2a6-0db0-11e8-9446-995a8bd1b453.png)

![screen shot 2018-02-09 at 3 47 02 pm](https://user-images.githubusercontent.com/14288989/36022875-a26d1128-0db0-11e8-93b7-fa70a0e2b4de.png)

![screen shot 2018-02-09 at 3 47 27 pm](https://user-images.githubusercontent.com/14288989/36022873-a2365bf6-0db0-11e8-93d8-241a730638cb.png)


After running the script, you should see the database being created ( Refresh the browser in "Database" in the nav panel )

![screen shot 2018-02-09 at 3 55 05 pm](https://user-images.githubusercontent.com/14288989/36023204-a9c1b5a4-0db1-11e8-9987-47962fd9f3f5.png)
