# from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
import time
import os

class InstagramBot():

    def __init__(self,username = '',password = ''):
        opt = Options()
        # opt.headless = True
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages','en-US,en') #setting languages to english
        self.browser = webdriver.Firefox(service_log_path=os.devnull,options = opt,firefox_profile=profile)
        self.username = username
        self.password = password
        self.posts = ''
        self.followers = ''
        self.following = ''
        self.bio = ''
        if self.username == '' or self.password =='':
            print('Username or password cannot be empty')
        else:
            try:
                self.browser.get('https://www.instagram.com/accounts/login/')
                time.sleep(2)
            except:
                print('No Internet Connection.')
                self.closeBot()
            try:
                emailInput = self.browser.find_elements_by_css_selector('form input')[0]
                pwdInput = self.browser.find_elements_by_css_selector('form input')[1]
                emailInput.send_keys(self.username)
                pwdInput.send_keys(self.password)
                pwdInput.send_keys(Keys.ENTER)
                # notification disabled
                try:
                    ui.WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".aOOlW.HoLwm"))).click()
                except:
                    pass
                print('Signed In Succesfully')
                self.browser.get('https://www.instagram.com/'+self.username+'/')
                time.sleep(2)
                self.posts = self.browser.find_element_by_xpath('//span/span').text
                self.followers = self.browser.find_element_by_xpath(f'//a[@href = "/{self.username}/followers/"]/span').text
                self.following = self.browser.find_element_by_xpath(f'//a[@href = "/{self.username}/following/"]/span').text
                self.browser.get('https://www.instagram.com/')
                time.sleep(2)
            except:
                print('''               1.No internet connection.
                2.Username Invalid.
                3.Else,report to the developer''') 
    
    
    def isFollowing(self,name):
        try:
            self.browser.get('https://www.instagram.com/'+name+'/')
            time.sleep(2)
            followButton = self.browser.find_element_by_css_selector('button')
            if followButton.text == 'Following':
                return True
            else:
                return False
        except:
            print('''1.No internet connection.
                2.Username Invalid.
                3.Else,report to the developer''')
    

    def followUsername(self,name=''):
        if name=='':
            print('A name is required.')

        else:
            try:
                self.browser.get('https://www.instagram.com/'+name+'/')
                time.sleep(2)
                followButton = self.browser.find_element_by_css_selector('button')
                if followButton.text == 'Following':
                    print('You are already following this account.')
                else:
                    followButton.click()
                    time.sleep(2)
                    print(f'Now you are following {name}.')
            except:
                print('''1.No internet connection.
                2.Username Invalid.
                3.Else,report to the developer''')


    def unfollowUsername(self,name=''):
        if name=='':
            print('A name is required.')
        else:
            try:
                self.browser.get('https://www.instagram.com/'+name+'/')
                time.sleep(2)
                followButton = self.browser.find_element_by_css_selector('button')
                if followButton.text == 'Following':
                    followButton.click()
                    time.sleep(2)
                    self.browser.find_element_by_css_selector('button.aOOlW:nth-child(1)').click()
                    print(f'Unfollowed {name} successfully.')
                else:
                    print('You are not  following this account.')
            except :
                print('''1.No internet connection.
                2.Username Invalid.
                3.Else,report to the developer''')

    
    def followerList(self,name=''):

        '''Fetch the set of people who are your followers.'''
        if name == '':
            self.browser.get('https://www.instagram.com/'+self.username+'/')
            time.sleep(2)

            followersLink = self.browser.find_element_by_css_selector('ul li a')
            followersLink.click()
            time.sleep(2)

            followersList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
            numberOfFollowerInList = len(followersList.find_elements_by_css_selector('li'))

            followersList.click()
            actionChain = webdriver.ActionChains(self.browser)

            while numberOfFollowerInList<int(self.followers):
                actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                numberOfFollowerInList = len(followersList.find_elements_by_css_selector('li'))
            
            followers = []
            for user in followersList.find_elements_by_css_selector('li'):
                userLink = user.find_element_by_css_selector('a').get_attribute('href')
                followers.append(userLink[26:-1])
                if len(followers) == int(self.followers):
                    break
            return followers
        else:
            self.browser.get('https://www.instagram.com/'+name+'/')
            time.sleep(2)
            
            # followButton = self.browser.find_element_by_css_selector('button')
            try:
                self.browser.find_element_by_xpath("//h2[text()='This Account is Private']")
                print('You are not following this account.Also the account is private.')
                return False
            except:
                max1 = self.browser.find_element_by_xpath(f'//a[@href = "/{name}/followers/"]/span').text
                followersLink = self.browser.find_element_by_css_selector('ul li a')
                followersLink.click()
                time.sleep(2)

                followersList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
                numberOfFollowerInList = len(followersList.find_elements_by_css_selector('li'))

                followersList.click()
                actionChain = webdriver.ActionChains(self.browser)

                while numberOfFollowerInList<int(max1):
                    actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                    numberOfFollowerInList = len(followersList.find_elements_by_css_selector('li'))
        
                followers = []
                for user in followersList.find_elements_by_css_selector('li'):
                    userLink = user.find_element_by_css_selector('a').get_attribute('href')
                    followers.append(userLink[26:-1])
                    if len(followers) == int(max1):
                        break
                return followers 
                    
    
    def followingList(self,name = ''):
        '''Fetch the set of people whom you are following.'''
        if name =='':
            self.browser.get('https://www.instagram.com/'+self.username+'/')
            time.sleep(2)

            followingLink = self.browser.find_element_by_partial_link_text('following')
            followingLink.click()
            time.sleep(2)

            followingList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
            numberOfFollowingInList = len(followingList.find_elements_by_css_selector('li'))

            followingList.click()
            actionChain = webdriver.ActionChains(self.browser)

            while numberOfFollowingInList<int(self.following):
                actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                numberOfFollowingInList = len(followingList.find_elements_by_css_selector('li'))
            
            following = []
            for user in followingList.find_elements_by_css_selector('li'):
                userLink = user.find_element_by_css_selector('a').get_attribute('href')
                following.append(userLink[26:-1])
                if len(following) == int(self.following):
                    break
            return following
        else:
            self.browser.get('https://www.instagram.com/'+name+'/')
            time.sleep(2)
            try:
                self.browser.find_element_by_xpath("//h2[text()='This Account is Private']")
                print('You are not following this account.Also the account is private.')
                return False
            except:
                max1 = self.browser.find_element_by_xpath(f'//a[@href = "/{name}/following/"]/span').text
                followingLink = self.browser.find_element_by_partial_link_text('following')
                followingLink.click()
                time.sleep(2)

                followingList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
                numberOfFollowingInList = len(followingList.find_elements_by_css_selector('li'))

                followingList.click()
                actionChain = webdriver.ActionChains(self.browser)

                while numberOfFollowingInList<int(max1):
                    actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                    numberOfFollowingInList = len(followingList.find_elements_by_css_selector('li'))
        
                following = []
                for user in followingList.find_elements_by_css_selector('li'):
                    userLink = user.find_element_by_css_selector('a').get_attribute('href')
                    following.append(userLink[26:-1])
                    if len(following) == int(max1):
                        break
                return following
                    
    
    
    def analysis(self,follower,following):

        '''Return three sets traitor,fans,friends respectively.
            Traitor:-These are the list of people who are not following you back.
            Fans:-These are the list of people whom you are not following back.
            Friends:-These are your friends which are maintaining a symbiotic relationship.'''

        traitor = following.difference(follower)
        fans = follower.difference(following)
        symbiosis = follower.intersection(following)
        return traitor,fans,symbiosis

    
    def closeBot(self):
        self.browser.close()
    
    def __exit__(self,exc_type,exc_value,traceback):
        self.closeBot()
    
    def __repr__(self):
        return f'InstagramBot({self.username},{self.password})'

    def __str__(self):
        return f'{self.username}-{self.password}'