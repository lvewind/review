from selenium import common
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions


driver_url = os.path.join(os.path.abspath(os.getcwd()), "../bin", "msedgedriver.exe")
driver = webdriver.Edge(executable_path=driver_url)
try:
    driver.get("https://cn.bing.com/")
    driver.save_screenshot('bing1.png')
except common.exceptions.WebDriverException:
    print("连接超时")
