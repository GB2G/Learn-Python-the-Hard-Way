price = float(input("How much is the sales price?: "))

salesTax = price * 0.0825
total = price - salesTax


print(f"Item price:\t {price}")
print(f"Sales tax:\t {salesTax}")
print(f"Total cost:\t {total}")


