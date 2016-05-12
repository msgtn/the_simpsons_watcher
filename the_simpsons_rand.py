import selenium
from selenium import webdriver as wd

b = wd.Firefox()
b.get('http://www.watch-episodes.tv/the-simpsons')
season_links = b.find_elements_by_class_name('sn-button')
episode_links = b.find_elements_by_class_name('season')