
 Bài 3.2 
print("===== BÀI 3.2 =====")

ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000

print("Tên:", ten)
print("Điểm Toán:", diem_toan)
print("Điểm Văn:", diem_van)
print("Số lượng môn học:", so_luong_mon_hoc)
print("Mức lương tối thiểu:", MUC_LUONG_TOI_THIEU)


# Bài 5.1 
print("\n===== BÀI 5.1 =====")

a = 17
b = 5

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)


# Bài 5.2 
print("\n===== BÀI 5.2 =====")

diem = 6.5
tuoi = 20

print("Điểm đạt loại Khá:", diem >= 6.5 and diem < 8.0)
print("Tuổi trên 18:", tuoi > 18)
print("Tuổi không trên 18:", not (tuoi > 18))


# Bài 5.3
print("\n===== BÀI 5.3 =====")

x = 10

x += 5
print("Sau x += 5:", x)

x -= 3
print("Sau x -= 3:", x)

x *= 2
print("Sau x *= 2:", x)

x /= 4
print("Sau x /= 4:", x)

x //= 2
print("Sau x //= 2:", x)

x **= 2
print("Sau x **= 2:", x)

danh_sach = [1, 2, 3, "python"]

print("3 có trong danh_sach:", 3 in danh_sach)
print("danh_sach is danh_sach:", danh_sach is danh_sach)


# Bài 5.4 
print("\n===== BÀI 5.4 =====")

print(2 + 3 * 4 ** 2)
print((2 + 3) * 4 ** 2)
print((10 > 5 and 3 < 1) or False)


# Bài 6.1
print("\n===== BÀI 6.1 =====")

bien = 10
print(bien, type(bien))

bien = "Xin chao"
print(bien, type(bien))

bien = 3.14
print(bien, type(bien))

bien = True
print(bien, type(bien))


# Bài 6.2 
print("\n===== BÀI 6.2 =====")

ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

dtb = (diem_toan + diem_ly + diem_hoa) / 3

la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0

print(ho_ten, "- DTB:", round(dtb, 2))
print("Đạt loại Giỏi:", la_gioi)
print("Đạt loại Khá:", la_kha)
print("Đạt loại Trung bình:", la_trung_binh)
print("Đạt loại Yếu:", la_yeu)
print("Kiểu dữ liệu của la_gioi:", type(la_gioi))