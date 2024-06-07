#โจทย์ข้อที่ 3 ค่าไฟในบ้านของฉัน

#รับค่ากำลังไฟฟ้าของเครื่องปรับอากาศทั้ง 3 เครื่อง
power_x = float(input("กำลังไฟเครื่องปรับอากาศที่ 1 (วัตต์): "))
power_y = float(input("กำลังไฟเครื่องปรับอากาศที่ 2 (วัตต์): "))
power_z = float(input("กำลังไฟเครื่องปรับอากาศที่ 3 (วัตต์): "))

#รับอัตราค่าไฟฟ้าต่อหน่อย
rate_unit = float(input("อัตราค่าไฟต่อหน่วย (บาท): "))

#จำนวนชั่วโมงที่ใช้ต่อวัน
per_day = 8

#จำนวนวันในหนึ่งเดือน
per_month = 30

#คำนวณพลังงานไฟฟ้าต่อวัน (หน่วย)
units_x = (power_x * per_day) /1000
units_y = (power_y * per_day) /1000
units_z = (power_z * per_day) /1000

#คำนวณพลังงานไฟฟ้าต่อเดือน (หน่วย)
month_x = units_x * per_month
month_y = units_y * per_month
month_z = units_z * per_month

#คำนวณค่าไฟฟ้ารวมต่อเดือน (บาท)
total = int(month_x + month_y + month_z) * rate_unit


print("ค่าไฟที่ต้องจ่ายเมื่อครบ 30 วัน: "  ,total,   "บาท")
