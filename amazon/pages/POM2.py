class Search(object):

    def __init__(self, object):

        self.driver = object


    def search_text(self, searchbox):
        self.driver.find_element_by_id("twotabsearchtextbox").send_keys(searchbox)

