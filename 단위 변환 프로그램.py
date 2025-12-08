def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

if __name__ == "__main__":
    print("=== 온도 단위 변환 프로그램 ===")
    while True:
        print("\n1. °C → °F")
        print("2. °F → °C")
        print("0. 종료")

        menu = input("메뉴 선택: ")

        if menu == "1":
            c = float(input("섭씨(°C) 입력: "))
            print(f"{c:.2f} °C = {c_to_f(c):.2f} °F")

        elif menu == "2":
            f = float(input("화씨(°F) 입력: "))
            print(f"{f:.2f} °F = {f_to_c(f):.2f} °C")