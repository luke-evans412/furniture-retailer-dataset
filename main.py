#library imports
import random
from random import shuffle, seed
from faker.providers.person.en import Provider
from faker import Faker
import pandas as pd

#names import from faker dataset
fake = Faker()
first_names = list(set(Provider.first_names))
last_names = list(set(Provider.last_names))

#first and last names are randomly shuffled
# integer = random.randint(1, 10000)
# seed(integer)
# shuffle(first_names)
# shuffle(last_names)


quotation = "'"



itemID = 100000
itemIDs = []
orderID = 20000
orderIDList = []
itemCost = [300, 125, 100, 100, 125, 75, 30, 230, 130, 125, 125, 140,
            125, 100, 80, 150, 110, 150, 200, 225, 240, 500, 300, 400,
            1000, 1200, 900, 800, 600, 200, 150, 200, 250, 110, 75, 100,
            250, 75, 160, 125, 100, 125, 100, 125, 120, 90, 90, 125, 150, 40]
itemPrices = []

for i in range(15935):
    orderID = orderID + 1
    orderIDList.append(orderID)


for i in range(50):
    itemID = itemID + 1
    itemIDs.append(itemID)
    itemPrice = itemCost[i] * 5
    itemPrices.append(itemPrice)

#arrays to store order details data

orderDetailsIDList = []
totalOrderIDList = []
itemIDList = []
quantityOrderedList = []

itemIDs = []
itemID = 100000

for i in range(50):
    itemID = itemID + 1
    itemIDs.append(itemID)



itemMin = 1
itemMax = 10
minQuantityOrdered = 1
maxQuantityOrdered = 4
#Order Details For Loop
for i in range(len(orderIDList)):

    newIDList = []
    itemIDQuantity = random.randint(itemMin, itemMax)
    tempItemIDList = random.choices(itemIDs, k=itemIDQuantity)
    for id in tempItemIDList:
        if id not in newIDList:
           newIDList.append(id)

    #nested loop is for amount of items
    for j in range(len(newIDList)):
        orderDetailsIDList.append(orderIDList[i])
        itemIDList.append(newIDList[j])
        quantityOrdered = random.randint(minQuantityOrdered, maxQuantityOrdered)
        quantityOrderedList.append(quantityOrdered)






#Order Details data frame creation

orderDetailsOutput = [orderDetailsIDList, itemIDList, quantityOrderedList]
orderDetails = pd.DataFrame(orderDetailsOutput)
orderDetailsDf = orderDetails.transpose()

orderDetailsColumns = ['OrderID', 'ItemID', 'QuantityOrdered', ]
orderDetailsDf.columns = orderDetailsColumns
orderDetailsDf.to_csv('order_Details.csv', index=False, encoding='utf-8')




# customerIDList = []
# customerID = 10000
#
# for i in range(12000):
#     customerID = customerID + 1
#     customerIDList.append(customerID)



# #arrays to store undetermined order data
# orderID = 20000
# custID = 10001
# orderDateList = []
# orderIDList = []
# customerIDs = []
# chosenCustID = []
# adCampaignIDList = []
# adCampaignIDs = [1, 2, 3, 4, 5, 6, 7]
# randomOrderAmount = random.randint(15000, 18000)
# custID = 10000
# customerIDList = []
#
# for i in range(12000):
#     custID = custID + 1
#     customerIDList.append(custID)
#
# custID = 10000
# #Order Creation Loop
# for i in range(randomOrderAmount):
#     orderID = orderID + 1
#     custID = custID + 1
#     if custID <= 22000:
#         customerID = custID
#         customerIDs.append(customerID)
#     else:
#         customerID = random.choice(customerIDList)
#         customerIDs.append(customerID)
#     chosenCustID.append(customerID)
#     orderDate = fake.date_between(start_date="-3y",end_date="now")
#     orderDateString = orderDate.strftime("%Y-%m-%d")
#     sqlOrderDate = quotation + orderDateString + quotation
#     #sets ad campaign choice to repeat customer for repeat customers
#     frequency = chosenCustID.count(customerID)
#     # if frequency > 1:
#     #     adCampaignID = 8
#     # else:
#     adCampaignID = random.choice(adCampaignIDs)
#     #information is appended to its respective list. Loop repeats until i reaches target number
#     adCampaignIDList.append(adCampaignID)
#     orderDateList.append(sqlOrderDate)
#     orderIDList.append(orderID)
#

#Orders data frame creation

# orderOutput = [orderIDList, customerIDs, orderDateList, adCampaignIDList]
# totalOrder = pd.DataFrame(orderOutput)
# totalOrderDf = totalOrder.transpose()
#
# orderColumns = ['OrderID', 'CustID', 'OrderDate', 'Ad_CampaignID']
# totalOrderDf.columns = orderColumns
# totalOrderDf.to_csv('orders.csv', index=False, encoding='utf-8')









