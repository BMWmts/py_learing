#Learning Python made simple
#Classes
#Self
#Methods
#Dunder methods
#Conclusion

class Microwave: # สร้างคลาสชื่อ Microwave เพื่อเป็นแม่แบบในการสร้างวัตถุไมโครเวฟ
    def __init__(self, brand: str, power_rating: str) -> None: # กำหนดเมธอดเริ่มต้นของคลาส Microwave ที่รับพารามิเตอร์ brand และ power_rating
        self.brand = brand # กำหนดคุณสมบัติของไมโครเวฟ เช่น ยี่ห้อ
        self.power_rating = power_rating # กำหนดคุณสมบัติของไมโครเวฟ เช่น ยี่ห้อและระดับพลังงาน
        self.turned_on: bool = False # กำหนดสถานะเริ่มต้นของไมโครเวฟว่าเป็นปิดอยู่

    def turn_on(self) -> None: # กำหนดเมธอดสำหรับเปิดไมโครเวฟ
        if self.turned_on:
            print(f'Microwave ({self.brand}) is already on.') # ถ้าไมโครเวฟเปิดอยู่แล้ว ให้แสดงข้อความว่าไมโครเวฟนั้นเปิดอยู่แล้ว
        else:
            self.turned_on = True # เปลี่ยนสถานะของไมโครเวฟเป็นเปิด
            print(f'Microwave ({self.brand}) is now on.') # แสดงข้อความว่าไมโครเวฟนั้นเปิดแล้ว

    def turn_off(self) -> None: # กำหนดเมธอดสำหรับปิดไมโครเวฟ
        if self.turned_on:
             self.turned_on = False # เปลี่ยนสถานะของไมโครเวฟเป็นปิด
             print(f'Microwave ({self.brand}) is already off.') # ถ้าไมโครเวฟปิดอยู่แล้ว ให้แสดงข้อความว่าไมโครเวฟนั้นปิดอยู่แล้ว
        else:
            print(f'Microwave ({self.brand}) is now off.') # แสดงข้อความว่าไมโครเวฟนั้นปิดแล้ว

    def run(self, duration: int) -> None: # กำหนดเมธอดสำหรับการใช้งานไมโครเวฟ โดยรับพารามิเตอร์ duration ที่เป็นจำนวนเวลาที่ต้องการใช้งาน
        if self.turned_on:
            print(f'Running ({self.brand}) for {duration} seconds.') # ถ้าไมโครเวฟเปิดอยู่ ให้แสดงข้อความว่าไมโครเวฟกำลังทำงานอยู่และระบุระยะเวลา
        else:
            print(f'Microwave ({self.brand}) is off. Please turn it on first.') # ถ้าไมโครเวฟปิดอยู่ ให้แสดงข้อความว่าไมโครเวฟนั้นปิดอยู่และขอให้เปิดก่อนใช้งาน

    def __add__(self, other):
        return f'{self.brand} + {other.brand}' # กำหนดเมธอดสำหรับการบวกวัตถุไมโครเวฟสองตัว โดยจะคืนค่าข้อความที่รวมยี่ห้อของไมโครเวฟทั้งสอง
     
    # สำหรับ User อ่าน (สวยงาม เข้าใจง่าย) 
    def __str__(self):
        return f'Microwave(brand={self.brand}, power_rating={self.power_rating})' # กำหนดเมธอดสำหรับการแสดงผลวัตถุไมโครเวฟในรูปแบบข้อความ
    
    # สำหรับ Developer อ่าน (เอาไปสร้าง Object ใหม่ได้เลย)
    def __repr__(self):
        return f'Microwave(brand={self.brand}, power_rating={self.power_rating})' # กำหนดเมธอดสำหรับการแสดงผลวัตถุไมโครเวฟในรูปแบบข้อความที่เหมาะสมสำหรับการแสดงผลในคอนโซลหรือการดีบัก

    def __mul__(self, other):
        return f'{self.brand} * {other.brand}' # กำหนดเมธอดสำหรับการคูณวัตถุไมโครเวฟสองตัว โดยจะคืนค่าข้อความที่รวมยี่ห้อของไมโครเวฟทั้งสอง
smeg: Microwave = Microwave(brand='Smeg', power_rating='B') # สร้างวัตถุ smeg จากคลาส Microwave โดยกำหนดยี่ห้อเป็น 'Smeg' และระดับพลังงานเป็น 'B'
bosch: Microwave = Microwave(brand='Bosch', power_rating='A') # สร้างวัตถุ bosch จากคลาส Microwave โดยกำหนดยี่ห้อเป็น 'Bosch' และระดับพลังงานเป็น 'A'

print(smeg + bosch) # แสดงผลวัตถุ smeg โดยเรียกใช้เมธอด __str__ ของคลาส Microwave
print(smeg * bosch) # แสดงผลวัตถุ smeg โดยเรียกใช้เมธอด __mul__ ของคลาส Microwave
print(smeg) # แสดงผลวัตถุ smeg โดยเรียกใช้เมธอด __str__ ของคลาส Microwave
print(repr(smeg)) # แสดงผลวัตถุ smeg โดยเรียกใช้เมธอด __repr__ ของคลาส Microwave