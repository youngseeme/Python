from bmi_utils import calc_bmi, classify_bmi

print("*** BMI 측정 계산기 ***")
weight = float(input("체중(kg)을 입력하세요: "))
height = float(input("신장(cm)을 입력하세요: "))

bmi = calc_bmi(weight, height)
result = classify_bmi(bmi)

print(f"\nBMI 수치: {bmi}")
print(f"건강 상태: {result}")