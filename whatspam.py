from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import random
import subprocess

class Whatspam:
    def __init__(self):
        i = 0; count = 1; message = []
        print("Whatspam Start")
        print(message)
        chat = input("[+] Enter the name of the chat > ")
        length_message = int(input("[+] Enter length message > "))

        while (i < length_message):
            msg = input("[+] Enter your message [" + str(count) + "] > ")
            message.append(msg)
            i += 1
            count += 1
        amount = input("[+] Enter message amount > ")
        self.spammer(chat, message, amount, length_message - 1)

    def spammer(self, chat, message, amount, length_message):
        try:
            opt = Options()
            opt.add_argument('--disable-logging')
            opt.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
            driver=webdriver.Chrome(executable_path="includes\chromedriver.exe", chrome_options=opt)
            input("[!] Scan the QR code and press Enter")
            try:
                driver.find_element_by_xpath('//*[@title="{0}"]'.format(chat)).click()
            except:
                subprocess.call("cls", shell=True)
                print("[+] Could not find chat with name: {0}".format(chat))
                exit(0)
            subprocess.call("cls", shell=True)
            count = 0
            print("chat\t\t\tmessage\t\t\tamount\n------------------------------------------------------")
            for i in range(int(amount)):
                k = random.randint(0, length_message)
                driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(message[k])
                sleep(0.300)
                try:
                    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
                    count = count + 1
                except:
                    sleep(0.300)
                    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
                    amount = int(amount) + 1
                print("\r" + str(chat) + "\t\t\t" + str(message[k]) + "\t\t\t" + str(count), end="")

            sleep(15)
            driver.quit()
        except KeyboardInterrupt:
            subprocess.call("cls", shell=True)
            print("[+] Spam stopped! Exit from WhatSpam")

Whatspam()