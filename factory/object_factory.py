from faker import Faker
import control_excel as xl

class Ipman:
    def __init__(self, name, address, ip):
        self.name = name
        self.address = address
        self.ip = ip

    def show_data(self):
        print('name :', self.name)
        print('address :', self.address)
        print('ip :', self.ip)
        
# 끝남
IPmans = []
def faker_test():
    f = Faker('ko_KR') # 한국어로 바꿔주기
    
    # 가상환경 쓸 경우, 버퍼에 가상환경 주소가 남아 있는 것을 해결하기 위해
    input()
    
    number = input('몇 개의 객체를 생성하시겠습니까? > ')

    for i in range(int(number)):
        IPmans.append(Ipman(f.name(), f.address(), f.ipv4_private()))
        
    for j in IPmans:
        j.show_data()

    print(len(IPmans))

if __name__ == "__main__":
    # faker_test()
    xl.write_excel()