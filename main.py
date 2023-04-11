
#library imports
import random
from random import shuffle, seed

import pandas as pd
from faker.providers.person.en import Provider
from faker import Faker
#import pandas as pd
#import numpy as np

#names import from faker dataset
fake = Faker()
first_names = list(set(Provider.first_names))
last_names = list(set(Provider.last_names))

#first and last names are randomly shuffled
integer = random.randint(1, 10000)
seed(integer)
shuffle(first_names)
shuffle(last_names)

quotation = "'"

quotation = "'"

# #arrays to store undetermined employee data
empFirstNames = []
empLastNames = []
employeeEmail = []
empDOB = []
empStartDates = []
empEndDates = []

#arrays to store undetermined employee data
empFirstNames = []
empLastNames = []
employeeEmail = []
empDOB = []
empStartDates = []
empEndDates = []
employeeIDList = []
empID = 1000

#arrays for predetermined employee data
jobIDList = [100, 101, 103, 104, 105, 1000, 1100, 1200, 1300, 1400,
         1500, 1600, 1800, 2100, 3000, 3100, 3200, 3300, 3400,
         3500, 3600, 3700, 3800, 4100, 4200, 4300, 5000, 5100, 5200]
departmentIDList = [1001, 1002, 1003, 1004, 1005, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1002, 1006, 1003, 1006,
                1003, 1006, 1006, 1003, 1003, 1004, 1006, 1004, 1004, 1005, 1005, 1005]
empSalaryList = [80000, 80000, 80000, 80000, 80000, 60000, 30000, 40000, 37000, 37000, 37000,
                 37000, 45000, 40000, 60000, 50000, 100000, 100000, 100000, 100000, 45000,
                 45000, 25000, 40000, 24000, 24000, 60000, 34000, 34000]
#file clerk salary = 32,050

#email suffix and period declarations used for email concatenation
empEmailSuffix = '@musiccityfurnishings.com'
period = '.'

#Employee creator for loop. Variables with prefix "sql" are formatted to be inserted into SQL
for i in range(29):
    empID = empID + 1
    employeeIDList.append(empID)
    first_name = quotation + first_names[i] + quotation
    last_name = quotation + last_names[i] + quotation
    firstNameEmail = quotation + first_names[i]
    lastNameEmail = last_names[i]
    empEmail = firstNameEmail + period + lastNameEmail + empEmailSuffix + quotation
    empEmail.lower()
    empBirthday = fake.date_between(start_date='-65y', end_date='-22y')
    empBirthdayString = empBirthday.strftime("%Y-%m-%d")
    sqlEmpBirthday = quotation + empBirthdayString + quotation
    empStartDate = fake.date_between(start_date= '-4y', end_date='-3y')
    empStartDateString = empStartDate.strftime("%Y-%m-%d")
    sqlEmpStartDate = quotation + empStartDateString + quotation
    empFirstNames.append(first_name)
    empLastNames.append(last_name)
    employeeEmail.append(empEmail)
    empDOB.append(sqlEmpBirthday)
    empStartDates.append(sqlEmpStartDate)


empOutput = [employeeIDList, jobIDList, departmentIDList, empFirstNames,
                empLastNames, empDOB, empSalaryList, employeeEmail, empStartDates, empEndDates]
totalEmp = pd.DataFrame(empOutput)
totalEmpDf = totalEmp.transpose()

empColumns = ['EmployeeID', 'JobID', 'DepartmentID', 'EmpFName',
               'EmpLName', 'EmpDOB', 'EmpSalary', 'EmpEmail', 'EmpStartDate', 'EmpEndDate']
totalEmpDf.columns = empColumns
totalEmpDf.to_csv('EMPLOYEE.csv', index=False, encoding='utf-8')

#---------------------------------------------------------------------------------------------------------

