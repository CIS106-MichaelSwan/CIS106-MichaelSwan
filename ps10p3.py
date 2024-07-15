def compute_out_the_door_price(msrp, make, model, electric_vehicle_code):
    percent_off = 0
    if make == "Honda" and model == "Accord":
        percent_off = 0.10
    elif make == "Toyota" and model == "Rav4":
        percent_off = 0.15
    elif electric_vehicle_code == "Y":
        percent_off = 0.30
    else:
        percent_off = 0.05

    new_msrp = msrp * (1 - percent_off)
    sales_tax = 0.07 * new_msrp
    total = new_msrp + sales_tax
    return total

total_msrp = 0
total_sales_price = 0
r = input("Do you want to run the program? (Y or N): ")
while r == "Y":
        make = input("Enter the make of the car: ")
        model = input("Enter the model of the car: ")
        electric_vehicle_code = input("Is the car electric (Y or N)? ")
        msrp = float(input("Enter the MSRP (sticker price) of the car: "))

        total_msrp += msrp
        out_the_door_price = compute_out_the_door_price(msrp, make, model, electric_vehicle_code)
        total_sales_price += out_the_door_price
        print(f"The out-the-door price of the car is: {out_the_door_price:.2f}")
        r = input("Do you want to run the program again? (Y or N): ")

print(f"Total MSRP of all cars: {total_msrp:.2f}")
print(f"Total sales price of all cars: {total_sales_price:.2f}")