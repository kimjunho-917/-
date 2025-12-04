def sec_to_min(sec):
    return sec / 60

def min_to_sec(minute):
    return minute * 60

def min_to_hour(minute):
    return minute / 60

def hour_to_min(hour):
    return hour * 60

def sec_to_hour(sec):
    return sec / 3600

def hour_to_sec(hour):
    return hour * 3600

if __name__ == "__main__":
    print("=== 시간 단위 변환 프로그램 ===")
    while True:
        print("\n1. 초 → 분")
        print("2. 분 → 초")
        print("3. 분 → 시간")
        print("4. 시간 → 분")
        print("5. 초 → 시간")
        print("6. 시간 → 초")
        print("0. 종료")

        menu = input("메뉴 선택: ")

        if menu == "1":
            sec = float(input("초 입력: "))
            print(f"{sec} 초 = {sec_to_min(sec):.3f} 분")

        elif menu == "2":
            minute = float(input("분 입력: "))
            print(f"{minute} 분 = {min_to_sec(minute):.3f} 초")
        
        elif menu == "3":
            minute = float(input("분 입력: "))
            print(f"{minute} 분 = {min_to_hour(minute):.3f} 시간")

        elif menu == "4":
            hour = float(input("시간 입력: "))
            print(f"{hour} 시간 = {hour_to_min(hour):.3f} 분")
        
        elif menu == "5":
            sec = float(input("초 입력: "))
            print(f"{sec} 초 = {sec_to_hour(sec):.3f} 시간")