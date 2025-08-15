# ชื่อ , เงินเดือน
class Employee : # การสร้าง class
    # สร้าง method
    def detail(self , name, salary, department):
        # สร้าง Attridute
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {} '.format(self.salary))
        print('แผนก = {} '.format(self.department))

# Attridute เป็นกลไกที่กำหนดคุณสมบัติให้กับ class
# การสร้าง Attridute
    # self.name = ชื่อพนักงาน
    # self.salary = เงินเดือน
    # self.age = อายุของพนักงาน
# Method เป็นกลไกที่กำหนดพฤติกรรมให้กับ class
# การสร้าง Method
    # def getName(self):
    # rerun self.name
# การเรียกใช้งาน
# ชื่อวัตถุ.getName()

# คีย์เวิร์ค self
#  การใช้คีย์เวิร์คของ self จะเป็นตัวชี้หรือบ่งบอกว่าตอนนี้เราทำงานกับวัตถุใด
# ให้บอกตัวตนของวัตถุนั้นๆ   เช่น การกำหนดคุณสมบัติต่างๆในวัตถุ เป็นต้น

# Constructor
# เป็น method พิเศษที่จะถูกใช้งานเมื่อตอนเริ่มสร้างวัตถุ (ไม่ระบุก็ได้)
# โครงสร้างของ Constructor
#   def__init__(self):

# สร้างวุัตถุ

emp1 = Employee()
emp1.detail('ฐิตินันท์',50000,'HTD2')
emp1.showData()

emp2 = Employee()
emp2.detail('อนงชัย',60000,'HTD2')
emp2.showData()

emp3 = Employee()
emp3.detail('Titinan',9000000,'HTD2')
emp3.showData()
