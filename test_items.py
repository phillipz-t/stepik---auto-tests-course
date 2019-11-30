from selenium import webdriver

import pytest, time


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_basket(browser):
	browser.get(link)
	time.sleep(30)
	btns = browser.find_elements_by_class_name('btn')
	test_btn = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")

	assert test_btn in btns, "There is no such button"