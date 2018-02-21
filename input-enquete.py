from selenium import webdriver
import userdata

driver = webdriver.Chrome()

rank_point = 4; # 入力する評価点数

driver.get("http://jsystem.tu.tokuyama.ac.jp/eval-kamoku/gakusei/index.php");

username_input_area = driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/td/form/div[2]/div[1]/input")
password_input_area = driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/td/form/div[2]/div[2]/input[1]")

username_input_area.send_keys(userdata.username)
password_input_area.send_keys(userdata.password)

driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/td/form/div[2]/div[2]/input[2]").click()

items = driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/td/form/div[2]/table/tbody/tr")

for i in range(1, len(items)+1):
	td = driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/td/form/div[2]/table/tbody/tr["+str(i)+"]/td[1]")
	print(td.text)

	if(td.text != '済'):
		td.click()
		driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/td/form/div[2]/div[4]/input").click()
		
		for i in range(3, 21, 2):
			driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/td/form[2]/div["+str(i)+"]/div[2]/table/tbody/tr/td["+str(rank_point)+"]/input").click()

		driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/td/form[2]/table/tbody/tr/td/input").click()
		driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/td/table[2]/tbody/tr/td[2]/input").click()
		driver.get("http://jsystem.tu.tokuyama.ac.jp/eval-kamoku/gakusei/index.php")