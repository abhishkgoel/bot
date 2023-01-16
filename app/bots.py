from datetime import datetime
import time
from tkinter import Tk
import tkinter.filedialog as fd
import pandas as pd
from selenium.webdriver.common.by import By
from .models import *

def producer(driver,excelfile,select,df1):
    errors=[]
    
    action = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-producer-list/div[1]/kl-simple-table-with-pagination/div[1]/div/div[1]/table/tbody/tr/td[8]/span/span/em').click()
    time.sleep(1)
    close = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[3]/div/div/div[1]/button/span').click()
    time.sleep(1)
    nxt = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[1]/div/div[3]/div/div/div[2]/div[4]/form/div[4]/button[2]').click()
    # select = input("you want to proceed with?\n a) Plastic Raw Material/Packaging Procured from Non-registered Entity\n b)Plastic Raw material sold to UnRegistered PIBOs\n enter a or b")
    # df1 = pd.DataFrame(list(file2), columns =['file_path'])
    # df1['file_name']=0
    # for i in range(len(df1)):
    #     file2 = df1['file_path'][i].split("/")
    #     file_name = file2[-1].split(".")[0]
    #     df1['file_name'][i]=file_name
    df = pd.read_excel(excelfile)
    df = df.astype(str)
    count=0
    if(select=='sales'):
        for i in range(len(df)):
            driver.implicitly_wait(20)
            #Add button
            try:
                time.sleep(1)
                add = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[1]/div/div[2]/div[1]/div[2]/div[4]/kl-simple-table-with-pagination/div[1]/div/div[1]/table/thead[1]/tr/th/div/div[2]/a[1]').click()
                time.sleep(1)