#Customer creation from line 64 to line 194
#declaration of initial customer ID and empty customer information lists
customerID = 10000
customerIDList = []
custFNames = []
custLNames = []
custBirthdays = []
custAddresses = []
custCityList = []
custStateList = []
custZIPList = []
custPhoneNumbers = []
custEmails = []
quotation = "'"
#reference lists to create information for customers
custEmailSuffixList = ['@gmail.com', '@hotmail.com', '@yahoo.com', '@icloud.com', '@aol.com']
addressSuffixList = ['Road', 'Ave', 'Blvd', 'St', 'Way', 'Lane', 'Place', 'Dr']
cityList = ['Nashville', 'Antioch', 'Goodlettsville', 'Hermitage', 'Madison', 'Old Hickory',
                  'Columbia', 'Spring Hill', 'Greenbrier', 'Springfield', 'White House', 'LaVergne',
                  'Murfeesboro', 'Smyrna', 'Bethpage', 'Gallatin', 'Hendersonville',
                  'Portland', 'Westmoreland', 'Lebanon', 'Brentwood', 'Mount Juliet', 'Franklin', 'Nolensville']
franklinZipList = ['37064', '37067', '37069']
lebanonZipList = ['37087', '37090']
mtJulietZipList = ['37121', '37122']
custAreaCodeList = ['615', '629']
#string parameters for usage in the concatenation of variables
space = ' '
hyphen = '-'
period = '.'
#for loop for creation of a customer
quotation = "'"

#Customer creation from line 64 to line 194
#declaration of initial customer ID and empty customer information lists
customerID = 10000
customerIDList = []
custFNames = []
custLNames = []
custBirthdays = []
custAddresses = []
custCityList = []
custStateList = []
custZIPList = []
custPhoneNumbers = []
custEmails = []
quotation = "'"
#reference lists to create information for customers
custEmailSuffixList = ['@gmail.com', '@hotmail.com', '@yahoo.com', '@icloud.com', '@aol.com']
addressSuffixList = ['Road', 'Ave', 'Blvd', 'St', 'Way', 'Lane', 'Place', 'Dr']
cityList = ['Nashville', 'Antioch', 'Goodlettsville', 'Hermitage', 'Madison', 'Old Hickory',
                  'Columbia', 'Spring Hill', 'Greenbrier', 'Springfield', 'White House', 'LaVergne',
                  'Murfeesboro', 'Smyrna', 'Bethpage', 'Gallatin', 'Hendersonville',
                  'Portland', 'Westmoreland', 'Lebanon', 'Brentwood', 'Mount Juliet', 'Franklin', 'Nolensville']
