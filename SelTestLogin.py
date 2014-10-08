# Test case reference 

def test_basicpython(self):
	driver = self.driver
	driver.get(self.base_url + "/")
	driver.find_element_by_link_text("Login").click
	driver.find_element_by_id("edit-name").clear()
	driver.find_element_by_id("edit-name").send_keys("XXXXXXX")
	driver.find_element_by_id("edit-pass").clear()
	driver.find_element_by_id("edit-pass").send_keys("XXXXXXXX")
	driver.find_element_by_id("edit-submit").click
	driver.get(self.base_url + "/")
	
def is_element_present(self, how, what):
	try: self.driver.find_element(by=how, value=what)
	except NoSuchElementException, e: return False
	return True 