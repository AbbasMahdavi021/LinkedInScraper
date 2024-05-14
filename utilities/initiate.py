from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


from get_linkedin_credentials import get_linkedin_credentials

def initiate():

    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service)