franklinZipList = ['37064', '37067', '37069']
lebanonZipList = ['37087', '37090']
mtJulietZipList = ['37121', '37122']
custAreaCodeList = ['615', '629']
#string parameters for usage in the concatenation of variables
space = ' '
hyphen = '-'
period = '.'
#for loop for creation of a customer
for i in range(12000):

    #ID, First name, Last name, and Date of Birth creations
    customerID = customerID + 1
    custFName = random.choice(first_names)
    custLName = random.choice(last_names)
    custFNameString = quotation + custFName + quotation
    custLNameString = quotation + custLName + quotation
    custDOB = fake.date_between(start_date='-72y', end_date='-21y')
    custDOBString = custDOB.strftime("%Y-%m-%d")
    sqlCustDOB = quotation + custDOBString + quotation
    #customer email creation and concatenation
    randomEmailNumber = random.randint(10, 1000)
    numString = str(randomEmailNumber)
    emailSuffix = random.choice(custEmailSuffixList)
    custEmail = quotation + custFName + period + custLName + numString + emailSuffix + quotation

    #customer phone number creation and concatenation
    custAreaCode = random.choice(custAreaCodeList)
    custPhoneMiddle = random.randint(100,999)
    middle = str(custPhoneMiddle)
    custPhoneLastFour = random.randint(1000,9999)
    lastFour = str(custPhoneLastFour)
    custPhone = quotation + custAreaCode + hyphen + middle + hyphen + lastFour + quotation

    #customer address creation and concatenation
    addressNumber = random.randint(1, 3000)
    addressNumString = str(addressNumber)
    streetName = fake.street_name()
    addressSuffix = random.choice(addressSuffixList)
    custAddress = quotation + addressNumString + space + streetName + space + addressSuffix + quotation

    #customer city is randomly selected from list
    custCity = quotation + random.choice(cityList) + quotation

    #customer ZIP is determined by randomly chosen city name
    if custCity == 'Nashville':
        customerZIP = random.randint(37201, 37221)
        if customerZIP == 37202:
            customerZIP = random.randint(37203, 37221)
        custZIP = str(customerZIP)
    elif custCity == 'Antioch':
        custZIP = '37013'
    elif custCity == 'Goodlettsville':
        custZIP = '37072'
    elif custCity == 'Hermitage':
        custZIP = '37076'
    elif custCity == 'Madison':
        custZIP = '37115'
    elif custCity == 'Old Hickory':
        custZIP = '37138'
    elif custCity == 'Columbia':
        customerZIP = random.randint(38401, 38402)
        custZIP = str(customerZIP)
    elif custCity == 'Greenbrier':
        custZIP = '37073'
    elif custCity == 'Springfield':
        custZIP = '37172'
    elif custCity == 'LaVergne':
        custZIP = '37086'
    elif custCity == 'Murfeesboro':
        customerZIP = random.randint(37127, 37130)
        custZIP = str(customerZIP)
    elif custCity == 'Bethpage':
        custZIP = '37022'
    elif custCity == 'Spring Hill':
        custZIP = '37174'
    elif custCity == 'White House':
        custZIP = '37188'
    elif custCity == 'Smyrna':
        custZIP = '37167'
    elif custCity == 'Hendersonville':
        custZIP = '37075'
    elif custCity == 'Portland':
        custZIP = '37148'
    elif custCity == 'Westmoreland':
        custZIP = '37186'
    elif custCity == 'Lebanon':
        custZIP = random.choice(lebanonZipList)
    elif custCity == 'Mount Juliet':
        custZIP = random.choice(mtJulietZipList)
    elif custCity == 'Brentwood':
        custZIP = '37027'
    elif custCity == 'Gallatin':
        custZIP = '37066'
    elif custCity == 'Franklin':
        custZIP = random.choice(franklinZipList)
    else:
        custZIP = '37135'

    #customer state declaration
    custState = quotation + 'TN' + quotation
    sqlCustZIP = quotation + custZIP + quotation

    #information is appended to its respective list. Loop repeats until i reaches target number
    customerIDList.append(customerID)
    custFNames.append(custFNameString)
    custLNames.append(custLNameString)
    custAddresses.append(custAddress)
    custBirthdays.append(sqlCustDOB)
    custCityList.append(custCity)
    custStateList.append(custState)
    custZIPList.append(sqlCustZIP)
    custPhoneNumbers.append(custPhone)
    custEmails.append(custEmail)

#------------------------------------------------------------------------------------------------------

#arrays to store undetermined order data
orderID = 20000
custID = 10001
orderDateList = []
orderIDList = []
customerIDs = []
chosenCustID = []
adCampaignIDList = []
adCampaignIDs = [1, 2, 3, 4, 5, 6, 7]
randomOrderAmount = random.randint(15000, 18000)
custID = 10000
customerIDList = []

for i in range(12000):
    custID = custID + 1
    customerIDList.append(custID)

