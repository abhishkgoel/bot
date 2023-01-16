import random
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .forms import *

import tkinter as tk
# import tkinter as Tk
import tkinter.filedialog as fd
import getpass
from time import sleep
import time
import re
from datetime import date
from datetime import timedelta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd 
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import datetime
from dateutil.relativedelta import relativedelta
from .bots import *
today = date.today()
global driver


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect(register)
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, password=password, 
                                        email=email, first_name=first_name, last_name=last_name)
                user.save()
                
                return redirect('login_user')


        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(register)
            

    else:
        return render(request, 'app/registeration.html')



def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('model_form_upload')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')
    else:
        return render(request, 'app/login.html')

def logout_user(request):
    auth.logout(request)
    return redirect('login_user')

@login_required
def home(request):
    return render(request, 'app/home.html')
    

def model_form_upload(request):
    global driver
    if request.method == 'POST':
        form = DocumentForm(request.POST,request.POST)
        if form.is_valid():
            file_instance = Document()
            file_instance.email = request.POST['email']
            file_instance.password = request.POST['password']
            file_instance.save()
            idd = file_instance.id
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.maximize_window()
            driver.get('https://eprplastic.cpcb.gov.in/#/plastic/home')
            time.sleep(1)
            email = driver.find_element(by=By.XPATH, value='//*[@id="username"]')
            document1call = Document.objects.get(id = idd)
            mail = document1call.email
            passs = document1call.password
            email.send_keys(mail)
            password = driver.find_element(by=By.XPATH, value='//*[@id="password"]')
            password.send_keys(passs)
            login = driver.find_element(by=By.XPATH, value='//*[@id="signIn"]')
            login.click()
            time.sleep(4)
            return redirect('upload_pdf')

    else:
        form = DocumentForm()
    return render(request, 'app/model_form_upload.html', {
        'form': form
    })

def upload_pdf(request):
    global random_id
    random_id = random.randint(0,9999)
    global login_select
    global select
    global excelfile
    global files_id
    files_id =[]
    if request.method == 'POST':
        form = DocumentForm2(request.POST,request.POST)
        otp = request.POST['otp']
        file = request.FILES['file']
        # files = request.FILES.getlist('files')
        if form.is_valid():
            # for f in files:
            file_instance = Document2()
            file_instance.types = request.POST['types']
            file_instance.category = request.POST['category']
            file_instance.identity = random_id
            file_instance.document_excel = file.read()
            # filename = f.name
            # file_instance.file_name = filename.split('.')[0]
            # file_instance.document_pdf = f.read()
            file_instance.save()
            # files_id.append(file_instance.id)
            idd = file_instance.id
            document2call = Document2.objects.get(id = idd)
            excelfile = document2call.document_excel
            login_select = document2call.types
            select = document2call.category
            otp = driver.find_element(by=By.XPATH, value='//*[@id="loginUserID"]').send_keys(otp)
            driver.implicitly_wait(40)
            continu = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-plastic/div/app-admin-login/div/div/div/div[2]/div[2]/div/div[2]/form/div[2]/button').click()
            return redirect('main')
    else:
        form = DocumentForm2()
    return render(request,'app/upload_pdf.html', {
        'form': form})

def main(request):
    print('testtttttttttttttttt')
    root = tk.Tk()
    file2 = fd.askopenfilenames(parent=root, title='Choose a pdf files')
    root.destroy()
    df1 = pd.DataFrame(list(file2), columns =['file_path'])
    df1['file_name']=0
    time.sleep(10)
    for i in range(len(df1)):
        file2 = df1['file_path'][i].split("/")
        file_name = file2[-1].split(".")[0]
        df1['file_name'][i]=file_name
    start = time.time()
    if(login_select.lower() =="producer"):
        producer(driver,excelfile,select,df1)
    elif(login_select.lower() =="brand owner"):
        brand_owner(driver,excelfile,df1)
    elif(login_select.lower() =="importer"):
        importer(driver,excelfile,select,df1)
    else:
        print("PLEASE ENTER CORRECT CHOICE")
        pass
    # member = Document2.objects.get(identity=random_id)
    # member.delete.all()
    end = time.time()
    print("The time of execution of program is :",
        (end-start), "s")    

    return redirect('model_form_upload')