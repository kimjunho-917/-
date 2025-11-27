def cm_to_inch(cm):
    return cm / 2.54

def inch_to_cm(inch):
    return inch * 2.54

def kg_to_lb(kg):
    return kg * 2.20462262

def lb_to_kg(lb):
    return lb / 2.20462262

if __name__ == "__main__":
    print("=== 단위 변환 프로그램 ===")
    while True:
        print("\n1. cm → inch")
        print("2. inch → cm")
        print("3. kg → lb")
        print("4. lb → kg")
        print("0. 종료")

        menu = input("메뉴 선택: ")

        if menu == "1":
            cm = float(input("cm 입력: "))
            print(f"{cm} cm = {cm_to_inch(cm):.3f} inch")

        elif menu == "2":
            inch = float(input("inch 입력: "))
            print(f"{inch} inch = {inch_to_cm(inch):.3f} cm")

        elif menu == "3":
            kg = float(input("kg 입력: "))
            print(f"{kg} kg = {kg_to_lb(kg):.3f} lb")

        elif menu == "4":
            lb = float(input("lb 입력: "))
            print(f"{lb} lb = {lb_to_kg(lb):.3f} kg")

        elif menu == "0":
            print("프로그램 종료!")
            break