custID = 10000
#Order Creation Loop
for i in range(randomOrderAmount):
    orderID = orderID + 1
    custID = custID + 1
    if custID <= 22000:
        customerID = custID
        customerIDs.append(customerID)
    else:
        customerID = random.choice(customerIDList)
        customerIDs.append(customerID)
    chosenCustID.append(customerID)
    orderDate = fake.date_between(start_date="-3y",end_date="now")
    orderDateString = orderDate.strftime("%Y-%m-%d")
    sqlOrderDate = quotation + orderDateString + quotation
    #sets ad campaign choice to repeat customer for repeat customers
    frequency = chosenCustID.count(customerID)
    # if frequency > 1:
    #     adCampaignID = 8
    # else:
    adCampaignID = random.choice(adCampaignIDs)
    #information is appended to its respective list. Loop repeats until i reaches target number
    adCampaignIDList.append(adCampaignID)
    orderDateList.append(sqlOrderDate)
    orderIDList.append(orderID)



#------------------------------------------------------------------------------------------------
#Item table creation
companyID = 1
quotation = "'"
companyIDList = []
itemID = 100000
itemIDs = []
itemNames = []
itemCost = [300, 125, 100, 100, 125, 75, 30, 230, 130, 125, 125, 140,
            125, 100, 80, 150, 110, 150, 200, 225, 240, 500, 300, 400,
            1000, 1200, 900, 800, 600, 200, 150, 200, 250, 110, 75, 100,
            250, 75, 160, 125, 100, 125, 100, 125, 120, 90, 90, 125, 150, 40]
itemPrices = []
itemQuantity = []
weight = [180, 100, 20, 75, 100, 40, 25, 200, 120, 150, 100, 130, 150,
          75, 100, 135, 210, 150, 100, 250, 300, 250, 150,
          300, 400, 300, 500, 250, 50, 100, 200, 150, 175, 125, 200,
          35, 40, 130, 90, 100, 120, 130, 190, 150, 70, 75, 100, 150, 80, 30]
itemName = ['Wooden Tahoe Dining Table', 'Wooden Dresser (4 Drawers)', 'Wooden Coffee Table', 'Wooden Desk', 'Wooden Wardrobe',
            'Wood Night Stand', 'Wood Chair', 'Glass Dining Table with Stainless Steel Base', 'Round Glass Coffee Table with Stainless Steel Base',
            'Clear Glass Drinking Table with Stainless Steel Base', 'Glass Display Stand with Wooden Base', 'Triangular Glass Coffee Table with Wood Base',
            'Glass TV Stand with Wooden Shelves', 'Stainless Steel Kitchen Stand- 4 Shelves',
            'Stainless Steel Utility Stand', 'Stainless Steel Curved Side Table',
            'Stainless Steel Work Table with Casters', 'Stainless Steel Solid Coffee Table', 'MCF Floor Shelf Coffee Table',
            'Stainless Steel Bookshelf with Wooden Sides', 'Leather Sofa with Cotton/Poly Interior', 'Leather Recliner', 'Leather Chair',
            'Leather Exquisite Futon', 'Leather 3 Seat Couch', 'China Cabinet',
            'Leather Multi-Piece Sofa', 'Leather Exhibition Daybed', 'MCF Brewster Chair', 'MCF Love Seat',
            'Wooden Bookshelf', 'MCF TV Stand', 'Stainless Steel Work Bench', 'Wooden Work Bench',
            'Barcelona Chair','Bar Stool', 'Counter Stool', 'Rectangular Wooden Cabinet', 'Square Wooden Cupboard',
            'Wooden Door Sideboard Chest with Glass Doors', 'Stainless Steel Sideboard Chest with Glass Doors',
            'Outdoor Glass Dining Table', 'Wooden Study Table', 'Wooden Buffet Server',
            'Wooden End Table with Stainless Steel Base', 'Wooden 2 Drawer Chest', 'Wooden Storage Cabinet',
            'Stainless Steel Storage Cabinet', 'Leather Armchair with Wooden Legs', 'Wooden Floating Shelf']


for i in range(50):
    itemID = itemID + 1
    itemIDs.append(itemID)

