# untuk mengambil library
from usb import *
from time import *
from gpio import *
from ioeclient import *

# membuat fungsi GetDir(x)
def getDir(x):
    # jika string atas di x maka cetak string atas dan mengembalikan string 0
	if "atas" in x:
		print("atas")
		return "0"
    # jika string bawah di x maka cetak string bawah dan mengembalikan string 1
	elif "bawah" in x:
		print("bawah")
		return "1"
    # jika string kiri di x maka cetak string kiri dan mengembalikan string 2
	elif "kiri" in x:
		print("kiri")
		return "2"
    # jika string kanan di x maka cetak string kanan dan mengembalikan string 3
	elif "kanan" in x:
		print("kanan")
		return "3"
    # jika salah maka print x dan mengembalikan string 4
	else:
		print(x)
		return "4"

# fungsi main
def main():
    # memulai USB
	usb = USB(0, 57600)

	# setting registrasi server	pada IoEClient Cisco
	IoEClient.setup({
		"type": "SBC",
		"states": [{
			"name": "Direction",
			"type": "options",
			"options": {
				"0" : "Up",
				"1" : "Down",
				"2" : "Left",
				"3" : "Right",
				"4" : "Stop"
			},
            # control sama dengan False
			"controllable": False
		}]
	});

    # jika While True maka
	while True:
        # memasukkan arah dari USB
		direction=""
        # jika usb dalam menunggu lebih dari 0 maka direction diisi dengan readLine
		while usb.inWaiting() > 0:
			direction = usb.readLine()
            # IoEClient mengambil direction atau arah
			IoEClient.reportStates(getDir(direction))
        # memberikan jeda sebesar 0.5 second
		delay(500)

# jika __name__ sama dengan string __main__ maka jalankan function main
if __name__ == "__main__":
	main()
