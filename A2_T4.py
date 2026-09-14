print("Program starting.")
print("Estimate how many minutes you spent on programming...")
print()

time1 = int(input("A1_T1: "))
time2 = int(input("A1_T2: "))
time3 = int(input("A1_T3: "))
time4 = int(input("A1_T4: "))
time5 = int(input("A1_T5: "))
time6 = int(input("A1_T6: "))
time7 = int(input("A1_T7: "))

total_time = time1 + time2 + time3 + time4 + time5 + time6 + time7

print(f"In total you spent {total_time} minutes on programming.")

Average_time = total_time / 7
Average_time = round(Average_time, 2)

print(f"Average per task was {Average_time} min and same rounded to nearest integer {round(Average_time)} min.")

print("Program ending.")