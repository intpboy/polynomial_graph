import matplotlib.pyplot as plt
import numpy as np

a, b, c, d, e = 0, 0, 0, 0, 0

def coef_init():
      a = 0
      b = 0
      c = 0
      d = 0
      e = 0

def set_func():
      # x 범위 설정
      x = np.linspace(-10, 10, 400)

      # 함수 정의
      y = a*x**4 + b*x**3 + c*x**2 + d*x + e

      # 그래프 그리기

      plt.plot(x, y, label=f'{a}x^4 + {b}x^3 + {c}x^2 + {d}x + {e}')

      plt.title('Polynomial function')
      plt.xlabel('x')
      plt.ylabel('y')
      plt.grid(True)

      plt.axhline(0, color='black',linewidth=1)
      plt.axvline(0, color='black',linewidth=1)

      plt.legend()

      plt.show()


print("원하는 연산을 입력 후 ENTER.")
print("1: 1차함수")
print("2: 2차함수")
print("3: 3차함수")
print("4: 4차함수")
print("0: 나가기")

while(True):
  choice = input("입력: ")
  if choice == '0':
    print('종료합니다')

    break

  if choice == '1' :
        d = float(input("1차항 계수 d를 입력하세요: "))
        e = float(input("상수항 e를 입력하세요: "))
        set_func()
        coef_init()

  elif choice == '2' :
        c = float(input("2차항 계수 c를 입력하세요: "))
        d = float(input("1차항 계수 d를 입력하세요: "))
        e = float(input("상수항 e를 입력하세요: "))
        set_func()
        coef_init()

  elif choice == '3' :
        b = float(input("3차항 계수 b를 입력하세요: "))
        c = float(input("2차항 계수 c를 입력하세요: "))
        d = float(input("1차항 계수 d를 입력하세요: "))
        e = float(input("상수항 e를 입력하세요: "))
        set_func()
        coef_init()

  elif choice == '4' :
        a = float(input("4차항 계수 a를 입력하세요: "))
        b = float(input("3차항 계수 b를 입력하세요: "))
        c = float(input("2차항 계수 c를 입력하세요: "))
        d = float(input("1차항 계수 d를 입력하세요: "))
        e = float(input("상수항 e를 입력하세요: "))
        set_func()
        coef_init()

  else:
      print("잘못된 입력입니다.")  


