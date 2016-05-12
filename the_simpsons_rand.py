import selenium
from selenium import webdriver as wd
import time

b = wd.Firefox()
# b.get('http://www.watch-episodes.tv/the-simpsons')
# season_links = b.find_elements_by_class_name('sn-button')
# episode_links = b.find_elements_by_class_name('season')

b.get('http://watchcartoonsonline.eu/watch-the-simpsons-season-1-full-episodes-online-free/')
time.sleep(20)
while(1):
    try:
        b.find_element_by_class_name('spu-icon-close').click()
        break
    except:
        pass
        

ep_links = b.find_elements_by_partial_link_text('The Simpsons Season')
ep_links[1].click()

b.switch_to_window(b.window_handles[1])
b.find_elements_by_class_name('jw-icon-display')[0].click()

