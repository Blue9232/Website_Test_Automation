"Automatically open a Website (any website) using Selenium, Python & Geckodriver"

from selenium import webdriver
driver = webdriver.Firefox(executable_path="c:\selenium_browser_drivers\geckodriver.exe")
driver.get("https://www.emag.ro")
