from secret import pwd # importing password from another file secret.py
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class InstaBot:
    def __init__(self, username, pw):

        self.username = username

        # calling webdriver
        self.driver = webdriver.Chrome()

        # opening instagram
        self.driver.get("https://www.instagram.com/")
        sleep(2)

        # //*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a
        self.driver.find_element_by_xpath('//a[contains(text(), "Log in")]').click()
        sleep(5)

        # sending user name and password to the page
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(pw)

        # clicking submit button
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]').click()
        sleep(5)

        # not now for notifications
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        sleep(5)

        # click profile button
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username)).click()
        sleep(3)


    def get_unfollowers(self):

        # following
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        following = self._get_names()

        # followers
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        followers = self._get_names()

        # getting the list of people
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)      


    def _get_names(self):
        sleep(3)
        scroll_box = self.driver.find_element_by_xpath('/html/body/div[4]')
        # /html/body/div[4]
        # WebDriverWait(driver, 10).until(lambda d: d.find_element_by_css_selector('div[role="dialog"]'))
        # # now scroll
        # ht = self.driver.execute_script('''
        #       var fDialog = document.querySelector('div[role="dialog"] .isgrP');
        #     fDialog.scrollTop = fDialog.scrollHeight
        # ''')

        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(4)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']

        # close button
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div[2]/button").click()
        return names


my_bot = InstaBot('shubham_s.o.n.i', pwd)
my_bot.get_unfollowers()