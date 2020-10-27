from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from twilio.rest import Client
from django.utils.datastructures import MultiValueDictKeyError
import time
        
# Create your views here.
def home(request):
        if request.method == 'POST':
                #Stroring all the data, which were entered by the user
                meetLink = request.POST.get('meetLink', '')
                searchText = request.POST.get('searchText', 'dheeraj')
                phoneNo = request.POST.get('phoneNo', '')
                alertText = request.POST.get('alertText', 'Join the meet right now!!!')

                #setting up driver for Google Chrome
                driver = webdriver.Chrome()
                driver.get(meetLink)
                driver.implicitly_wait(100)

                #starting up the process
                for i in range(20000000):
                        try:  
                                elem = driver.find_elements_by_class_name('CNusmb')

                                #name tracking
                                for x in elem:
                                        if (searchText in x.text):
                                                sendMessage(phoneNo, alertText)                 
                                                print("Alert message incoming at your mobile: ", phoneNo)
                                                time.sleep(10)
               
                        except StaleElementReferenceException as Exception:
                                pass  
        else:
                return render(request, 'home.html')

def sendMessage(phoneNumber, alertText):
        account_sid = '' #Add your account_sid, from your twilio account
        auth_token = ''  #Add your auth_token, from your twilio account
        client = Client(account_sid, auth_token)

        message = client.messages \
                .create(
                 body= alertText,
                 from_='', #Add your twilio mobile number
                 to= phoneNumber
                 )

        print(message.sid)
        return