# #Customer creation from line 64 to line 194
# #declaration of initial customer ID and empty customer information lists
# customerID = 10000
# customerIDList = []
# custFNames = []
# custLNames = []
# custBirthdays = []
# custAddresses = []
# custCityList = []
# custStateList = []
# custZIPList = []
# custPhoneNumbers = []
# custEmails = []
# quotation = "'"
# #reference lists to create information for customers
# custEmailSuffixList = ['@gmail.com', '@hotmail.com', '@yahoo.com', '@icloud.com', '@aol.com']
# addressSuffixList = ['Road', 'Ave', 'Blvd', 'St', 'Way', 'Lane', 'Place', 'Dr']
# cityList = ['Nashville', 'Antioch', 'Goodlettsville', 'Hermitage', 'Madison', 'Old Hickory',
#                   'Columbia', 'Spring Hill', 'Greenbrier', 'Springfield', 'White House', 'LaVergne',
#                   'Murfeesboro', 'Smyrna', 'Bethpage', 'Gallatin', 'Hendersonville',
#                   'Portland', 'Westmoreland', 'Lebanon', 'Brentwood', 'Mount Juliet', 'Franklin', 'Nolensville']
# franklinZipList = ['37064', '37067', '37069']
# lebanonZipList = ['37087', '37090']
# mtJulietZipList = ['37121', '37122']
# custAreaCodeList = ['615', '629']
# #string parameters for usage in the concatenation of variables
# space = ' '
# hyphen = '-'
# period = '.'
# #for loop for creation of a customer
# for i in range(12000):
#
#     #ID, First name, Last name, and Date of Birth creations
#     customerID = customerID + 1
#     custFName = random.choice(first_names)
#     custLName = random.choice(last_names)
#     custFNameString = quotation + custFName + quotation
#     custLNameString = quotation + custLName + quotation
#     custDOB = fake.date_between(start_date='-72y', end_date='-21y')
#     custDOBString = custDOB.strftime("%Y-%m-%d")
#     sqlCustDOB = quotation + custDOBString + quotation
#     #customer email creation and concatenation
#     randomEmailNumber = random.randint(10, 1000)
#     numString = str(randomEmailNumber)
#     emailSuffix = random.choice(custEmailSuffixList)
#     custEmail = quotation + custFName + period + custLName + numString + emailSuffix + quotation
#
#     #customer phone number creation and concatenation
#     custAreaCode = random.choice(custAreaCodeList)
#     custPhoneMiddle = random.randint(100,999)
#     middle = str(custPhoneMiddle)
#     custPhoneLastFour = random.randint(1000,9999)
#     lastFour = str(custPhoneLastFour)
#     custPhone = quotation + custAreaCode + hyphen + middle + hyphen + lastFour + quotation
#
#     #customer address creation and concatenation
#     addressNumber = random.randint(1, 3000)
#     addressNumString = str(addressNumber)
#     streetName = fake.street_name()
#     addressSuffix = random.choice(addressSuffixList)
#     custAddress = quotation + addressNumString + space + streetName + space + addressSuffix + quotation
#
#     #customer city is randomly selected from list
#     custCity = random.choice(cityList)
#
#     #customer ZIP is determined by randomly chosen city name
#     if custCity == 'Nashville':
#         customerZIP = random.randint(37201, 37221)
#         if customerZIP == 37202:
#             customerZIP = random.randint(37203, 37221)
#         custZIP = str(customerZIP)
#     elif custCity == 'Antioch':
#         custZIP = '37013'
#     elif custCity == 'Goodlettsville':
#         custZIP = '37072'
#     elif custCity == 'Hermitage':
#         custZIP = '37076'
#     elif custCity == 'Madison':
#         custZIP = '37115'
#     elif custCity == 'Old Hickory':
#         custZIP = '37138'
#     elif custCity == 'Columbia':
#         customerZIP = random.randint(38401, 38402)
#         custZIP = str(customerZIP)
#     elif custCity == 'Greenbrier':
#         custZIP = '37073'
#     elif custCity == 'Springfield':
#         custZIP = '37172'
#     elif custCity == 'LaVergne':
#         custZIP = '37086'
#     elif custCity == 'Murfeesboro':
#         customerZIP = random.randint(37127, 37130)
#         custZIP = str(customerZIP)
#     elif custCity == 'Bethpage':
#         custZIP = '37022'
#     elif custCity == 'Spring Hill':
#         custZIP = '37174'
#     elif custCity == 'White House':
#         custZIP = '37188'
#     elif custCity == 'Smyrna':
#         custZIP = '37167'
#     elif custCity == 'Hendersonville':
#         custZIP = '37075'
#     elif custCity == 'Portland':
#         custZIP = '37148'
#     elif custCity == 'Westmoreland':
#         custZIP = '37186'
#     elif custCity == 'Lebanon':
#         custZIP = random.choice(lebanonZipList)
#     elif custCity == 'Mount Juliet':
#         custZIP = random.choice(mtJulietZipList)
#     elif custCity == 'Brentwood':
#         custZIP = '37027'
#     elif custCity == 'Gallatin':
#         custZIP = '37066'
#     elif custCity == 'Franklin':
#         custZIP = random.choice(franklinZipList)
#     else:
#         custZIP = '37135'
#
#     #customer state declaration
#     custState = quotation + 'TN' + quotation
#
#     #reformatting of city and state for SQL insert statements
#     sqlCustCity = quotation + custCity + quotation
#     sqlCustZIP = quotation + custZIP + quotation
#
#     #information is appended to its respective list. Loop repeats until i reaches target number
#     customerIDList.append(customerID)
#     custFNames.append(custFNameString)
#     custLNames.append(custLNameString)
#     custAddresses.append(custAddress)
#     custBirthdays.append(sqlCustDOB)
#     custCityList.append(sqlCustCity)
#     custStateList.append(custState)
#     custZIPList.append(sqlCustZIP)
#     custPhoneNumbers.append(custPhone)
#     custEmails.append(custEmail)
#
# custOutput = [customerIDList, custFNames, custLNames, custBirthdays, custAddresses,
# custCityList, custStateList, custZIPList, custPhoneNumbers, custEmails]
# totalCust = pd.DataFrame(custOutput)
# totalCustDf = totalCust.transpose()
#
# custColumns = ['CustomerID', 'CustFName', 'CustLName', 'CustDOB',
#                'CustAddress', 'CustCity', 'CustState', 'CustZIP', 'CustPhone', 'CustEmail']
# totalCustDf.columns = custColumns
# totalCustDf.to_csv('customer.csv', index=False, encoding='utf-8')

















