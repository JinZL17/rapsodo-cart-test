# Rapsodo Cart Automation Test

This script automates the following flow on the Rapsodo website using Selenium:

1. Navigate to https://rapsodo.com
2. Check if the cart is empty
3. Access the "GOLF" section
4. Click on "SHOP NOW"
5. Select the Mobile Launch Monitor (MLM) product
6. Toggle between product variants to ensure form state is correct
7. Add the product to cart
8. Go to cart and increase quantity to 2
9. Confirm quantity updated successfully

---

## Approach

This script was designed iteratively to overcome the following real-world web automation challenges:

- **Stale elements and dynamic re-rendering**: Shopify refreshes certain DOM elements after actions like clicking the "+" button. To solve this, we re-locate elements each time within loops.
- **Variant selection fallback (optional)**: In some Shopify setups, the default product variant might not register correctly when loading the page. While currently unnecessary, toggling variants before adding to cart is kept as a precaution to ensure the intended variant is selected.
- **Click intercept issues**: JS-based clicks were used (`execute_script`) instead of `.click()` to bypass overlays and animations.
- **Unreliable quantity update**: The quantity doesn’t always update on the first `+` click, so a loop was implemented to click and verify until it reaches `2`.

---

## Prerequisites

- Python 3.7+
- Google Chrome
- ChromeDriver installed (ensure it's on PATH or in the script directory)
- `pip install selenium`

---

## Running the Script

```bash
python rapsodo_cart_test.py
```

The browser will open and walk through the cart process. At the end, it will wait 10 seconds before closing, so you can visually verify that the cart is updated.

---

## Notes

- Quantity updates are confirmed by checking the input field value, not just assuming button clicks worked.

---

## Files

- `rapsodo_cart_test.py` – Main Selenium script
- `README.md` 