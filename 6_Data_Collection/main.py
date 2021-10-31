from selenium import webdriver
from selenium.webdriver.common.by import By

import os
from uuid import uuid4
chrome = webdriver.Chrome(executable_path="/opt/homebrew/bin/chromedriver")
chrome.get("")