#             except:
#                 errors.append('add button error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
#                 pass
                #Registration Type
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[1]/div/ng-select/div/div/div[2]/input').send_keys(df['Registration type'][i])
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[1]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                    time.sleep(0.5)
                except:
                    errors.append('registeration error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    pass



                #Name of the Entity unregistred
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[3]/div/input').send_keys(df['Name of Entity'][i])
                except:
                    errors.append('Name of the Entity error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    pass

                #Address
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[4]/div/input').send_keys(df['Address'][i])
                except:
                    errors.append('Name of the Entity error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    pass

                #state
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[5]/div/ng-select/div/div/div[2]/input').send_keys(df['State'][i])
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[5]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                    time.sleep(1)
                except:
                    errors.append('state error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    pass

                #Mobile Number
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[6]/div/input').send_keys(int(df['Mobile Number'][i]))
                except:
                    errors.append('Mobile Number error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    pass

                #Financial Year
                try:
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[9]/div/ng-select/div/div/div[3]/input').send_keys(df['Year'][i])
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[9]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                    time.sleep(0.5)
                except:
                    errors.append('Financial Year error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    pass

                #GST
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[10]/div/input').send_keys(df['GST number'][i])
                except:
                    errors.append('GST error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    pass

                #Bank Account No
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[11]/div/input').send_keys(int(df['Bank account no'][i]))
                except:
                    errors.append('Bank Account No error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    pass

                #IFSC Code
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[12]/div/input').send_keys(df['IFSC code'][i])
                except:
                    errors.append('IFSC Code error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    pass

                #GST Paid
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[13]/div/input').send_keys(int(df['GST paid'][i]))
                except:
                    errors.append('GST Paid error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    pass

                #Total Quantity (Tons)
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[2]/div[1]/div/input').send_keys(df['Quantity (TPA)'][i])
                except:
                    errors.append('Total Quantity error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    pass


                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[2]/div[3]/div/input').send_keys(df['Invoice number'][i])
                except:
                    errors.append('Invoice number error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    pass

                #Upload Invoice / GST E-Invoice
                try:
                    upload_file = driver.find_element(by=By.XPATH, value='//*[@id="invoiceID"]')
                    pdf_file_index = df1[df1['file_name']==df['pdf_filename'][i]].index[0]
                    pdf_file = df1['file_path'][pdf_file_index]
                    # pdf_file = Document2.objects.get(file_name=df['pdf_filename'][i]).document_pdf
                    upload_file.send_keys(pdf_file)
                    time.sleep(1)
                except:
                    errors.append('Invoice upload error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    pass

                #Category of Plastic
                try:
                    if(df['Category of Plastic'][i].lower()=='cat iv'):
                        driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[8]/div/ng-select/div/div/div[2]/input').send_keys(df['Category of Plastic'][i])
                        driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[8]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                        time.sleep(0.5)
                    else:
                        time.sleep(1)
                        driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[8]/div/ng-select/div/div/div[2]/input').send_keys(df['Category of Plastic'][i])
                        time.sleep(1)
                        driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[8]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                        time.sleep(0.5)
                #% of recycled plastic packaging
                        try:
                            driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[2]/div[2]/div/input').send_keys(int(df['% of recycled plastic packaging content'][i]))
                        except:
                            errors.append('% of recycled plastic packaging error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                            pass    
                except:
                    errors.append('Category of Plastic error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    pass

                #Entity Type
                try:
                    if(df['Entity type'][i].lower()=='brand owner' and df['Category of Plastic'][i].lower()=='cat i'):
                        driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[2]/div/ng-select/div/div/div[2]/input').send_keys(df['Entity type'][i])
                        driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[2]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                        time.sleep(1)
                        #Cat-1 Container Capacity
                        driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[9]/div/ng-select/div/div/div[2]/input').send_keys(df['Cat-1 Container Capacity'][i])
                        time.sleep(0.5)
                        driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[9]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                        time.sleep(1)
                    else:
                        driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[2]/div/ng-select/div/div/div[2]/input').send_keys(df['Entity type'][i])
                        driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[2]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                        time.sleep(1)

                except:
                    errors.append('Entity Type error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    pass

                #Plastic Material Type
                try:
                    if(df['Plastic material type'][i].lower()=='others'):
                        driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[7]/div/ng-select/div/div/div[2]/input').send_keys(df['Plastic material type'][i])
                        driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[7]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                        time.sleep(0.5)
                        #Other Plastic Material Type
                        driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[8]/div/input').send_keys(df['Other Plastic Material Type'][i])
                    else:
                        driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[7]/div/ng-select/div/div/div[2]/input').send_keys(df['Plastic material type'][i])
                        driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[7]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                        time.sleep(0.5)
                except:
                    errors.append('Plastic Material Type error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    pass
            
                #Submit
                try:
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[3]/button').click()
                    time.sleep(0.5)
                except:
                    errors.append('Submit error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    pass

                #Confirm
                try:
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[2]/app-pibo-material-procurement-form-sales/div/div/div/div[3]/button[2]').click()
                    time.sleep(1)
                    add = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[1]/div/div[2]/div[1]/div[2]/div[4]/kl-simple-table-with-pagination/div[1]/div/div[1]/table/thead[1]/tr/th/div/div[2]/a[1]').click()
                    time.sleep(0.5)
                    pop = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/kl-toastr/toaster-container/div/div/button').click()
                    close = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[1]/button/span').click()

                except:
                    try:
                        errors.append('Confirm error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                        pop = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/kl-toastr/toaster-container/div/div/button').click()
                        close = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[1]/button/span').click()
                        pass
                    except:
                        close = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[1]/button/span').click()
                        pass
                    
            except:
                errors.append('add button error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                pass




    #----------------------------------------------------------------------------------------------------------------------    
    #----------------------------------------------------------------------------------------------------------------------    
    #----------------------------------------------------------------------------------------------------------------------     
    elif(select=='procurement'):
        df['Date of procurement']=df['Date of procurement'].astype(str)
        df['Date of procurement'] = df['Date of procurement'].apply(lambda x: x.replace("-", "/"))
        #plastic raw material/packaging procured
        for i in range(len(df)):
            driver.implicitly_wait(30)
            
            #Add button
            try:
                r_type = driver.find_element(by=By.XPATH, value='//*[@id="simple-table-with-pagination"]/thead[1]/tr/th/div/div[2]/a[1]').click()
                time.sleep(0.3)
                r_click = driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div/div/ng-select/div/div/div[2]/input').send_keys('unregistered')
                time.sleep(0.3)
                r_select = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()

#             except:
#                 errors.append('add button error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
#                 pass

                #Entity Type
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[2]/div/ng-select/div/div/div[2]/input').send_keys(df['Entity Type'][i])
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[2]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                    time.sleep(1)
                except:
                    errors.append('Entity Type error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    pass

                #Name of the Entity unregistred
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[3]/div/input').send_keys(df['Name of Entity'][i])
                    #driver.find_element(by=By.XPATH, value='').click()
                except:
                    errors.append('Name of the Entity error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    pass

                #state
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[4]/div/ng-select/div/div/div[2]/input').send_keys(df['State'][i])
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[4]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                    time.sleep(1)
                except:
                    errors.append('state error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    pass

                #Address
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[5]/div/input').send_keys(df['Address'][i])
                except:
                    errors.append('Name of the Entity error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    pass

                #Mobile Number
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[6]/div/input').send_keys(int(df['Mobile Number'][i]))
                except:
                    errors.append('Mobile Number error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    pass

                #Category of Plastic
                try:
                    if(df['Category of Plastic'][i].lower()=='cat iv'):
                        driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[8]/div/ng-select/div/div/div[2]/input').send_keys(df['Category of Plastic'][i])
                        driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[8]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                        time.sleep(0.5)
                    else:
                        driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[8]/div/ng-select/div/div/div[2]/input').send_keys(df['Category of Plastic'][i])
                        time.sleep(0.5)
                #% of recycled plastic packaging
                        try:
                            driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[12]/div/input').send_keys(int(df['Recycled Plastic %'][i]))
                        except:
                            errors.append('% of recycled plastic packaging error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                            pass    
                except:
                    errors.append('Category of Plastic error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    pass

                #Financial Year
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[9]/div/ng-select/div/div/div[3]/input').send_keys(df['Financial Year'][i])
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[9]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                    time.sleep(0.5)
                except:
                    errors.append('Financial Year error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    pass

                #DATE
                try:
                    datetime0 = datetime.datetime.strptime(df['Date of procurement'][0], '%Y/%m/%d')
                    datetime1 = datetime0.date()
                    datetime2 = datetime.date.strftime(datetime1, "%d-%m-%Y")
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[10]/div/input').send_keys(datetime2)
                except:
                    errors.append('GST error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    pass

                #Total Plastic Quantity
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[11]/div/input').send_keys(df['Quantity (TPA)'][i])
                except:
                    errors.append('GST error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    pass

                #GST
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[13]/div/input').send_keys(df['GST Number'][i])
                except:
                    errors.append('GST error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    pass

                #GST Paid
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[14]/div/input').send_keys(int(df['GST Paid'][i]))
                except:
                    errors.append('GST Paid error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    pass

                #Invoice number
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[15]/div/input').send_keys(df['Invoice Number'][i])
                except:
                    errors.append('Invoice number error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    pass

                #Upload Invoice / GST E-Invoice
                try:
                    upload_file = driver.find_element(by=By.XPATH, value='//*[@id="invoiceID"]')
                    pdf_file_index = df1[df1['file_name']==df['pdf_filename'][i]].index[0]
                    pdf_file = df1['file_path'][pdf_file_index]
                    # pdf_file = Document2.objects.get(file_name=df['pdf_filename'][i])
                    upload_file.send_keys(pdf_file)
                    time.sleep(1)

                except:
                    errors.append('Invoice upload error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    pass

                #Plastic Material Type
                try:
                    time.sleep(1)
                    if(df['Plastic Material Type'][i].lower()=='others'):
                        driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[7]/div/ng-select/div/div/div[2]/input').send_keys(df['Plastic Material Type'][i])
                        driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[7]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                        time.sleep(0.5)
                        #Other Plastic Material Type
                        driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[8]/div/input').send_keys(df['Other Plastic Material Type'][i])
                    else:
                        driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[7]/div/ng-select/div/div/div[2]/input').send_keys(df['Plastic Material Type'][i])
                        driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[7]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                        time.sleep(0.5)
                except:
                    errors.append('Plastic Material Type error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    pass

                #Submit
                try:
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/button').click()
                    time.sleep(1)
                except:
                    errors.append('Submit error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
                    pass
            except:
                errors.append('add button error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                pass

    if(len(errors)>0):
        print(errors)
    else:
        print("ALL DATA INPUT SUCCESS")








# Brand Owner Bot


def brand_owner(driver,excelfile,df1):
    errors=[]
    # df1 = pd.DataFrame(list(file2), columns =['file_path'])
    # df1['file_name']=0
    # for i in range(len(df1)):
    #     file2 = df1['file_path'][i].split("/")
    #     file_name = file2[-1].split(".")[0]
    #     df1['file_name'][i]=file_name
    df = pd.read_excel(excelfile)
    df = df.astype(str)
    df['Date of procurement']=df['Date of procurement'].astype(str)
    df['Date of procurement'] = df['Date of procurement'].apply(lambda x: x.replace("-", "/"))
    driver.implicitly_wait(30)
    continu = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-bo-list/div[1]/div[1]/kl-simple-table-with-pagination/div[1]/div/div[1]/table/tbody/tr/td[8]/span/span/em').click()
    time.sleep(0.5)
    action = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[3]/div/div/div[1]/button/span').click()
    time.sleep(0.5)
    nxt = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[1]/div/div[3]/div/div/div[2]/div[4]/form/div[4]/button[2]').click()
    for i in range(len(df)):
        driver.implicitly_wait(30)
        #Add button
        try:
            time.sleep(1)
            r_type = driver.find_element(by=By.XPATH, value='//*[@id="simple-table-with-pagination"]/thead[1]/tr/th/div/div[2]/a[1]').click()
            r_click = driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div/div/ng-select/div/div/div[2]/input').send_keys('unregistered')
            r_select = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()

        except:
            errors.append('add button error')
            break



        #Name of the Entity unregistred
        try:
            driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[3]/div/input').send_keys(df['Name of Entity'][i])
            #driver.find_element(by=By.XPATH, value='').click()
        except:
            errors.append('Name of the Entity error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
            driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
            pass

        #state
        try:
            driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[4]/div/ng-select/div/div/div[2]/input').send_keys(df['State'][i])
            driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[4]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
            time.sleep(1)
        except:
            errors.append('state error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
            driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
            pass

        #Address
        try:
            driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[5]/div/input').send_keys(df['Address'][i])
        except:
            errors.append('Name of the Entity error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
            driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
            pass

        #Mobile Number
        try:
            driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[6]/div/input').send_keys(int(df['Mobile Number'][i]))
        except:
            errors.append('Mobile Number error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
            driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
            pass



        #Financial Year
        try:
            driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[9]/div/ng-select/div/div/div[2]/input').send_keys(df['Financial Year'][i])
            driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[9]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
            time.sleep(0.5)
        except:
            errors.append('Financial Year error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
            driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
            pass

        #DATE
        try:
            datetime0 = datetime.datetime.strptime(df['Date of procurement'][0], '%Y/%m/%d')
            datetime1 = datetime0.date()
            datetime2 = datetime.date.strftime(datetime1, "%d-%m-%Y")
            driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[10]/div/input').send_keys(datetime2)
        except:
            errors.append('GST error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
            driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
            pass

        #Total Plastic Quantity
        try:
            driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[11]/div/input').send_keys(df['Quantity (TPA)'][i])
        except:
            errors.append('GST error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
            driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
            pass

        #GST
        try:
            driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[13]/div/input').send_keys(df['GST Number'][i])
        except:
            errors.append('GST error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
            driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
            pass

        #GST Paid
        try:
            driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[14]/div/input').send_keys(int(df['GST Paid'][i]))
        except:
            errors.append('GST Paid error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
            driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
            pass

        #Invoice number
        try:
            driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[15]/div/input').send_keys(df['Invoice Number'][i])
        except:
            errors.append('Invoice number error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
            driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
            pass

        #Upload Invoice / GST E-Invoice
        try:
            upload_file = driver.find_element(by=By.XPATH, value='//*[@id="invoiceID"]')
            pdf_file_index = df1[df1['file_name']==df['pdf_filename'][i]].index[0]
            pdf_file = df1['file_path'][pdf_file_index]
            # pdf_file = Document2.objects.get(file_name=df['pdf_filename'][i])
            upload_file.send_keys(pdf_file)
            time.sleep(1)

        except:
            errors.append('Invoice upload error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
            driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
            pass

        #Category of Plastic
        try:
            if(df['Category of Plastic'][i].lower()=='cat iv'):
                driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[8]/div/ng-select/div/div/div[2]/input').send_keys(df['Category of Plastic'][i])
                driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[8]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                time.sleep(0.5)
            else:
                driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[8]/div/ng-select/div/div/div[2]/input').send_keys(df['Category of Plastic'][i])
                driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[8]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                time.sleep(0.5)
        #% of recycled plastic packaging
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[12]/div/input').send_keys(int(df['Recycled Plastic %'][i]))
                except:
                    errors.append('% of recycled plastic packaging error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()                    
                    pass    
        except:
            errors.append('Category of Plastic error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
            driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
            pass

        #Entity Type
        try:
            if(df['Category of Plastic'][i].lower()=='cat i'):
                driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[2]/div/ng-select/div/div/div[2]/input').send_keys(df['Entity Type'][i])
                driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[2]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                time.sleep(1)
                #Cat-1 Container Capacity
                driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[9]/div/ng-select/div/div/div[2]/input').send_keys(df['Cat-1 Container Capacity'][i])
                driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[9]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                time.sleep(1)
            else:
                driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[2]/div/ng-select/div/div/div[2]/input').send_keys(df['Entity Type'][i])
                driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[2]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                time.sleep(1)

        except:
            errors.append('Entity Type error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
            driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[1]/button').click()
            pass

        #Plastic Material Type
        try:
            time.sleep(1)
            if(df['Plastic Material Type'][i].lower()=='others'):
                driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[7]/div/ng-select/div/div/div[2]/input').send_keys(df['Plastic Material Type'][i])
                driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[7]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                time.sleep(0.5)
                #Other Plastic Material Type
                driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[8]/div/input').send_keys(df['Other Plastic Material Type'][i])
                time.sleep(1)
                try:
                    #financial year and date
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[10]/div/ng-select/div/div/div[3]/input').send_keys(df['Financial Year'][i])
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[10]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                    time.sleep(0.5)
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[11]/div/input').send_keys(datetime2)
                except:
                    pass
            else:
                driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[7]/div/ng-select/div/div/div[2]/input').send_keys(df['Plastic Material Type'][i])
                driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[7]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                time.sleep(0.5)
        except:
            errors.append('Plastic Material Type error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
            driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
            pass

        try:
            if(df['Plastic Material Type'][i].lower()!='others'):
                driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[9]/div/ng-select/div/div/div[3]/input').send_keys(df['Financial Year'][i])
                driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[9]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                time.sleep(0.5)
                driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[10]/div/input').send_keys(datetime2)
            else:
                pass
        except:
            pass

        #Submit
        try:
            driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/button').click()
            time.sleep(1)
        except:
            errors.append('Submit error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
            driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
            pass






# Importer Bot

def importer(driver,excelfile,select,df1):
    errors=[]
    action = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-importer-list/div[1]/kl-simple-table-with-pagination/div[1]/div/div[1]/table/tbody/tr/td[8]/span/span/em').click()
    time.sleep(1)
    close = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[3]/div/div/div[1]/button/span').click()
    time.sleep(1)
    nxt = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[1]/div/div[3]/div/div/div[2]/div[4]/form/div[4]/button[2]').click()
    # select = input("you want to proceed with?\n a) Plastic Raw Material/Packaging Procured from Non-registered Entity\n b)Plastic Raw material sold to UnRegistered PIBOs\n enter a or b")
    # df1 = pd.DataFrame(list(file2), columns =['file_path'])
    # df1['file_name']=0
    # for i in range(len(df1)):
    #     file2 = df1['file_path'][i].split("/")
    #     file_name = file2[-1].split(".")[0]
    #     df1['file_name'][i]=file_name
    df = pd.read_excel(excelfile)
    df = df.astype(str)
    count=0
    try:
        if(select=='sales'):
            for i in range(len(df)):
                driver.implicitly_wait(30)
                #Add button
                try:
                    time.sleep(1)
                    add = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[1]/div/div[2]/div[1]/div/div[4]/kl-simple-table-with-pagination/div[1]/div/div[1]/table/thead[1]/tr/th/div/div[2]/a[1]').click()
                    time.sleep(1)
                except:
                    errors.append('add button error')
                    break
                #Registration Type
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[1]/div/ng-select/div/div/div[2]/input').send_keys(df['Registration type'][i])
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[1]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                    time.sleep(0.5)
                except:
                    errors.append('registeration error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[1]/button').click()
                    pass



                #Name of the Entity unregistred
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[3]/div/input').send_keys(df['Name of Entity'][i])
                    #driver.find_element(by=By.XPATH, value='').click()
                except:
                    errors.append('Name of the Entity error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[1]/button').click()
                    pass

                #Address
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[4]/div/input').send_keys(df['Address'][i])
                except:
                    errors.append('Name of the Entity error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[1]/button').click()
                    pass

                #state
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[5]/div/ng-select/div/div/div[2]/input').send_keys(df['State'][i])
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[5]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                    time.sleep(1)
                except:
                    errors.append('state error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[1]/button').click()
                    pass

                #Mobile Number
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[6]/div/input').send_keys(int(df['Mobile Number'][i]))
                except:
                    errors.append('Mobile Number error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[1]/button').click()
                    pass

                #Financial Year
                try:
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[9]/div/ng-select/div/div/div[3]/input').send_keys(df['Year'][i])
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[9]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                    time.sleep(0.5)
                except:
                    errors.append('Financial Year error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[1]/button').click()
                    pass

                #GST
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[10]/div/input').send_keys(df['GST number'][i])
                except:
                    errors.append('GST error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[1]/button').click()
                    pass

                #Bank Account No
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[11]/div/input').send_keys(int(df['Bank account no'][i]))
                except:
                    errors.append('Bank Account No error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[1]/button').click()
                    pass

                #IFSC Code
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[12]/div/input').send_keys(df['IFSC code'][i])
                except:
                    errors.append('IFSC Code error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[1]/button').click()
                    pass

                #GST Paid
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[13]/div/input').send_keys(int(df['GST paid'][i]))
                except:
                    errors.append('GST Paid error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[1]/button').click()
                    pass

                #Total Quantity (Tons)
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[2]/div[1]/div/input').send_keys(df['Quantity (TPA)'][i])
                except:
                    errors.append('Total Quantity error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[1]/button').click()
                    pass



                #Invoice number
                #import random
                #a = (random.randint(0,9999))
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[2]/div[2]/div/input').send_keys(df['Invoice number'][i])
                except:
                    errors.append('Invoice number error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[1]/button').click()
                    pass

                #Upload Invoice / GST E-Invoice
                try:
                    upload_file = driver.find_element(by=By.XPATH, value='//*[@id="invoiceID"]')
                    pdf_file_index = df1[df1['file_name']==df['pdf_filename'][i]].index[0]
                    pdf_file = df1['file_path'][pdf_file_index]
                    # pdf_file = Document2.objects.get(file_name=df['pdf_filename'][i])
                    upload_file.send_keys(pdf_file)
                    time.sleep(1)
                except:
                    errors.append('Invoice upload error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[1]/button').click()
                    pass

                #Category of Plastic
                try:
                    if(df['Category of Plastic'][i].lower()=='cat iv'):
                        driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[8]/div/ng-select/div/div/div[2]/input').send_keys(df['Category of Plastic'][i])
                        driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[8]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                        time.sleep(0.5)
                    else:
                        time.sleep(1)
                        driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[8]/div/ng-select/div/div/div[2]/input').send_keys(df['Category of Plastic'][i])
                        time.sleep(1)
                        driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[8]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                        time.sleep(0.5)
                #% of recycled plastic packaging
                        try:
                            driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[2]/div[2]/div/input').send_keys(int(df['% of recycled plastic packaging content'][i]))
                        except:
                            errors.append('% of recycled plastic packaging error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                            driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[1]/button').click()
                            pass    
                except:
                    errors.append('Category of Plastic error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[1]/button').click()
                    pass

                #Entity Type
                try:
                    if(df['Entity type'][i].lower()=='brand owner' and df['Category of Plastic'][i].lower()=='cat i'):
                        driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[2]/div/ng-select/div/div/div[2]/input').send_keys(df['Entity type'][i])
                        driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[2]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                        time.sleep(1)
                        #Cat-1 Container Capacity
                        driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[9]/div/ng-select/div/div/div[2]/input').send_keys(df['Cat-1 Container Capacity'][i])
                        driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[9]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                        time.sleep(1)
                    else:
                        driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[2]/div/ng-select/div/div/div[2]/input').send_keys(df['Entity type'][i])
                        driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[2]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                        time.sleep(1)

                except:
                    errors.append('Entity Type error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[1]/button').click()
                    pass


                #Plastic Material Type
                try:
                    if(df['Plastic material type'][i].lower()=='others'):
                        driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[7]/div/ng-select/div/div/div[2]/input').send_keys(df['Plastic material type'][i])
                        driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[7]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                        time.sleep(0.5)
                        #Other Plastic Material Type
                        driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[8]/div/input').send_keys(df['Other Plastic Material Type'][i])
                    else:
                        driver.find_element(by=By.XPATH, value='//*[@id="modal8c8d"]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[7]/div/ng-select/div/div/div[2]/input').send_keys(df['Plastic material type'][i])
                        driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[1]/div[7]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                        time.sleep(0.5)
                except:
                    errors.append('Plastic Material Type error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[1]/button').click()
                    pass

                #Submit
                try:
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[2]/app-pibo-material-procurement-form-sales/form/div[3]/button').click()
                    time.sleep(0.5)
                except:
                    errors.append('Submit error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[1]/button').click()
                    pass
                #Confirm
                try:
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[2]/app-pibo-material-procurement-form-sales/div/div/div/div[3]/button[2]').click()
                    time.sleep(1)
                    add = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[1]/div/div[2]/div[1]/div/div[4]/kl-simple-table-with-pagination/div[1]/div/div[1]/table/thead[1]/tr/th/div/div[2]/a[1]').click()
                    time.sleep(0.5)
                    pop = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/kl-toastr/toaster-container/div/div/button').click()
                    close = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[1]/button/span').click()

                except:
                    errors.append('Confirm error in-'+str(df['Invoice number'][i])+'-row-'+str(i+1))
                    pop = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/kl-toastr/toaster-container/div/div/button').click()
                    close = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[6]/div/div/div[1]/button/span').click()
                    pass


        #----------------------------------------------------------------------------------------------------------------------    
        #----------------------------------------------------------------------------------------------------------------------    
        #----------------------------------------------------------------------------------------------------------------------     
        elif(select=='procurement'):
            df['Date of procurement']=df['Date of procurement'].astype(str)
            df['Date of procurement'] = df['Date of procurement'].apply(lambda x: x.replace("-", "/"))
            #plastic raw material/packaging procured
            for i in range(len(df)):
                driver.implicitly_wait(30)
                #Add button
                try:
                    time.sleep(0.5)
                    r_type = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[1]/div/div[2]/div[1]/div/div[2]/kl-simple-table-with-pagination/div[1]/div/div[1]/table/thead[1]/tr/th/div/div[2]/a[1]').click()
                    time.sleep(0.5)
                    r_click = driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div/div/ng-select/div/div/div[2]/input').send_keys('unregistered')
                    time.sleep(0.5)
                    r_select = driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()

                except:
                    errors.append('add button error')
                    break

                #Entity Type
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[2]/div/ng-select/div/div/div[2]/input').send_keys(df['Entity Type'][i])
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[2]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                    time.sleep(1)
                except:
                    errors.append('Entity Type error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
                    pass

                #Name of the Entity unregistred
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[3]/div/input').send_keys(df['Name of Entity'][i])
                    #driver.find_element(by=By.XPATH, value='').click()
                except:
                    errors.append('Name of the Entity error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
                    pass

                #country
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[4]/ng-select/div/div/div[2]/input').send_keys(df['Country'][i])
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[4]/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                    time.sleep(1)
                except:
                    errors.append('Country error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
                    pass

                #Address
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[5]/div/input').send_keys(df['Address'][i])
                except:
                    errors.append('Name of the Entity error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
                    pass

                #Mobile Number
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[6]/div/input').send_keys(int(df['Mobile Number'][i]))
                except:
                    errors.append('Mobile Number error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
                    pass

                #Category of Plastic
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[8]/div/ng-select/div/div/div[2]/input').send_keys(df['Category of Plastic'][i])
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[8]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                    time.sleep(0.5)
                except:
                    errors.append('Category of Plastic error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
                    pass

                #Financial Year
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[9]/div/ng-select/div/div/div[3]/input').send_keys(df['Financial Year'][i])
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[9]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                    time.sleep(0.5)
                except:
                    errors.append('Financial Year error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()
                    pass

                #DATE
                try:
                    datetime0 = datetime.datetime.strptime(df['Date of procurement'][0], '%Y/%m/%d')
                    datetime1 = datetime0.date()
                    datetime2 = datetime.date.strftime(datetime1, "%d-%m-%Y")
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[10]/div/input').send_keys(datetime2)
                except:
                    errors.append('GST error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
                    pass

                #Total Plastic Quantity
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[11]/div/input').send_keys(df['Quantity (TPA)'][i])
                except:
                    errors.append('GST error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
                    pass

                #Invoice number
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[12]/div/input').send_keys(df['Invoice Number'][i])
                except:
                    errors.append('Invoice number error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
                    pass

                #Upload Invoice / GST E-Invoice
                try:
                    upload_file = driver.find_element(by=By.XPATH, value='//*[@id="invoiceID"]')
                    pdf_file_index = df1[df1['file_name']==df['pdf_filename'][i]].index[0]
                    pdf_file = df1['file_path'][pdf_file_index]
                    # pdf_file = Document2.objects.get(file_name=df['pdf_filename'][i])
                    upload_file.send_keys(pdf_file)
                    time.sleep(1)

                except:
                    errors.append('Invoice upload error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
                    pass

                #Plastic Material Type
                try:
                    time.sleep(1)
                    if(df['Plastic Material Type'][i].lower()=='others'):
                        driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[7]/div/ng-select/div/div/div[2]/input').send_keys(df['Plastic Material Type'][i])
                        driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[7]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                        time.sleep(0.5)
                        #Other Plastic Material Type
                        driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[8]/div/input').send_keys(df['Other Plastic Material Type'][i])
                    else:
                        driver.find_element(by=By.XPATH, value='//*[@id="modal8a8b"]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[7]/div/ng-select/div/div/div[2]/input').send_keys(df['Plastic Material Type'][i])
                        driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/div/div[7]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]').click()
                        time.sleep(0.5)
                except:
                    errors.append('Plastic Material Type error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
                    pass

                #Submit
                try:
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[2]/app-pibo-material-procurement-form/div/form/button').click()
                    time.sleep(1)
                except:
                    errors.append('Submit error in-'+str(df['Invoice Number'][i])+'-row-'+str(i+1))
                    driver.find_element(by=By.XPATH, value='/html/body/app-root/app-epr/app-brand-owner-application/div[5]/div/div/div[1]/button/span').click()            
                    pass
    except:
        print(i,' records inserted ,',len(df)-i,' records left to insert')

    if(len(errors)>0):
        print(errors)
    else:
        print("ALL DATA INPUT SUCCESS")




