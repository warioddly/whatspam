from selenium import webdriver
from time import sleep
import subprocess

class Whatspam:
    def __init__(self):
        print("Whatspam Start")
        sleep(3)
        chat = input("[+] Enter the name of the chat > ")
        message = input("[+] Enter your message > ")
        amount = input("[+] Enter message amount > ")
        self.spammer(chat, message, amount)

    def spammer(self, chat, message, amount):
        try:
            driver = webdriver.Chrome()
            driver.get("https://web.whatsapp.com/")
            input("[!] Scan the QR code and press Enter")
            try:
                driver.find_element_by_xpath('//*[@title="{0}"]'.format(chat)).click()
            except:
                subprocess.call("cls", shell=True)
                print("[+] Could not find chat with name: {0}".format(chat))
                exit(0)
            driver.find_element_by_class_name("DuUXI").click()
            subprocess.call("cls", shell=True)
            count = 0
            print("chat\t\t\tmessage\t\t\tamount\n------------------------------------------------------")
            for i in range(int(amount)):
                driver.find_element_by_xpath('//*[@class="DuUXI"]').send_keys(message)
                sleep(0.300)
                try:
                    driver.find_element_by_class_name("_2Ujuu").click()
                    count = count + 1
                except:
                    amount = int(amount) + 1
                    pass
                    print("\r" + str(chat) + "\t\t\t" + str(message) + "\t\t\t" + str(count), end="")
            sleep(15)
            driver.quit()
        except KeyboardInterrupt:
            subprocess.call("cls", shell=True)
            print("[+] Spam stopped! Exit from WhatSpam")

Whatspam()