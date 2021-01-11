from faker import Faker

class Ipman:
    def __init__(self, name, address, ip): # 클래스 함수 (메소드 X)
        self.name = name
        self.address = address
        self.ip = ip

    def show_data(self): # 메소드
        print('name :', self.name)
        print('address :', self.address)
        print('ip :', self.ip)

if __name__ == "__main__":
    f = Faker('ko_KR')

    input() # 가상환경일 경우, 버퍼에 가상환경 주소가 남아있는 것을 해결하기 위해 input을 사용

    number = input('몇 개를 생성하겠습니까? > ')
    IPmans = [] # Ipman을 저장할 list

    for i in range(int(number)):
        tmp = IPmans.append(Ipman(f.name(), f.address(), f.ipv4_private()))

    for j in IPmans:
        j.show_data()
        
    print(len(IPmans))