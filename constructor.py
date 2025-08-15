# Constructor
    # เป็น Method พิเศษที่จะถูกใช้งานเมื่อตอนเริ่มสร้างวัตถุ (ไม่ระบุบก็ได้)
    # โครงสร้าง  Constructor
        # def __init__(self):
        #      pass

# Destructor
    # เป็น method พิเศษที่ตรงข้างกับ Constructor จะูถูกใช้งานเมื่อ
    # สิ้นสุดการทำงานของ class หรือถูกทำก่อนจะสลาย object
    # ส่วนใหญ่จะเป็นกลุ่มคำสั่งที่ทำหน้าที่คืนหน่วยความจำให้ระบบ (ไม่ระบุบก็ได้)
    # โครงสร้าง
    # def __del__(self):
    #  pass

# การสร้าง Constructor

class Employee :
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department


    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {} '.format(self.salary))
        print('แผนก = {} '.format(self.department))
    
    # มีหรือไม่ก็ได้ destructor
    def __del__(self):
        print('call destructor')

emp1 = Employee('ฐิตินันท์',50000,'HTD2')
emp1.showData()

emp2 = Employee('อนงชัย',60000,'HTD2')
emp2.showData()

emp3 = Employee('Titinan',9000000,'HTD2')
emp3.showData()

emp4 = Employee('Gamini',80000,'HTD2')
emp4.salary = 80001
emp4.showData()
