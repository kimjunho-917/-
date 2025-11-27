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