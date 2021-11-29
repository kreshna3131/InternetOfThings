# 1 "C:\\Users\\KRESHNA PUTRA ADI\\Documents\\1. FOLDER KULIAH\\SEMESTER 3\\Praktik IoT\\PERTEMUAN 13\\iotku\\iotku.ino"
# 2 "C:\\Users\\KRESHNA PUTRA ADI\\Documents\\1. FOLDER KULIAH\\SEMESTER 3\\Praktik IoT\\PERTEMUAN 13\\iotku\\iotku.ino" 2

// Present a "Will be back soon web page", as stand-in webserver.
// 2011-01-30 <jc@wippler.nl>
//
// License: GPLv2

# 9 "C:\\Users\\KRESHNA PUTRA ADI\\Documents\\1. FOLDER KULIAH\\SEMESTER 3\\Praktik IoT\\PERTEMUAN 13\\iotku\\iotku.ino" 2




// ethernet interface ip address
static byte myip[] = { 192,168,1,200 };
// gateway ip address
static byte gwip[] = { 192,168,1,1 };


// ethernet mac address - must be unique on your network
static byte mymac[] = { 0x74,0x69,0x69,0x2D,0x30,0x31 };

byte Ethernet::buffer[500]; // tcp/ip send and receive buffer

const char page[] 
# 24 "C:\\Users\\KRESHNA PUTRA ADI\\Documents\\1. FOLDER KULIAH\\SEMESTER 3\\Praktik IoT\\PERTEMUAN 13\\iotku\\iotku.ino" 3
                 __attribute__((__progmem__)) 
# 24 "C:\\Users\\KRESHNA PUTRA ADI\\Documents\\1. FOLDER KULIAH\\SEMESTER 3\\Praktik IoT\\PERTEMUAN 13\\iotku\\iotku.ino"
                         =
"HTTP/1.0 503 Service Unavailable\r\n"
"Content-Type: text/html\r\n"
"Retry-After: 600\r\n"
"\r\n"
"<html>"
  "<head><title>"
    "Tugas IoT Pertemuan 13"
  "</title></head>"
  "<body>"
    "<h3>Kreshna Putra Adi Wicaksana</h3>"
    "<p><em>"
      "V3920032<br />"
      "31 Maret 2001<br />"
      "kreshnaputraadi31@student.uns.ac.id"
    "</em></p>"
  "</body>"
"</html>"
;

void setup(){
  Serial.begin(57600);
  Serial.println("\n[backSoon]");

  // Change 'SS' to your Slave Select pin, if you arn't using the default pin
  if (ether.begin(sizeof Ethernet::buffer, mymac, SS) == 0)
    Serial.println( "Failed to access Ethernet controller");

  ether.staticSetup(myip, gwip);





  ether.printIp("IP:  ", ether.myip);
  ether.printIp("GW:  ", ether.gwip);
  ether.printIp("DNS: ", ether.dnsip);
}

void loop(){
  // wait for an incoming TCP packet, but ignore its contents
  if (ether.packetLoop(ether.packetReceive())) {
    memcpy_P(ether.tcpOffset(), page, sizeof page);
    ether.httpServerReply(sizeof page - 1);
  }
}