for i in range(50):
    companyIDList.append(companyID)
    itemTitle = quotation + itemName[i] + quotation
    itemNames.append(itemTitle)
    if itemIDs[i] >= 100019 and itemIDs[i] <= 100033:
        itemCount = random.randint(10, 30)
    else:
        itemCount = random.randint(50, 100)
    itemQuantity.append(itemCount)
    itemPrice = itemCost[i] * 5
    itemPrices.append(itemPrice)




#------------------------------------------------------------------------------------------------
#arrays to store order details data

orderDetailsIDList = []
totalOrderIDList = []
itemIDList = []
quantityOrderedList = []



itemMin = 1
itemMax = 10
minQuantityOrdered = 1
maxQuantityOrdered = 5
#Order Details For Loop
for i in range(len(totalOrderIDList)):

    itemIDQuantity = random.choice(itemMin, itemMax)
    tempItemIDList = random.choices(itemIDs, k=itemIDQuantity)

    #nested loop is for amount of items
    for j in range(len(tempItemIDList)):

        quantityOrdered = random.choice(minQuantityOrdered, maxQuantityOrdered)
        orderDetailsIDList.append(totalOrderIDList[i])
        itemIDList.append(tempItemIDList[j])
        quantityOrderedList.append(quantityOrdered)











# empOutput = ['EmployeeID', jobIDList, 'departmentIDList', empFirstNames,
#               empLastNames, 'empDOB', 'empSalaryList', employeeEmail, empStartDates, empEndDates]
# totalEmp = pd.DataFrame(empOutput)
# totalEmpDf = totalEmp.transpose()
#
# empColumns = ['EmployeeID', 'JobID', 'DepartmentID', 'EmpFName',
#               'EmpLName', 'EmpDOB', 'EmpSalary', 'EmpEmail', 'EmpStartDate', 'EmpEndDate']
# totalEmpDf.columns = empColumns
#totalCustDf.to_csv('customer.csv', index=False, encoding='utf-8')

#custOutput = [customerIDList, custFNames, custLNames, custBirthdays, custAddresses,
#custCityList, custStateList, custZIPList, custPhoneNumbers, custEmails]
#totalCust = pd.DataFrame(custOutput)
#totalCustDf = totalCust.transpose()

#custColumns = ['CustomerID', 'CustFName', 'CustLName', 'CustDOB',
#               'CustAddress', 'CustCity', 'CustState', 'CustZIP', 'CustPhone', 'CustEmail']
#totalCustDf.columns = custColumns
#totalCustDf.to_csv('customer.csv', index=False, encoding='utf-8')

#Orders data frame creation

# orderOutput = [orderIDList, customerOrderIDList, orderDateList, adCampaignIDList]
# totalOrder = pd.DataFrame(orderOutput)
# totalOrderDf = totalOrder.transpose()
#
# orderColumns = ['OrderID', 'CustID', 'OrderDate', 'Ad_CampaignID']
# totalOrderDf.columns = orderColumns
# totalOrderDf.to_csv('orders.csv', index=False, encoding='utf-8')

#Item data frame creation

# itemOutput = [itemIDs, companyIDList, itemNames, itemQuantity, itemCost, itemPrices, weight]
# totalItem = pd.DataFrame(itemOutput)
# totalItemDf = totalItem.transpose()
#
# itemColumns = ['ItemID', 'CompanyID', 'ItemName', 'ItemQuantity', 'ItemCost', 'ItemPrice', 'ItemWeightLBS']
# totalItemDf.columns = itemColumns
# totalItemDf.to_csv('item.csv', index=False, encoding='utf-8')



#Order Details data frame creation

# orderDetailsOutput = [orderIDs, itemIDs, quantityOrderedList]
# orderDetails = pd.DataFrame(orderDetailsOutput)
# orderDetailsDf = orderDetails.transpose()
#
# orderDetailsColumns = ['OrderID', 'ItemID', 'QuantityOrdered', ]
# orderDetailsDf.columns = orderDetailsColumns
# orderDetailsDf.to_csv('order_Details.csv', index=False, encoding='utf-8')

