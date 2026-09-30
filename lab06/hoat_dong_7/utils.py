def dao_nguoc_chuoi(chuoi):
 return chuoi[::-1]
def kiem_tra_palindrome(chuoi):
 return chuoi == chuoi[::-1]
def chuan_hoa_ho_ten(chuoi):
 return " ".join(chuoi.split()).title()
def uscln(a, b):
 while b != 0:
  a, b = b, a % b
 return a
def kiem_tra_nguyen_to(n):
 if n < 2:
  return False
 for i in range(2, n):
  if n % i == 0:
   return False
 return True
#utils.py và main.py cần đặt trong 1 thư mục để lệnh import utils trong main.py có thể tìm thấy utils.py. 
# Nếu utils.py và main.py không cùng thư mục, Python sẽ không thể tìm thấy utils.py và sẽ báo lỗi ModuleNotFoundError.