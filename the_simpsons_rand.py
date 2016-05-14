import selenium
from selenium import webdriver as wd
import time
from random import randint

i = 0
# open firefox
b = wd.Firefox()
try:
    while(1):
        season_num = randint(1, 10)
        # problem with 2nd season: needs 'episode' instead of 'episodes' in url
        if (season_num == 2):
            season_url = 'http://watchcartoonsonline.eu/watch-the-simpsons-season-' + str(season_num) + '-full-episode-online-free/'
        else:
            season_url = 'http://watchcartoonsonline.eu/watch-the-simpsons-season-' + str(season_num) + '-full-episodes-online-free/'

        # go to the download site
        b.get(season_url)
        # keep trying to close the popup
        # only for first time going to the site (first episode)
        if (i == 0): 
            # wait for the popup to come
            time.sleep(10)
            while(1):
                try:
                    b.find_element_by_class_name('spu-icon-close').click()
                    i = 1
                    break
                except:
                    pass
        
        # get a list of the links to the episodes
        # the first one is redundant
        # there are 7 more results at the end that aren't to episodes
        ep_links = b.find_elements_by_partial_link_text('The Simpsons Season ' + str(season_num))
        # go to random episode
        ep_links[randint(1, len(ep_links)-7)].click()

        # close current window with episode links
        b.close()
        # switch to actual episode window
        # might want to find way to keep episode link in the same window
        b.switch_to_window(b.window_handles[0])
        b.maximize_window()
        # find the play button (should only be 1) and click it
        b.find_elements_by_class_name('jw-icon-display')[0].click()
# 
#         # sleep for the episode to complete
#         time.sleep(30*60)

        raw_input('Press Enter to go to next episode')
except KeyboardInterrupt:
    # close the browser
    b.quit()

