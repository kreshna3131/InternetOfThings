# mengambil library yang tersedia
from usb import *
from time import *
from gpio import *

# membuat function main
def main():
	# deklarasi usb dengan diisi seperti dibawah ini
	usb = USB(0, 57600)
    #  setting pinMode yang berfungsi untuk menjalankan program. hal ini disesuaikan dengan koneksi yang dibuat
	pinMode(0, IN)
	pinMode(1, IN)
	pinMode(2, IN)
	pinMode(3, IN)
    # jika perulangan while True
	while True:
        # jika digitalRead ke 0 == High atau bernilai 1 maka jalankan usb.write kiri
		if digitalRead(0) == HIGH:
			usb.write("kiri");
        # jika digitalRead ke 1 == High atau bernilai 1 maka jalankan usb.write kanan
		elif digitalRead(1) == HIGH:
			usb.write("kanan");
        # jika digitalRead ke 2 == High atau bernilai 1 maka jalankan usb.write atas
		elif digitalRead(2) == HIGH:
			usb.write("atas");
        # jika digitalRead ke 3 == High atau bernilai 1 maka jalankan usb.write bawah
		elif digitalRead(3) == HIGH:
			usb.write("bawah");
        # jika salah maka cetak berhenti
		else:
			usb.write("berhenti");
		# memberikan delay pada program sebesar 0.5 second
		delay(500)

# jika __name__ sama dengan string __main__ maka jalankan function main
if __name__ == "__main__":
	main()