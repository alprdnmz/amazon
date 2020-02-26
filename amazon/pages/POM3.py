class List(object):

    def __init__(self, object):

        self.driver = object


    def click_wishlist(self):
        self.driver.find_element_by_id("add-to-wishlist-button").click()

    def click_wishlist_withproduct(self):
        self.driver.find_element_by_id("atwl-link-to-list-1IA0UU0PQ7XH2").click()




