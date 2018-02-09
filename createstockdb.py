#################################################################################
#
#  Code to read data from an external csv file containing stocks data and loading them to 
#  Cloudant DB from this Python Script.
#  
#  User would replace appropriate userid, password and the databases's URL in the client()
#
#  Pre-requisites:
#  
#  The external file in csv format is read one line at a time and loaded to DB.
#  This file ( or similar ) can be generated by going to finance.yahoo.com and 
#  selecting any stock and look at Historical prices and download it.
#  In this example I have used MSFT's daily stock prices and updated it to Cloudant.
#
#  Install Python on the laptop or the server where this script is going to be run.
#  
#  Interesting links :
#
#	https://console.bluemix.net/docs/services/Cloudant/getting-started.html#getting-started-with-cloudant
#
#
#################################################################################
import csv
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

# Replace as appropriate, this is obtained when user creates the DB instance in IBMs Cloudant .

client = Cloudant("7be57a6c-61cb-455a-af9c-3e3b8c392d0f-bluemix", "0b3e4268a2d73219efd0432625c8130ba0e65020b6a036edccf6065a584c13cd", url="https://7be57a6c-61cb-455a-af9c-3e3b8c392d0f-bluemix:0b3e4268a2d73219efd0432625c8130ba0e65020b6a036edccf6065a584c13cd@7be57a6c-61cb-455a-af9c-3e3b8c392d0f-bluemix.cloudant.com")

client.connect()

databaseName = "sdb"

myDatabase = client.create_database(databaseName)

if myDatabase.exists():
	print "'{0}' successfully created.\n".format(databaseName)

stock_data=[]

count=0
with open('MSFT.csv', 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in spamreader:
	stock_data=[]
	count=count+1

	print  ', '.join(row)	

	stock_data.append(row[0])  # 
	stock_data.append(row[1])  # 
	stock_data.append(row[2])  # 
	stock_data.append(row[3])  # 
	stock_data.append(row[4])  # 

	print "Printing .. stock_data"
	print stock_data

	#Date,Open,High,Low,Close,Adj Close,Volume
	#2018-01-08,88.199997,88.580002,87.599998,88.279999,88.279999,22113000

	
	date   = stock_data[0]
	open   = stock_data[1]
	high   = stock_data[2]
	low    = stock_data[3]
	close  = stock_data[4]
		
	# Create a JSON document that represents
	# all the data in the row.
	jsonDocument = {
		    "date"   : date,
		    "open"   : open,
		    "high"   : high,
		    "low"    : low,
	 	    "close"  : close
	}
	
	# Create a document using the Database API.
 	newDocument = myDatabase.create_document(jsonDocument)
	
	if newDocument.exists():
		print "Document  successfully created."
			#print "Document '{0}' successfully created.".format(number)
	

	result_collection = Result(myDatabase.all_docs)
	print "Retrieved minimal document:\n{0}\n".format(result_collection[0])
	
	
	result_collection = Result(myDatabase.all_docs, include_docs=True)
	print "Retrieved full document:\n{0}\n".format(result_collection[0])

client.disconnect()