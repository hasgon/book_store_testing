"""Отображение страницы товара"""
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("https://practice.automationtesting.in/")
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 10)
#
# my_account = driver.find_element_by_link_text("My Account").click()
# login = driver.find_element_by_id("username")
# login.send_keys("chelovek_pavuk@mail.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("Buba-854-")
# login_btn = driver.find_element_by_css_selector("input[value='Login']").click()
# shop = driver.find_element_by_link_text("Shop").click()
# html_book = driver.find_element_by_css_selector("a[data-product_id='181']").click()
# element = driver.find_element_by_css_selector("h1[class='product_title entry-title']")
# element_get_text = element.text
# assert "HTML5 Forms" in element_get_text
# print ("HTML5 Forms есть в загловке")
# driver.quit()
"""количество товаров в категории"""
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("https://practice.automationtesting.in/")
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 10)
#
# my_account = driver.find_element_by_link_text("My Account").click()
# login = driver.find_element_by_id("username")
# login.send_keys("chelovek_pavuk@mail.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("Buba-854-")
# login_btn = driver.find_element_by_css_selector("input[value='Login']").click()
# shop = driver.find_element_by_id("menu-item-40").click()
# html = driver.find_element_by_css_selector("li a[href='https://practice.automationtesting.in/product-category/html/']").click()
# html_counts = driver.find_elements_by_class_name("woocommerce-LoopProduct-link")
# if len(html_counts) == 3:
#     print("в разделе три товара")
# else:
#     print("товаров больше"+str(len(html_counts)))
# driver.quit()
"""сортировка товара"""
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("https://practice.automationtesting.in/")
# from selenium.webdriver.support.select import Select
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 10)
#
# my_account = driver.find_element_by_link_text("My Account").click()
# login = driver.find_element_by_id("username")
# login.send_keys("chelovek_pavuk@mail.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("Buba-854-")
# login_btn = driver.find_element_by_css_selector("input[value='Login']").click()
# shop = driver.find_element_by_id("menu-item-40").click()
# select = driver.find_element_by_class_name("orderby")
# select_default = driver.find_element_by_css_selector("[value='menu_order']")
# select_Check = select_default.get_attribute("selected")
# if select_Check is not None:
#     print("выбрано значение по умолчанию")
# else:
#     print("выбрано другое значение")
# select_status = Select(select)
# select_status.select_by_value("price-desc")
# new_status = driver.find_element_by_css_selector("[value='price-desc']")
# select_new_status = new_status.get_attribute("selected")
# if select_new_status is not None:
#     print("выбран варинт сортировки от большего к меньшему ")
# else:
#     print("выбрано другое значение")
# driver.quit()
"""отображение,скидка товара"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("https://practice.automationtesting.in/")
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 10)
#
# my_account = driver.find_element_by_link_text("My Account").click()
# login = driver.find_element_by_id("username")
# login.send_keys("chelovek_pavuk@mail.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("Buba-854-")
# login_btn = driver.find_element_by_css_selector("input[value='Login']").click()
# shop = driver.find_element_by_id("menu-item-40").click()
# android_book = driver.find_element_by_css_selector(".post-169 h3").click()
# old_price = driver.find_element_by_css_selector(".price > del > span ")
# old_price_text = old_price.text
# new_price = driver.find_element_by_css_selector(".price > ins > span ")
# new_price_text = new_price.text
# assert old_price_text == "₹600.00"
# assert new_price_text == "₹450.00"
# img_book = wait.until(EC.element_to_be_clickable ((By.CSS_SELECTOR, ".images")))
# img_book.click()
# img_close = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# img_close.click()
# driver.quit()
"""проверка цены в корзине"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("https://practice.automationtesting.in/")
# driver.maximize_window()
# driver.implicitly_wait(10)
# wait = WebDriverWait(driver, 10)
#
#
# shop = driver.find_element_by_id("menu-item-40").click()
# add = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[4]/a[2]").click()
# amount = driver.find_element_by_css_selector("li a  span[class='amount']")
# amount_text = amount.text
# assert amount_text == "₹180.00"
# basket = driver.find_element_by_css_selector(".wpmenucart-contents").click()
# subtotal = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".cart-subtotal" ),"180.00"))
# total = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".order-total"),"183.60"))
# driver.quit()
"""работа в корзине"""
# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("https://practice.automationtesting.in/")
# driver.maximize_window()
# driver.implicitly_wait(10)
# wait = WebDriverWait(driver, 10)
#
# shop = driver.find_element_by_id("menu-item-40").click()
# driver.execute_script("window.scrollBy(0,300);")
# add_html5 = driver.find_element_by_css_selector("a[data-product_id='182']").click()
# time.sleep(2)
# add_js = driver.find_element_by_css_selector("a[data-product_id='165'").click()
# driver.find_element_by_css_selector(".wpmenucart-contents").click()
# time.sleep(2)
# delete_one = driver.find_element_by_css_selector("[data-product_id='182']").click()
# undo = driver.find_element_by_link_text("Undo?").click()
# qti = driver.find_element_by_css_selector("div [name='cart[4c5bde74a8f110656874902f07378009][qty]']")
# qti.clear()
# qti.send_keys("3")
# update = driver.find_element_by_css_selector("[value='Update Basket']").click()
# value_box = qti.get_attribute("value")
# assert value_box == "3"
# time.sleep(2)
# apply = driver.find_element_by_css_selector("[value='Apply Coupon']").click()
# coupon = driver.find_element_by_css_selector(".woocommerce-error")
# coupon_text = coupon.text
# assert coupon_text == "Please enter a coupon code."
# driver.quit()
"""покупка товара"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("https://practice.automationtesting.in/")
# driver.maximize_window()
# driver.implicitly_wait(10)
# wait = WebDriverWait(driver, 10)
#
#
# shop = driver.find_element_by_id("menu-item-40").click()
# driver.execute_script("window.scrollBy(0,300);")
# add_html5 = driver.find_element_by_css_selector("a[data-product_id='182']").click()
# time.sleep(2)
# basket = driver.find_element_by_css_selector(".wpmenucart-contents").click()
# check = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".checkout-button.button.alt.wc-forward")))
# check.click()
# check_first_name = wait.until(EC.element_to_be_clickable((By.ID,"billing_first_name")))
# check_first_name.send_keys("Vazya")
# last_name = driver.find_element_by_id("billing_last_name")
# last_name.send_keys("Ara")
# email = driver.find_element_by_id("billing_email")
# email.send_keys("ji.estb@mail.ru")
# number = driver.find_element_by_id("billing_phone")
# number.send_keys("89991113232")
# country_selector = driver.find_element_by_id("select2-chosen-1").click()
# country = driver.find_element_by_css_selector("input[id='s2id_autogen1_search']")
# country.send_keys("albania")
# albania = driver.find_element_by_css_selector(".select2-match").click()
# address_1 =driver.find_element_by_id("billing_address_1")
# address_1.send_keys("stepb")
# city = driver.find_element_by_id("billing_city")
# city.send_keys("manchester city")
# state = driver.find_element_by_id("billing_state")
# state.send_keys("ustal pisatb")
# code = driver.find_element_by_id("billing_postcode")
# code.send_keys("xvatit")
# driver.execute_script("window.scrollBy(0,600);")
# paypall = driver.find_element_by_id("payment_method_cheque").click()
# place = driver.find_element_by_id("place_order").click()
# thank = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".woocommerce-thankyou-order-received"),"Thank you. Your order has been received."))
# payment = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"ul li[class='method']"),"Check Payments"))
# driver.quit()