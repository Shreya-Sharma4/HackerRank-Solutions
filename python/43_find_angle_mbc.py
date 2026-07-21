import math

ab = int(input())
bc = int(input())

ac = math.sqrt(ab**2 + bc**2)
cm = ac / 2

angle_acb = math.atan2(ab, bc)

bm = math.sqrt(bc**2 + cm**2 - 2 * (bc * cm) * math.cos(angle_acb))

angle_mbc = (bc**2 + bm**2 - cm**2) / (2 * bc * bm)
angle_mbc = max(-1.0, min(1.0, angle_mbc))

angle_mbc_radians = math.acos(angle_mbc)
angle_mbc_degrees = round(math.degrees(angle_mbc_radians))

print(f"{angle_mbc_degrees}{chr(176)}")