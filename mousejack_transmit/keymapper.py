#!/usr/bin/env python

import sys, os

dict = {
			"a":"00:D3:1F:F9:F8:36:CD:C3:F7:93:F5:DE:EB:A3:00:00:00:00:00:00:00:6C",
			"b":"00:D3:0A:1B:C0:2B:42:C8:46:09:F5:DE:EB:A5:00:00:00:00:00:00:00:61",
			"c":"00:D3:F1:4B:61:43:79:79:16:6D:F5:DE:EB:A7:00:00:00:00:00:00:00:73",
			"d":"00:D3:C3:42:2B:A8:C3:F9:08:44:F5:DE:EB:A9:00:00:00:00:00:00:00:E6",
			"e":"00:D3:4C:09:5F:68:1C:8E:01:02:F5:DE:EB:AB:00:00:00:00:00:00:00:FB",
			"f":"00:D3:BC:21:A7:B5:FF:C8:F3:71:F5:DE:EB:AD:00:00:00:00:00:00:00:5E",
			"g":"00:D3:1B:DE:7B:63:AD:BE:AB:40:F5:DE:EB:AF:00:00:00:00:00:00:00:93",
			"h":"00:D3:7B:51:7D:A8:9F:A0:F0:59:F5:DE:EB:B1:00:00:00:00:00:00:00:45",
			"i":"00:D3:32:68:38:4F:46:6A:D4:13:F5:DE:EB:B3:00:00:00:00:00:00:00:04",
			"j":"00:D3:55:52:BE:F6:3A:D8:30:DC:F5:DE:EB:B5:00:00:00:00:00:00:00:41",
			"k":"00:D3:F9:C1:81:5E:6C:55:20:EF:F5:DE:EB:B7:00:00:00:00:00:00:00:4F",
			"l":"00:D3:66:BA:AF:A5:A0:20:E1:E1:F5:DE:EB:B9:00:00:00:00:00:00:00:C0",
			"m":"00:D3:C7:02:17:60:9D:A7:1B:2A:F5:DE:EB:BB:00:00:00:00:00:00:00:EB",
			"n":"00:D3:F1:C4:4D:7D:13:93:99:05:F5:DE:EB:BD:00:00:00:00:00:00:00:EF",
			"o":"00:D3:EA:C9:FB:44:CC:9C:16:0E:F5:DE:EB:BF:00:00:00:00:00:00:00:32",
			"p":"00:D3:B2:18:72:54:EF:03:94:DA:F5:DE:EB:C1:00:00:00:00:00:00:00:BE",
			"q":"00:D3:8C:EF:9F:CF:B6:56:2E:6E:F5:DE:EB:C3:00:00:00:00:00:00:00:1B",
			"r":"00:D3:36:76:60:E2:C3:5D:84:08:F5:DE:EB:C5:00:00:00:00:00:00:00:10",
			"s":"00:D3:E0:9C:61:1A:76:2B:CE:92:F5:DE:EB:C7:00:00:00:00:00:00:00:B0",
			"t":"00:D3:07:BD:61:B5:81:E3:60:05:F5:DE:EB:C9:00:00:00:00:00:00:00:03",
			"u":"00:D3:F4:C9:DD:BB:CE:FE:CB:B8:F5:DE:EB:CB:00:00:00:00:00:00:00:00",
			"v":"00:D3:FF:25:E6:26:B2:F3:1E:28:F5:DE:EB:CD:00:00:00:00:00:00:00:87",
			"w":"00:D3:A1:BC:64:57:FA:77:55:17:F5:DE:EB:CF:00:00:00:00:00:00:00:AB",
			"x":"00:D3:19:6B:00:4B:BE:0E:A1:31:F5:DE:EB:D1:00:00:00:00:00:00:00:31",
			"y":"00:D3:B2:E1:FB:15:F6:87:46:CF:F5:DE:EB:DB:00:00:00:00:00:00:00:5F",
			"z":"00:D3:59:3E:D2:B8:C0:9B:26:9C:F5:DE:EB:D5:00:00:00:00:00:00:00:5C",
			"A":"00:D3:E8:A6:D4:C9:93:AB:EB:15:F5:DE:EF:BE:00:00:00:00:00:00:00:44",
			"B":"00:D3:31:A3:F3:93:FB:63:97:A9:F5:DE:EF:C0:00:00:00:00:00:00:00:B3",
			"C":"00:D3:CB:26:D4:4E:BB:7E:3B:78:F5:DE:EF:C2:00:00:00:00:00:00:00:AA",
			"D":"00:D3:A9:EE:87:8C:B0:28:97:48:F5:DE:EF:C4:00:00:00:00:00:00:00:46",
			"E":"00:D3:F8:4F:ED:CB:A4:B9:92:52:F5:DE:EF:C6:00:00:00:00:00:00:00:65",
			"F":"00:D3:99:F4:AA:E0:D1:F6:6D:C5:F5:DE:EF:C8:00:00:00:00:00:00:00:93",
			"G":"00:D3:79:66:B5:A8:8C:C3:7C:69:F5:DE:EF:CA:00:00:00:00:00:00:00:31",
			"H":"00:D3:94:B3:97:27:FD:AA:09:8E:F5:DE:EF:CC:00:00:00:00:00:00:00:5C",
			"I":"00:D3:37:B7:DF:56:FE:66:5F:93:F5:DE:EF:CE:00:00:00:00:00:00:00:24",
			"J":"00:D3:A3:A5:1B:DC:16:88:8D:0A:F5:DE:EF:D0:00:00:00:00:00:00:00:27",
			"K":"00:D3:A2:00:72:B1:48:13:4E:E9:F5:DE:EF:D2:00:00:00:00:00:00:00:42",
			"L":"00:D3:18:EB:E2:60:4A:CD:BD:1A:F5:DE:EF:D4:00:00:00:00:00:00:00:64",
			"M":"00:D3:03:E5:E0:C8:98:F8:D6:09:F5:DE:EF:D6:00:00:00:00:00:00:00:96",
			"N":"00:D3:1D:0C:F2:6D:C2:F8:67:17:F5:DE:EF:D8:00:00:00:00:00:00:00:D3",
			"O":"00:D3:7A:71:AD:E7:E0:A3:70:7D:F5:DE:EF:DA:00:00:00:00:00:00:00:A2",
			"P":"00:D3:6F:84:70:6C:ED:6D:9A:B7:F5:DE:EF:DC:00:00:00:00:00:00:00:15",
			"Q":"00:D3:B7:99:5B:EC:5D:EA:2F:E9:F5:DE:EF:DE:00:00:00:00:00:00:00:97",
			"R":"00:D3:8C:DC:9A:CD:29:9D:C3:7A:F5:DE:EF:E0:00:00:00:00:00:00:00:B9",
			"S":"00:D3:E7:23:EB:6C:79:7F:45:43:F5:DE:EF:E2:00:00:00:00:00:00:00:A8",
			"T":"00:D3:FF:05:65:13:C1:C6:3A:30:F5:DE:EF:E4:00:00:00:00:00:00:00:1A",
			"U":"00:D3:90:C2:5E:C8:68:B0:8A:E6:F5:DE:EF:E6:00:00:00:00:00:00:00:85",
			"V":"00:D3:66:2D:C0:14:16:FC:B3:53:F5:DE:EF:E8:00:00:00:00:00:00:00:04",
			"W":"00:D3:F3:E0:2B:21:BB:8D:B6:EA:F5:DE:EF:EA:00:00:00:00:00:00:00:7A",
			"X":"00:D3:95:6E:DD:17:15:C8:66:C1:F5:DE:EF:EC:00:00:00:00:00:00:00:84",
			"Y":"00:D3:31:D7:8C:06:14:58:8C:24:F5:DE:EF:EE:00:00:00:00:00:00:00:C7",
			"Z":"00:D3:7C:E4:94:46:E3:3E:36:DF:F5:DE:EF:F0:00:00:00:00:00:00:00:0B",
			"1":"B4:D3:68:62:72:7D:CC:4B:C4:DD:F5:DE:EB:F3:00:00:00:00:00:00:00:57",
			"2":"00:D3:C1:1E:FE:28:B4:AB:8B:34:F5:DE:EB:F5:00:00:00:00:00:00:00:57",
			"3":"00:D3:8B:94:36:32:63:B0:7D:82:F5:DE:EB:F7:00:00:00:00:00:00:00:DF",
			"4":"00:D3:F6:E7:3C:36:52:67:28:1E:F5:DE:EB:F9:00:00:00:00:00:00:00:28",
			"5":"00:D3:46:06:1E:DB:58:93:57:03:F5:DE:EB:FB:00:00:00:00:00:00:00:EA",
			"6":"00:D3:BC:9B:18:BA:EE:93:6D:3C:F5:DE:EB:FD:00:00:00:00:00:00:00:1F",
			"7":"00:D3:47:7D:FC:44:55:5E:E4:78:F5:DE:EB:FF:00:00:00:00:00:00:00:5D",
			"8":"00:D3:BE:11:A7:CC:9D:75:7A:A5:F5:DE:EC:01:00:00:00:00:00:00:00:FA",
			"9":"00:D3:A1:E6:E7:E1:DC:6C:70:31:F5:DE:EC:03:00:00:00:00:00:00:00:33",
			"0":"00:D3:C5:01:FC:0A:F0:6C:B7:6D:F5:DE:EC:05:00:00:00:00:00:00:00:1D",
			"~":"00:D3:7D:EA:E4:10:D2:DB:91:B2:F5:DE:EC:1A:00:00:00:00:00:00:00:09",
			"!":"00:D3:6A:E1:D0:99:6E:E1:C7:41:F5:DE:EC:12:00:00:00:00:00:00:00:51",
			"@":"00:D3:9C:36:9D:63:6C:9D:EC:AA:F5:DE:EC:1E:00:00:00:00:00:00:00:DF",
			"#":"00:D3:AF:41:33:A4:9B:D0:1B:B5:F5:DE:EC:20:00:00:00:00:00:00:00:4C",
			"$":"00:D3:85:44:5D:B3:A6:AA:67:86:F5:DE:EC:22:00:00:00:00:00:00:00:36",
			"%":"00:D3:78:FB:E4:C6:AD:DF:B9:F3:F5:DE:EC:24:00:00:00:00:00:00:00:F5",
			"^":"00:D3:A0:B1:EA:7B:DC:4E:55:59:F5:DE:EC:26:00:00:00:00:00:00:00:BA",
			"&":"00:D3:33:BF:2A:C7:23:0D:D2:C5:F5:DE:EC:28:00:00:00:00:00:00:00:9C",
			"*":"00:D3:A3:0B:46:97:49:06:30:1D:F5:DE:EC:2A:00:00:00:00:00:00:00:1D",
			"(":"00:D3:A4:90:C7:B4:82:7D:81:62:F5:DE:EC:2C:00:00:00:00:00:00:00:B1",
			")":"00:D3:6A:E5:78:8D:17:42:74:C0:F5:DE:EC:2E:00:00:00:00:00:00:00:5F",
			"_":"00:D3:33:D1:50:29:FE:E0:35:5B:F5:DE:EC:30:00:00:00:00:00:00:00:53",
			"+":"00:D3:8C:CA:00:2E:28:DE:DD:FB:F5:DE:EC:32:00:00:00:00:00:00:00:DA",
			"`":"00:D3:25:B5:7F:64:B4:C1:18:E0:F5:DE:EC:39:00:00:00:00:00:00:00:0B",
			"-":"00:D3:DC:C7:D0:EE:52:F2:AC:3A:F5:DE:EC:3B:00:00:00:00:00:00:00:A8",
			"=":"00:D3:FD:2B:D4:46:F8:D3:35:F6:F5:DE:EC:3D:00:00:00:00:00:00:00:F9",
			"[":"00:D3:5B:CC:73:C3:82:8D:F3:B9:F5:DE:EC:3F:00:00:00:00:00:00:00:17",
			"]":"00:D3:89:30:F2:59:6D:FC:F6:44:F5:DE:EC:41:00:00:00:00:00:00:00:86",
			";":"00:D3:D9:9C:DC:A6:9B:07:9D:0D:F5:DE:EC:43:00:00:00:00:00:00:00:E8",
			"'":"00:D3:D0:53:1D:6A:81:97:DD:45:F5:DE:EC:45:00:00:00:00:00:00:00:45",
			",":"00:D3:4A:0D:3E:5B:F1:6B:BD:0F:F5:DE:EC:49:00:00:00:00:00:00:00:0D",
			".":"00:D3:EB:8B:94:DA:4A:0E:59:D9:F5:DE:EC:4B:00:00:00:00:00:00:00:B5",
			"/":"00:D3:EB:B5:BB:38:F9:1C:B7:AF:F5:DE:EC:4D:00:00:00:00:00:00:00:13",
			"{":"00:D3:2B:D3:B6:A2:CF:35:60:71:F5:DE:EC:50:00:00:00:00:00:00:00:F3",	
			"}":"00:D3:64:44:78:06:06:60:0C:5B:F5:DE:EC:52:00:00:00:00:00:00:00:29",
			":":"00:D3:B7:10:35:46:C2:B3:37:C2:F5:DE:EC:54:00:00:00:00:00:00:00:6A",
			'"':"00:D3:A6:D3:2F:71:5A:7C:8D:8E:F5:DE:EC:56:00:00:00:00:00:00:00:0E",
			"|":"00:D3:71:1B:35:F2:FB:EA:DB:5F:F5:DE:EC:58:00:00:00:00:00:00:00:44",
			"<":"00:D3:81:65:1A:23:BE:C3:98:1C:F5:DE:EC:5A:00:00:00:00:00:00:00:BC",
			">":"00:D3:0B:BF:0D:88:DF:F3:55:18:F5:DE:EC:5C:00:00:00:00:00:00:00:74",
			"?":"00:D3:5D:FF:C3:6C:5D:22:2A:AE:F5:DE:EC:5E:00:00:00:00:00:00:00:2E",
			"\\":"00:D3:9B:E8:EF:EB:EE:66:04:10:F5:DE:EC:47:00:00:00:00:00:00:00:62",
			" ":"00:D3:77:00:5F:82:86:41:2C:6E:F5:DE:EB:DF:00:00:00:00:00:00:00:D7",
			"\t":"00:D3:F4:B4:DC:82:18:2A:5F:22:F5:DE:EC:0D:00:00:00:00:00:00:00:98",
			"\n":"B4:D3:55:7D:C6:37:0D:A5:F6:06:F5:DE:EB:A1:00:00:00:00:00:00:00:9D"
}

'''
keystring = raw_input("Enter your input: ");

for keystroke in keystring:
        f = open("keystrokes.log","a")
        keys = dict[keystroke]
        f.write(keys + "\n")
        f.write("00:40:00:55:6B\n00:D3:2C:31:75:FA:AA:62:49:6C:F5:DE:EB:DE:00:00:00:00:00:00:00:04\n")
        f.close()
'''
while 1:
    try:
        c = sys.stdin.read(1)
        keystroke = dict[c]
        f = open("logs/keystrokes.log","a")
        f.write(keystroke + "\n")
        f.write("00:40:00:55:6B\n00:D3:2C:31:75:FA:AA:62:49:6C:F5:DE:EB:DE:00:00:00:00:00:00:00:04\n")
        f.close()
    except IOError: pass
