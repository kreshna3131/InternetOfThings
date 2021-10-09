# untuk mengambil library
from time import *
from gpio import *
from ioeclient import *
from physical import *

# membuat fungsi onInputReceive
def onInputReceive(input):
    # jika input sama dengan string 0 
	if input == "0":
        # maka cetak menuju atas dan menggeser keatas sebanyak -20 pixel 
		print("Menuju Atas")
		moveBy(0, -20)
    # jika input sama dengan string 1
	elif input == "1":
        # maka cetak menuju atas dan menggeser kebawah sebanyak 20 pixel 
		print("Menuju Bawah")
		moveBy(0, 20);
    # jika input sama dengan string 2
	elif input == "2":
        # maka cetak menuju atas dan menggeser kekiri sebanyak -20 pixel 
		print("Menuju Kiri")
		moveBy(-20, 0);
    # jika input sama dengan string 3
	elif input == "3":
        # maka cetak menuju atas dan menggeser kekanan sebanyak 20 pixel 
		print("Menuju Kanan")
		moveBy(20, 0);
    # jika salah maka cetak stop
	else:
		print("stop")

		
# membuat fungsi main
def main():
    # setting registrasi server	pada IoEClient Cisco
	IoEClient.setup({
		"type": "Car",
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
            # control sama dengan True
			"controllable": True
		}]
	});

    # IoEClient ini mengambil data inputan
	IoEClient.onInputReceive(onInputReceive)
    # jika benar maka memberikan delay sebesar 0.5 second
	while True:
		delay(500)

# jika __name__ sama dengan string __main__ maka jalankan function main
if __name__ == "__main__":
	main()
