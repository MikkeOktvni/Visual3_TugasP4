import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from form_profile import Ui_MainWindow  # Import file hasil konversi dari .ui

class MainWindow(QMainWindow, Ui_MainWindow):
    def _init_(self):
        super()._init_()
        self.setupUi(self)
        
        # Menghubungkan tombol dengan fungsi
        self.pushButton_simpan.clicked.connect(self.simpan_data)
        self.pushButton_edit.clicked.connect(self.edit_data)
        self.pushButton_hapus.clicked.connect(self.hapus_data)
        self.pushButton_batal.clicked.connect(self.batal)

    def simpan_data(self):
        # Ambil data dari form
        nim = self.lineEdit_nim.text()
        nama = self.lineEdit_nama.text()
        kelas = self.lineEdit_kelas.text()
        tempat_lahir = self.lineEdit_tempatLahir.text()
        tanggal_lahir = self.dateEdit_tanggalLahir.text()
        telepon = self.lineEdit_telepon.text()
        alamat = self.lineEdit_alamat.text()

        # Tampilkan pesan konfirmasi
        QMessageBox.information(self, "Data Disimpan", f"Data {nama} berhasil disimpan!")

    def edit_data(self):
        # Tampilkan pesan untuk edit data
        QMessageBox.information(self, "Edit Data", "Fungsi Edit Data Belum Diimplementasikan")

    def hapus_data(self):
        # Tampilkan pesan untuk hapus data
        QMessageBox.warning(self, "Hapus Data", "Fungsi Hapus Data Belum Diimplementasikan")

    def batal(self):
        # Kosongkan semua field input
        self.lineEdit_nim.clear()
        self.lineEdit_nama.clear()
        self.lineEdit_kelas.clear()
        self.lineEdit_tempatLahir.clear()
        self.dateEdit_tanggalLahir.setDate(self.dateEdit_tanggalLahir.minimumDate())
        self.lineEdit_telepon.clear()
        self.lineEdit_alamat.clear()

        QMessageBox.information(self, "Batal", "Input telah dibersihkan")

if _name_ == "_main_":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())