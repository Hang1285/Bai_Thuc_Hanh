#bài 6.1
def giai_thua_de_quy(n):
 if n <= 1: # dieu kien dung
  return 1
 return n * giai_thua_de_quy(n - 1)
def giai_thua_lap(n):
 ket_qua = 1
 for i in range(1, n + 1):
    ket_qua *= i
 return ket_qua
print(giai_thua_de_quy(5), "-", giai_thua_lap(5))
#bài 6.2
def fibonacci_de_quy(n):
 if n <= 1: # dieu kien dung
  return n
 return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)
for i in range(10):
 print(fibonacci_de_quy(i), end=" ")
print()
# Đệ quy là cách một hàm tự gọi lại chính nó để giải quyết bài toán,
# giúp code ngắn gọn và dễ hiểu đối với những bài toán có cấu trúc lặp lại
# Tuy nhiên, đệ quy sử dụng nhiều bộ nhớ hơn và có thể gây lỗi nếu gọi quá nhiều lần
# Trong khi đó, vòng lặp như for hoặc while thường dễ kiểm soát, ít tốn bộ nhớ và phù hợp với các bài toán lặp đơn giản.
#Vì vậy, vòng lặp thường hiệu quả hơn trong những bài toán chỉ cần thực hiện một công việc lặp đi lặp lại.

#Đệ quy Fibonacci tốn kém hơn đệ quy thông thường vì nó tính toán lại các giá trị Fibonacci đã được tính trước 
# đó nhiều lần, dẫn đến số lượng phép tính tăng theo cấp số nhân. Trong khi đó, vòng lặp chỉ tính toán mỗi giá trị một lần,
# làm cho nó hiệu quả hơn về thời gian và bộ nhớ.
#vì số lần gọi hàm tăng rất nhanh theo n, dẫn đến số lượng phép tính tăng theo cấp số nhân.
# Trong khi đó, vòng lặp chỉ tính toán mỗi giá trị một lần,