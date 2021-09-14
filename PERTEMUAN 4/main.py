# untuk mengambil / memasukkan library
from gpio import *
from time import *

# untuk mendeklarasikan fungsi handleSensorData
def handleSensorData():
    # mendeklarasikan inputan dari sensor digitalRead
	value = digitalRead(0)
    #  jika value sama dengan 0
	if value == 0:
        # maka semuanya mati dan mencetak tidak ada api terdeteksi
		customWrite(1, '0')
		digitalWrite(2, LOW)
		digitalWrite(3, LOW)
		digitalWrite(4, LOW)
		digitalWrite(5, LOW)
		print("Tidak ada Api terdeteksi")
    #   dan jika inputan tidak sesuai maka
	else:
        # semuanya menyala dan mencetak api terdeteksi
		customWrite(1, '1')
		digitalWrite(2, HIGH)
		digitalWrite(3, HIGH)
		digitalWrite(4, HIGH)
		digitalWrite(5, HIGH)
		print("Api Terdeteksi")
		
# mendeklarasikan fungsi main
def main():
    # berfungsi untuk melakukan tindakan atau ada api maka melakukan action atau aksi
	add_event_detect(0, handleSensorData)
	
    # jika action benar maka berikan delay atau jeda 1000
	while True:
		delay(1000)
		
# jika fungsi main dijalankan maka akan menjalankan programnya
if __name__ == "__main__":
	main()