#ClassInstanceVariable

# Class Variable คือ ตัวแปรที่ทำงานภายใน Class ส่วนอื่นสามารถเข้าถึงข้อมูลส่วนนี้ได้เลย (static attribute)
# โดยไม่จำเป็นต้องสร้าง Object ขั้นมา

# instance Variable คือตัวแปรที่อยู่ภายใน object
# สามารถเข้าถึงข้อมูลส่วนนี้ดดยต้องสร้าง Object ขึ้นมา ล


class Employee:
    # class  variable
    __minSalary = 12000
    __minSalary = 50000
    _companyName = 'บริษัท XYZ จำกัด'


    def __init__(self, name, salary, department):
        # instance Variable
        self.__name = name
        self.__salary = salary
        self.__department = department

    def _showData(self):
        print('ชื่อพนักงาน = {}'+self.__name())
        print('เงินเดือน = {} '+self.__salary())
        print('แผนก = {} '+self.__department())



emp1 = Employee('ฐิตินันท์', 50000, 'HTD2')
# print('เงินเดือนขั้นต่ำ ='+str(Employee.__minSalary))
print(Employee._companyName)