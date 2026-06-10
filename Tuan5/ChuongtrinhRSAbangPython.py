import customtkinter as ctk
from tkinter import messagebox, filedialog
import math as thuVienToanHoc
import random as ngauNhien

ctk.set_appearance_mode("Light")  
ctk.set_default_color_theme("blue")

def kiemTraSoNguyenTo(conSo):
    if conSo <= 1: return False
    for i in range(2, int(thuVienToanHoc.isqrt(conSo)) + 1):
        if conSo % i == 0: return False
    return True

def sinhSoNguyenToNgauNhien(giaTriNhoNhat=100, giaTriLonNhat=999):
    while True:
        conSo = ngauNhien.randint(giaTriNhoNhat, giaTriLonNhat)
        if kiemTraSoNguyenTo(conSo):
            return conSo

class GiaoDienRSA:
    def __init__(self, cuaSoChinh):
        self.cuaSoChinh = cuaSoChinh
        self.cuaSoChinh.title("Chương trình Mã hóa & Giải mã RSA")
        self.cuaSoChinh.geometry("950x750")
        
        self.bienP = ctk.StringVar()
        self.bienQ = ctk.StringVar()
        self.bienN = ctk.StringVar()
        self.bienE = ctk.StringVar()
        self.bienD = ctk.StringVar()

        self.thietLapGiaoDien()

    def thietLapGiaoDien(self):

        fontTieuDe = ctk.CTkFont(family="Arial", size=14, weight="bold")
        fontThuong = ctk.CTkFont(family="Arial", size=12)

        khungTong = ctk.CTkFrame(self.cuaSoChinh, corner_radius=20, fg_color="#f0f2f5", border_width=2, border_color="#cccccc")
        khungTong.pack(fill="both", expand=True, padx=15, pady=15)

        khungKhoa = ctk.CTkFrame(khungTong, corner_radius=15, fg_color="white")
        khungKhoa.pack(fill="x", padx=15, pady=15)
        
        ctk.CTkLabel(khungKhoa, text="QUẢN LÝ KHÓA RSA", font=fontTieuDe, text_color="#333333").grid(row=0, column=0, columnspan=6, pady=(10, 5), padx=15, sticky="w")

        ctk.CTkLabel(khungKhoa, text="p:", font=fontThuong).grid(row=1, column=0, sticky="e", padx=(10, 5))
        self.oNhapP = ctk.CTkEntry(khungKhoa, textvariable=self.bienP, width=100, corner_radius=8)
        self.oNhapP.grid(row=1, column=1, padx=5, pady=5)
        self.oNhapP.bind("<FocusOut>", self.kiemTraP)
        
        ctk.CTkLabel(khungKhoa, text="q:", font=fontThuong).grid(row=1, column=2, sticky="e", padx=(15, 5))
        self.oNhapQ = ctk.CTkEntry(khungKhoa, textvariable=self.bienQ, width=100, corner_radius=8)
        self.oNhapQ.grid(row=1, column=3, padx=5, pady=5)
        self.oNhapQ.bind("<FocusOut>", self.kiemTraQ)

        ctk.CTkLabel(khungKhoa, text="n (Public/Private):", font=fontThuong).grid(row=1, column=4, sticky="e", padx=(15, 5))
        ctk.CTkEntry(khungKhoa, textvariable=self.bienN, width=150, corner_radius=8, state="readonly").grid(row=1, column=5, padx=5, pady=5)

        ctk.CTkLabel(khungKhoa, text="e (Public Key):", font=fontThuong).grid(row=2, column=0, sticky="e", padx=(10, 5), pady=(0, 15))
        self.oNhapE = ctk.CTkEntry(khungKhoa, textvariable=self.bienE, width=100, corner_radius=8)
        self.oNhapE.grid(row=2, column=1, padx=5, pady=(0, 15))
        self.oNhapE.bind("<FocusOut>", self.kiemTraE)

        ctk.CTkLabel(khungKhoa, text="d (Private Key):", font=fontThuong).grid(row=2, column=2, sticky="e", padx=(15, 5), pady=(0, 15))
        ctk.CTkEntry(khungKhoa, textvariable=self.bienD, width=100, corner_radius=8, state="readonly").grid(row=2, column=3, padx=5, pady=(0, 15))

        khungNutBam = ctk.CTkFrame(khungKhoa, fg_color="transparent")
        khungNutBam.grid(row=2, column=4, columnspan=2, sticky="w", padx=10, pady=(0, 15))
        
        ctk.CTkButton(khungNutBam, text="Lấy Khóa Ngẫu Nhiên", width=120, corner_radius=10, font=fontThuong, fg_color="#ffc107", text_color="black", hover_color="#e0a800", command=self.sinhKhoaTuDong).pack(side="left", padx=5)
        ctk.CTkButton(khungNutBam, text="Tính Khóa", width=100, corner_radius=10, font=fontThuong, fg_color="#28a745", text_color="white", hover_color="#218838", command=self.tinhToanKhoa).pack(side="left", padx=5)

        khungChinh = ctk.CTkFrame(khungTong, fg_color="transparent")
        khungChinh.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        khungMaHoa = ctk.CTkFrame(khungChinh, corner_radius=15, fg_color="white")
        khungMaHoa.pack(side="left", fill="both", expand=True, padx=(0, 10))

        ctk.CTkLabel(khungMaHoa, text="MÃ HÓA ", font=fontTieuDe, text_color="#0056b3").pack(anchor="w", padx=15, pady=(10, 5))
        
        ctk.CTkLabel(khungMaHoa, text="Văn bản gốc:", font=fontThuong).pack(anchor="w", padx=15)
        self.oNhapVanBanGoc = ctk.CTkTextbox(khungMaHoa, height=100, corner_radius=10, border_width=1)
        self.oNhapVanBanGoc.pack(fill="x", padx=15, pady=5)
        
        ctk.CTkButton(khungMaHoa, text="📁 Tải tệp", width=80, corner_radius=8, fg_color="#6c757d", hover_color="#5a6268", command=lambda: self.taiTepLen(self.oNhapVanBanGoc)).pack(anchor="e", padx=15)

        ctk.CTkButton(khungMaHoa, text="🔒 Thực Hiện Mã Hóa", width=180, height=35, corner_radius=15, font=fontTieuDe, fg_color="#28a745", hover_color="#218838", command=self.thucHienMaHoa).pack(pady=15)

        ctk.CTkLabel(khungMaHoa, text="Văn bản Mã Hóa :", font=fontThuong).pack(anchor="w", padx=15)
        self.oXuatMaHoa = ctk.CTkTextbox(khungMaHoa, height=100, corner_radius=10, border_width=1)
        self.oXuatMaHoa.pack(fill="x", padx=15, pady=5)
        
        khungHanhDongMaHoa = ctk.CTkFrame(khungMaHoa, fg_color="transparent")
        khungHanhDongMaHoa.pack(fill="x", padx=15, pady=10)
        ctk.CTkButton(khungHanhDongMaHoa, text="❌ Xóa", width=80, corner_radius=8, fg_color="#dc3545", hover_color="#c82333", command=lambda: self.xoaTrangDuLieu(self.oNhapVanBanGoc, self.oXuatMaHoa)).pack(side="left")
        ctk.CTkButton(khungHanhDongMaHoa, text="💾 Lưu", width=80, corner_radius=8, fg_color="#007bff", hover_color="#0069d9", command=lambda: self.luuTepXuong(self.oXuatMaHoa)).pack(side="right")
        ctk.CTkButton(khungHanhDongMaHoa, text="📋 Copy", width=80, corner_radius=8, fg_color="#fd7e14", hover_color="#e36a0f", command=lambda: self.saoChepKhayNhoTam(self.oXuatMaHoa)).pack(side="right", padx=10)


        khungGiaiMa = ctk.CTkFrame(khungChinh, corner_radius=15, fg_color="white")
        khungGiaiMa.pack(side="right", fill="both", expand=True, padx=(10, 0))

        ctk.CTkLabel(khungGiaiMa, text="GIẢI MÃ ", font=fontTieuDe, text_color="#6f42c1").pack(anchor="w", padx=15, pady=(10, 5))

        ctk.CTkLabel(khungGiaiMa, text="Văn bản mã hóa :", font=fontThuong).pack(anchor="w", padx=15)
        self.oNhapGiaiMa = ctk.CTkTextbox(khungGiaiMa, height=100, corner_radius=10, border_width=1)
        self.oNhapGiaiMa.pack(fill="x", padx=15, pady=5)

        ctk.CTkButton(khungGiaiMa, text="📁 Tải tệp", width=80, corner_radius=8, fg_color="#6c757d", hover_color="#5a6268", command=lambda: self.taiTepLen(self.oNhapGiaiMa)).pack(anchor="e", padx=15)

        ctk.CTkButton(khungGiaiMa, text="🔓 Thực Hiện Giải Mã", width=180, height=35, corner_radius=15, font=fontTieuDe, fg_color="#28a745", hover_color="#218838", command=self.thucHienGiaiMa).pack(pady=15)

        ctk.CTkLabel(khungGiaiMa, text="Văn bản Giải Mã:", font=fontThuong).pack(anchor="w", padx=15)
        self.oXuatGiaiMa = ctk.CTkTextbox(khungGiaiMa, height=100, corner_radius=10, border_width=1)
        self.oXuatGiaiMa.pack(fill="x", padx=15, pady=5)

        khungHanhDongGiaiMa = ctk.CTkFrame(khungGiaiMa, fg_color="transparent")
        khungHanhDongGiaiMa.pack(fill="x", padx=15, pady=10)
        ctk.CTkButton(khungHanhDongGiaiMa, text="❌ Xóa", width=80, corner_radius=8, fg_color="#dc3545", hover_color="#c82333", command=lambda: self.xoaTrangDuLieu(self.oNhapGiaiMa, self.oXuatGiaiMa)).pack(side="left")
        ctk.CTkButton(khungHanhDongGiaiMa, text="💾 Lưu", width=80, corner_radius=8, fg_color="#007bff", hover_color="#0069d9", command=lambda: self.luuTepXuong(self.oXuatGiaiMa)).pack(side="right")
        ctk.CTkButton(khungHanhDongGiaiMa, text="📋 Copy", width=80, corner_radius=8, fg_color="#fd7e14", hover_color="#e36a0f", command=lambda: self.saoChepKhayNhoTam(self.oXuatGiaiMa)).pack(side="right", padx=10)

    def kiemTraP(self, event=None):
        chuoiP = self.bienP.get().strip()
        if not chuoiP: return 
        try:
            giaTriP = int(chuoiP)
            if not kiemTraSoNguyenTo(giaTriP):
                messagebox.showerror("Lỗi", "p phải là số nguyên tố. Vui lòng nhập lại!")
                self.bienP.set("") 
                self.cuaSoChinh.after(10, self.oNhapP.focus_set) 
        except ValueError:
            messagebox.showerror("Lỗi", "p phải là một số nguyên!")
            self.bienP.set("")
            self.cuaSoChinh.after(10, self.oNhapP.focus_set)

    def kiemTraQ(self, event=None):
        chuoiQ = self.bienQ.get().strip()
        if not chuoiQ: return
        try:
            giaTriQ = int(chuoiQ)
            if not kiemTraSoNguyenTo(giaTriQ):
                messagebox.showerror("Lỗi", "q phải là số nguyên tố. Vui lòng nhập lại!")
                self.bienQ.set("")
                self.cuaSoChinh.after(10, self.oNhapQ.focus_set)
                return
            
            chuoiP = self.bienP.get().strip()
            if chuoiP and int(chuoiP) == giaTriQ:
                messagebox.showerror("Lỗi", "q ≠  p. Vui lòng nhập lại số khác!")
                self.bienQ.set("")
                self.cuaSoChinh.after(10, self.oNhapQ.focus_set)
                
        except ValueError:
            messagebox.showerror("Lỗi", "q phải là một số nguyên!")
            self.bienQ.set("")
            self.cuaSoChinh.after(10, self.oNhapQ.focus_set)

    def kiemTraE(self, event=None):
        chuoiE = self.bienE.get().strip()
        if not chuoiE: return
        try:
            giaTriE = int(chuoiE)
            chuoiP = self.bienP.get().strip()
            chuoiQ = self.bienQ.get().strip()
            
            if not chuoiP or not chuoiQ:
                messagebox.showwarning("Lỗi", "Vui lòng nhập p và q trước khi nhập e!")
                self.bienE.set("")
                self.cuaSoChinh.after(10, self.oNhapP.focus_set)
                return
                
            giaTriP = int(chuoiP)
            giaTriQ = int(chuoiQ)
            giaTriPhiN = (giaTriP - 1) * (giaTriQ - 1)
            
            if not (1 < giaTriE < giaTriPhiN and thuVienToanHoc.gcd(giaTriE, giaTriPhiN) == 1):
                messagebox.showerror("Lỗi", f"1 <= e < {giaTriPhiN} và UCLN với {giaTriPhiN} bằng 1!")
                self.bienE.set("")
                self.cuaSoChinh.after(10, self.oNhapE.focus_set)
                
        except ValueError:
            messagebox.showerror("Lỗi", "e phải là một số nguyên!")
            self.bienE.set("")
            self.cuaSoChinh.after(10, self.oNhapE.focus_set)

    def sinhKhoaTuDong(self):
        giaTriP = sinhSoNguyenToNgauNhien(100, 500)
        giaTriQ = sinhSoNguyenToNgauNhien(100, 500)
        while giaTriP == giaTriQ:
            giaTriQ = sinhSoNguyenToNgauNhien(100, 500)
            
        self.bienP.set(str(giaTriP))
        self.bienQ.set(str(giaTriQ))
        
        giaTriPhiN = (giaTriP - 1) * (giaTriQ - 1)
        
        giaTriE = ngauNhien.randrange(2, giaTriPhiN)
        while thuVienToanHoc.gcd(giaTriE, giaTriPhiN) != 1:
            giaTriE = ngauNhien.randrange(2, giaTriPhiN)
            
        self.bienE.set(str(giaTriE))
        self.tinhToanKhoa()

    def tinhToanKhoa(self):
        try:
            giaTriP = int(self.bienP.get())
            giaTriQ = int(self.bienQ.get())
            giaTriE = int(self.bienE.get())

            if not (kiemTraSoNguyenTo(giaTriP) and kiemTraSoNguyenTo(giaTriQ)):
                messagebox.showerror("Lỗi", "p và q phải là số nguyên tố!")
                return

            giaTriN = giaTriP * giaTriQ
            giaTriPhiN = (giaTriP - 1) * (giaTriQ - 1)

            if thuVienToanHoc.gcd(giaTriE, giaTriPhiN) != 1:
                messagebox.showerror("Lỗi", f"e={giaTriE} không nguyên tố cùng nhau với phi(n)={giaTriPhiN}")
                return

            giaTriD = pow(giaTriE, -1, giaTriPhiN)
            
            self.bienN.set(str(giaTriN))
            self.bienD.set(str(giaTriD))
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ p, q, e đúng định dạng số nguyên!")

    def thucHienMaHoa(self):
        if not self.bienN.get() or not self.bienE.get():
            messagebox.showwarning("Lỗi", "Vui lòng thiết lập khóa trước!")
            return
        
        vanBan = self.oNhapVanBanGoc.get("1.0", "end").strip()
        if not vanBan: return

        giaTriE = int(self.bienE.get())
        giaTriN = int(self.bienN.get())

        danhSachHex = []
        for kyTu in vanBan:
            giaTriAscii = ord(kyTu)
            kyTuMaHoa = pow(giaTriAscii, giaTriE, giaTriN)
            danhSachHex.append(hex(kyTuMaHoa)[2:].zfill(4))
            
        chuoiKetQua = "".join(danhSachHex).upper()
        self.oXuatMaHoa.delete("1.0", "end")
        self.oXuatMaHoa.insert("end", chuoiKetQua)

    def thucHienGiaiMa(self):
        if not self.bienN.get() or not self.bienD.get():
            messagebox.showwarning("Lỗi", "Vui lòng thiết lập khóa trước!")
            return

        chuoiHex = self.oNhapGiaiMa.get("1.0", "end").strip()
        if not chuoiHex: return

        giaTriD = int(self.bienD.get())
        giaTriN = int(self.bienN.get())

        try:
            cacKhoiHex = [chuoiHex[i:i+4] for i in range(0, len(chuoiHex), 4)]
            chuoiGiaiMa = ""
            for khoi in cacKhoiHex:
                giaTriSo = int(khoi, 16)
                kyTuGoc = pow(giaTriSo, giaTriD, giaTriN)
                chuoiGiaiMa += chr(kyTuGoc)
                
            self.oXuatGiaiMa.delete("1.0", "end")
            self.oXuatGiaiMa.insert("end", chuoiGiaiMa)
        except Exception as e:
            messagebox.showerror("Lỗi", "Dữ liệu Hex không hợp lệ hoặc sai khóa!")

    def saoChepKhayNhoTam(self, oVanBan):
        noiDung = oVanBan.get("1.0", "end").strip()
        if noiDung:
            self.cuaSoChinh.clipboard_clear()
            self.cuaSoChinh.clipboard_append(noiDung)
            self.cuaSoChinh.update()
            messagebox.showinfo("Thành công", "Đã sao chép nội dung!")
        else:
            messagebox.showwarning("Lỗi", "Không có nội dung để sao chép!")

    def taiTepLen(self, oVanBan):
        duongDanTep = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if duongDanTep:
            with open(duongDanTep, 'r', encoding='utf-8') as tepDuLieu:
                noiDung = tepDuLieu.read()
                oVanBan.delete("1.0", "end")
                oVanBan.insert("end", noiDung)

    def luuTepXuong(self, oVanBan):
        e = self.bienE.get() or "Chưa thiết lập"
        d = self.bienD.get() or "Chưa thiết lập"
        n = self.bienN.get() or "Chưa thiết lập"
        
        khoa_cong_khai = f"({e}, {n})"
        khoa_bi_mat = f"({d}, {n})"

        if oVanBan == self.oXuatMaHoa:
            ban_ro = self.oNhapVanBanGoc.get("1.0", "end").strip()
            ban_ma = self.oXuatMaHoa.get("1.0", "end").strip()
        else:
            ban_ma = self.oNhapGiaiMa.get("1.0", "end").strip()
            ban_ro = self.oXuatGiaiMa.get("1.0", "end").strip()

        if not ban_ro and not ban_ma:
            messagebox.showwarning("Lỗi", "Không có nội dung bản rõ hay bản mã để lưu!")
            return
            
        duongDanTep = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if duongDanTep:
            with open(duongDanTep, 'w', encoding='utf-8') as tepDuLieu:

                tepDuLieu.write(f"Khóa công khai : {khoa_cong_khai}\n")
                tepDuLieu.write(f"Khóa bí mật : {khoa_bi_mat}\n")

                tepDuLieu.write(f"\n[BẢN RÕ]: {ban_ro}")
                tepDuLieu.write(f"\n[BẢN MÃ]: {ban_ma}")
                
            messagebox.showinfo("Thành công", "Đã xuất file thành công!")

    def xoaTrangDuLieu(self, oVanBan1, oVanBan2):
        oVanBan1.delete("1.0", "end")
        oVanBan2.delete("1.0", "end")

if __name__ == "__main__":
    cuaSoChinh = ctk.CTk()
    ungDung = GiaoDienRSA(cuaSoChinh)
    cuaSoChinh.mainloop()