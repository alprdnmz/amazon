
class Login(object):

    def __init__(self, object):

        self.driver = object




    def enter_mail(self, mail):
        self.driver.find_element_by_id("ap_email").clear
        self.driver.find_element_by_id("ap_email").send_keys(mail)

    def click_continue(self):
        self.driver.find_element_by_id("continue").click()

    def enter_password(self, password):
        self.driver.find_element_by_id("ap_password").clear
        self.driver.find_element_by_id("ap_password").send_keys(password)

    def click_signin(self):
        self.driver.find_element_by_id("signInSubmit").click()



