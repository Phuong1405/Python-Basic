"""
COMP.CS.101 Programming 1
Code template for Paracetamol
VU TU PHUONG NGUYEN
"""
def read_int(prompt):
    """read_int sets the loop while to get the answer"""
    while True:
        answer = int(input(prompt))
        if answer >= 0:
            break

    return answer

def calculate_dose(weight, time, total_dose_24):
    """set the calculation by using If"""

    if total_dose_24 >= 4000:
        return 0
    elif time < 6:
        return 0
    else:
        potential_dose = weight * 15

    if potential_dose + total_dose_24 > 4000:
        return 4000 - total_dose_24
    else:
        return potential_dose

def main():
    weight = read_int("Patient's weight (kg): ")
    time_since_last_dose = read_int("How much time has passed from the previous dose (full hours): ")
    total_last_24 = read_int("The total dose for the last 24 hours (mg): ")

    max_dose = calculate_dose(weight,time_since_last_dose,total_last_24)

    print("The amount of Parasetamol to give to the patient:",max_dose)

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)

if __name__ == "__main__":
  main()