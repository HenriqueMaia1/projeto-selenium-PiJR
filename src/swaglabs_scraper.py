from seleniumbase import BaseCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

class SwagLabsTest(BaseCase):

    def login(self):
        self.open("https://www.saucedemo.com/")
        self.type("#user-name", "standard_user")
        self.type("#password", "secret_sauce")
        self.click("#login-button")

    def extract_product_data(self):
        products = self.find_elements(".inventory_item")
        product_list = []
        for product in products:
            name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
            description = product.find_element(By.CLASS_NAME, "inventory_item_desc").text
            price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
            product_list.append({
                "name": name,
                "description": description,
                "price": price
            })
        return product_list

    def add_all_to_cart(self):
        buttons = self.find_elements("button.btn_inventory")
        for button in buttons:
            button.click()

    def checkout(self):
        self.click(".shopping_cart_link")
        self.click("#checkout")
        self.type("#first-name", "Trainee")
        self.type("#last-name", "PiJunior")
        self.type("#postal-code", "31270-901")
        self.click("#continue")

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_info"))
    )

        labels = self.find_elements(".summary_value_label")
        print(f"Qtd labels .summary_value_label: {len(labels)}")
        for i, label in enumerate(labels):
            print(f"Label {i+1}: {label.text}")

        payment = labels[0].text if len(labels) > 0 else "N/A"
        delivery = labels[1].text if len(labels) > 1 else "N/A"
        total = self.find_element(".summary_total_label").text

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "finish"))
    )
        self.click("#finish")

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    )
        confirmation = self.find_element(".complete-header").text

        print("Confirmação da compra:", confirmation)
        self.save_screenshot("screenshot_checkout.png")  

        return {
            "payment": payment,
            "delivery": delivery,
            "total": total,
            "confirmation": confirmation
         }    

    def test_full_flow(self):
        self.login()
        product_data = self.extract_product_data()
        with open("produtos.json", "w", encoding="utf-8") as f:
            json.dump(product_data, f, ensure_ascii=False, indent=4)
        self.add_all_to_cart()
        checkout_info = self.checkout()
        with open("checkout_info.json", "w", encoding="utf-8") as f:
            json.dump(checkout_info, f, ensure_ascii=False, indent=4)
        assert "Thank you for your order!" in checkout_info["confirmation"]
