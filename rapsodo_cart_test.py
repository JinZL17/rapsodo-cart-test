from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Setup
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)
driver.maximize_window()

try:
    # Step 1: Go to Rapsodo website
    driver.get("https://rapsodo.com")
    assert "rapsodo.com" in driver.current_url
    print("Step 1: Navigated to Rapsodo.com")

    time.sleep(5)

    # Step 2: Click the cart icon via JavaScript
    cart_icon = driver.find_element(By.XPATH, "//a[contains(@href, '/cart')]")
    driver.execute_script("arguments[0].click();", cart_icon)
    print("Step 2: Click on Cart icon")

    # Step 3: Check if cart is empty
    time.sleep(2)
    body_text = driver.find_element(By.TAG_NAME, "body").text
    if "Your cart is currently empty." in body_text:
        print("Step 3: Cart is empty")
    else:
        print("Step 3: Cart may not be empty or message is different")

    # Step 4: Click "GOLF" link
    golf_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "GOLF")))
    golf_link.click()
    print("Step 4: Clicked GOLF link")

    # Step 5: Click the "SHOP NOW" button
    shop_now = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.hero-slider-button")))
    shop_now.click()
    print("Step 5: Clicked SHOP NOW button")

    # Step 6: Click MLM image to go to product page
    mlm_img_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Mobile Launch Monitor (MLM)']/ancestor::a")))
    driver.execute_script("arguments[0].scrollIntoView(true);", mlm_img_link)
    time.sleep(1)
    mlm_img_link.click()
    print("Step 6: Clicked MLM product image")

    # Step 7: Toggle and re-select correct MLM variant  
    time.sleep(1)
    bundle_variant = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@data-variant, 'bundle')]")))
    driver.execute_script("arguments[0].click();", bundle_variant)
    time.sleep(1)
    mlm_variant = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@data-variant, 'single')]")))
    driver.execute_script("arguments[0].click();", mlm_variant)
    print("Step 7: Toggled and reselected MLM variant")

    # Step 8: Click Add to Cart using full class and JS
    add_to_cart = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.add-to-bag.add-email-to-cart")))
    driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.add-to-bag.add-email-to-cart")))
    driver.execute_script("arguments[0].click();", add_to_cart)
    print("Step 8: Clicked Add to Cart via JS")

    # Step 9: Wait for cart page to load
    wait.until(EC.url_contains("/cart"))
    time.sleep(3)
    print("Step 9: Redirected to cart")

    # Step 10: Increase quantity to 2 with full re-locate loop
    success = False

    for attempt in range(3):
        try:
            plus_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "js-qty__adjust--plus")))
            driver.execute_script("arguments[0].scrollIntoView(true);", plus_button)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", plus_button)
            print(f"Clicked + button (attempt {attempt + 1})")

            time.sleep(2)
            quantity_input = driver.find_element(By.NAME, "updates[]")
            if quantity_input.get_attribute("value") == "2":
                print("Step 10: Quantity successfully set to 2")
                success = True
                break

        except Exception as e:
            print(f"Retry due to: {type(e).__name__}")

    if not success:
        raise Exception("Step 10: Failed to update quantity to 2")

    print("Test Successful: Product added with correct quantity")

finally:
    time.sleep(10)
    driver.quit()
