import finalspc
from selenium import webdriver
import time
option = webdriver.ChromeOptions()
brower = webdriver.Chrome(
    executable_path="C:\my programs/chromedriver.exe")  # exe

brower.get("https://docs.google.com/forms/d/e/1FAIpQLSfnWb3SRYNyAGHuAjdtFEEnJP053_SBRemilQPxQcZqTP2Hnw/viewform?usp=sf_link")
time.sleep(10)
name = brower.find_elements_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
age = brower.find_elements_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
gender = brower.find_elements_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
submit = brower.find_elements_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
name[0].send_keys(finalspc.Name)
age[0].send_keys(finalspc.Age)
gender[0].send_keys(finalspc.Gender)
submit[0].click()
