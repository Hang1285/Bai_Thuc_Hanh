
danh_sach_sach = [
    {
        "ma_sach": "S001",
        "ten_sach": "Lập trình Python",
        "tac_gia": "Nguyễn Văn An",
        "nam_xuat_ban": 2024,
        "trang_thai": "Có sẵn"
    },
    {
        "ma_sach": "S002",
        "ten_sach": "Cơ sở dữ liệu",
        "tac_gia": "Trần Văn Bình",
        "nam_xuat_ban": 2023,
        "trang_thai": "Có sẵn"
    },
    {
        "ma_sach": "S003",
        "ten_sach": "Lập trình C++",
        "tac_gia": "Lê Văn Nam",
        "nam_xuat_ban": 2022,
        "trang_thai": "Đang mượn"
    }
]

lich_su = []
def nhap_so_nguyen(thong_bao):
    while True:
        try:
            so = int(input(thong_bao))
            return so
        except ValueError:
            print("Lỗi! Vui lòng nhập một số nguyên.")
def hien_thi_sach():
    print("\n" + "=" * 90)
    print("DANH SÁCH SÁCH TRONG THƯ VIỆN")
    print("=" * 90)

    if len(danh_sach_sach) == 0:
        print("Thư viện chưa có sách.")
        return

    print(
        f"{'Mã':<8}"
        f"{'Tên sách':<25}"
        f"{'Tác giả':<22}"
        f"{'Năm':<8}"
        f"{'Trạng thái':<15}"
    )

    print("-" * 90)

    for sach in danh_sach_sach:
        print(
            f"{sach['ma_sach']:<8}"
            f"{sach['ten_sach']:<25}"
            f"{sach['tac_gia']:<22}"
            f"{sach['nam_xuat_ban']:<8}"
            f"{sach['trang_thai']:<15}"
        )

def tim_kiem_sach():
    tu_khoa = input("Nhập tên sách cần tìm: ").strip().lower()

    ket_qua = []

    for sach in danh_sach_sach:
        if tu_khoa in sach["ten_sach"].lower():
            ket_qua.append(sach)

    print("\n===== KẾT QUẢ TÌM KIẾM =====")

    if len(ket_qua) == 0:
        print("Không tìm thấy sách phù hợp.")
    else:
        for sach in ket_qua:
            print(
                f"Mã: {sach['ma_sach']} | "
                f"Tên: {sach['ten_sach']} | "
                f"Tác giả: {sach['tac_gia']} | "
                f"Trạng thái: {sach['trang_thai']}"
            )
def them_sach():
    print("\n===== THÊM SÁCH MỚI =====")

    ma_sach = input("Nhập mã sách: ").strip()
    for sach in danh_sach_sach:
        if sach["ma_sach"].lower() == ma_sach.lower():
            print("Mã sách đã tồn tại!")
            return

    ten_sach = input("Nhập tên sách: ").strip()
    tac_gia = input("Nhập tên tác giả: ").strip()

    nam_xuat_ban = nhap_so_nguyen("Nhập năm xuất bản: ")

    sach_moi = {
        "ma_sach": ma_sach,
        "ten_sach": ten_sach,
        "tac_gia": tac_gia,
        "nam_xuat_ban": nam_xuat_ban,
        "trang_thai": "Có sẵn"
    }

    danh_sach_sach.append(sach_moi)

    print("Đã thêm sách thành công!")
def muon_sach():
    print("\n===== MƯỢN SÁCH =====")

    ma_sach = input("Nhập mã sách muốn mượn: ").strip()

    for sach in danh_sach_sach:
        if sach["ma_sach"].lower() == ma_sach.lower():

            if sach["trang_thai"] == "Đang mượn":
                print("Sách này hiện đang được mượn.")
                return

            sach["trang_thai"] = "Đang mượn"

            nguoi_muon = input("Nhập tên người mượn: ").strip()

            lich_su.append({
                "ma_sach": sach["ma_sach"],
                "ten_sach": sach["ten_sach"],
                "nguoi_muon": nguoi_muon,
                "hanh_dong": "Mượn"
            })

            print("Mượn sách thành công!")
            return

    print("Không tìm thấy mã sách.")
def tra_sach():
    print("\n===== TRẢ SÁCH =====")

    ma_sach = input("Nhập mã sách muốn trả: ").strip()

    for sach in danh_sach_sach:
        if sach["ma_sach"].lower() == ma_sach.lower():

            if sach["trang_thai"] == "Có sẵn":
                print("Sách này chưa được mượn.")
                return

            sach["trang_thai"] = "Có sẵn"

            lich_su.append({
                "ma_sach": sach["ma_sach"],
                "ten_sach": sach["ten_sach"],
                "nguoi_muon": "",
                "hanh_dong": "Trả"
            })

            print("Trả sách thành công!")
            return

    print("Không tìm thấy mã sách.")
def thong_ke():
    tong_so = len(danh_sach_sach)

    so_sach_co_san = 0
    so_sach_dang_muon = 0

    for sach in danh_sach_sach:
        if sach["trang_thai"] == "Có sẵn":
            so_sach_co_san += 1
        elif sach["trang_thai"] == "Đang mượn":
            so_sach_dang_muon += 1

    print("\n===== THỐNG KÊ THƯ VIỆN =====")
    print(f"Tổng số sách: {tong_so}")
    print(f"Sách đang có sẵn: {so_sach_co_san}")
    print(f"Sách đang được mượn: {so_sach_dang_muon}")
    print(f"Số giao dịch đã thực hiện: {len(lich_su)}")
def hien_thi_lich_su():
    print("\n===== LỊCH SỬ MƯỢN / TRẢ =====")

    if len(lich_su) == 0:
        print("Chưa có giao dịch nào.")
        return

    for i, giao_dich in enumerate(lich_su, start=1):
        print(
            f"{i}. {giao_dich['hanh_dong']} | "
            f"Mã sách: {giao_dich['ma_sach']} | "
            f"Tên sách: {giao_dich['ten_sach']} | "
            f"Người mượn: {giao_dich['nguoi_muon']}"
        )
def menu():
    while True:
        print("\n")
        print("=" * 50)
        print("       QUẢN LÝ THƯ VIỆN MINI")
        print("=" * 50)
        print("1. Hiển thị danh sách sách")
        print("2. Tìm kiếm sách")
        print("3. Thêm sách mới")
        print("4. Mượn sách")
        print("5. Trả sách")
        print("6. Thống kê")
        print("7. Xem lịch sử mượn/trả")
        print("0. Thoát")
        print("=" * 50)

        lua_chon = nhap_so_nguyen("Nhập lựa chọn: ")

        if lua_chon == 1:
            hien_thi_sach()

        elif lua_chon == 2:
            tim_kiem_sach()

        elif lua_chon == 3:
            them_sach()

        elif lua_chon == 4:
            muon_sach()

        elif lua_chon == 5:
            tra_sach()

        elif lua_chon == 6:
            thong_ke()

        elif lua_chon == 7:
            hien_thi_lich_su()

        elif lua_chon == 0:
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break

        else:
            print("Lựa chọn không hợp lệ!")
menu()
