# 2020
# Bộ công cụ Raven-Storm được lập trình và phát triển bởi Taguar258.
# Bộ công cụ Raven-Storm được xuất bản theo Giấy phép MIT.
# Bộ công cụ Raven-Storm dựa trên CLIF-Framework.
# CLIF-Framework được lập trình và phát triển bởi Taguar258.
# CLIF-Framework được xuất bản theo Giấy phép MIT.

import socket
from os import system
from time import sleep, time

import requests
import urllib3
from CLIF_Framework.framework import event  # noqa: I003, I900
from CLIF_Framework.framework import tools  # noqa: I900

try:
	import nmap
except ImportError:
	print("Vui lòng cài đặt mô-đun nmap.")
	quit()

event = event()
tools = tools()


class Main:
	def __init__(selfie, console):  # noqa: N805
		global self
		global var
		self = selfie
		var = console  # noqa: VNE002

		self._add_commands()

		# Colors
		var.C_None = "\x1b[0;39m"
		var.C_Bold = "\x1b[1;39m"
		var.C_Green = "\x1b[32m"
		var.C_Violet = "\x1b[34m"
		var.C_Dark_Blue = "\x1b[35m"
		var.C_Red = "\x1b[31m"

		var.nm = None
		var.nmapinstalled = False

	def _add_commands(self):
		event.commands(self.exit_console, ["exit", "quit", "e", "q"])
		event.command(self.help)

		event.commands(self.run_shell, ".")
		event.commands(self.debug, "$")

		event.help_comment("|\n|-- Quét cổng:")
		event.help("ports ip", "Nhận cổng của IP (lấy cổng i).")
		event.help("ports web", "Nhận cổng web (lấy cổng w).")
		event.help_comment("|\n|-- Quét mạng:")
		event.help("lan scan", "Nhận tất cả các Ips của Wi-Fi.")
		event.help_comment("|\n|-- Quét miền:")
		event.help("domain ip", "Nhận IP theo máy chủ.")
		event.help("post scan", "Nhận tất cả các biến bài đăng của một Trang web.")
		event.help_comment("|\n|-- Kiểm tra tốc độ:")
		event.help("speed down", "Trả lại thời gian cần thiết để mở một trang web.")
		event.help("speed ping", "Trả lại thời gian cần thiết để ping một IP.")

	def banner(self):
		system("clear || cls")
		print(("""C_B----------------------------------------------------------C_W
NGƯỜI SÁNG TẠO KHÔNG CHỊU BẤT CỨ TRÁCH NHIỆM NÀO VỀ THIỆT HẠI GÂY RA.
NGƯỜI DÙNG CŨNG PHẢI CHỊU TRÁCH NHIỆM
ĐỂ PHÙ HỢP VỚI CÁC MỤC ĐÍCH BẤT HỢP PHÁP HOẶC THIỆT HẠI TAI NẠN DO BÃO RAVEN gây ra.
BẰNG CÁCH SỬ DỤNG PHẦN MỀM NÀY, BẠN PHẢI ĐỒNG Ý CHỊU TRÁCH NHIỆM ĐẦY ĐỦ
ĐỐI VỚI BẤT KỲ THIỆT HẠI NÀO DO RAVEN-STORM gây ra.
MỌI Đòn tấn công SẼ gây ra THIỆT HẠI TẠM THỜI NHƯNG THIỆT HẠI DÀI HẠN LÀ
CÓ KHẢ NĂNG ĐÚNG CÁCH.
RAVEN-STORM KHÔNG NÊN ĐỀ XUẤT NHỮNG NGƯỜI THỰC HIỆN CÁC HOẠT ĐỘNG BẤT HỢP PHÁP.
C_B----------------------------------------------------------C_W""").replace("C_W", var.C_None).replace("C_B", var.C_Bold))
		self.help()

	def exit_console(self):
		print("\033[1;32;0mChúc một ngày tốt lành.")
		quit()

	def run_shell(self, command):
		print("")
		system(tools.arg("Nhập lệnh shell: \033[1;32;0m", ". ", command))
		print("")

	def debug(self, command):
		print("")
		eval(tools.arg("Nhập lệnh gỡ lỗi: \033[1;32;0m", "$ ", command))
		print("")

	@event.command
	def clear():
		system("clear || cls")

	@event.event
	def on_ready():
		try:
			var.nm = nmap.PortScanner()
			var.nmapinstalled = True
		except Exception as e:
			system("clear || cls")
			print("Vui lòng cài đặt gói nmap.")
			print("Một số chức năng sẽ không hoạt động nếu không có nó.")
			print(e)
			try:
				input("[Nhấn enter để tiếp tục mà không có nmap]")  # noqa: S322
			except Exception:
				quit()
		self.banner()

	@event.event
	def on_command_not_found(command):
		print("")
		print("Lệnh bạn đã nhập không tồn tại.")
		print("")

	def check_session(self):
		if var.session[1][0] and len(var.session[1][1]) >= 1:
			if len(var.session[1][1][0]) >= 1:
				run_following = [var.session[1][1][0][0], var.session[1][1][0][0]]
				var.session[1][1][0] = var.session[1][1][0][1:]
			else:
				var.session[1][1] = var.session[1][1][1:]
				run_following = [var.session[1][1][0][0], var.session[1][1][0][0]]
				var.session[1][1][0] = var.session[1][1][0][1:]
			var.run_command = run_following

	@event.event
	def on_input():
		self.check_session()
		if var.server[0] and not var.server[1]:
			while True:
				data = requests.post((var.server[2] + ("get/com%s" % var.server[4])), data={"password": var.server[3]}).text
				if data != "500":
					var.server[4] = var.server[4] + 1
					var.run_command = [data, data]
					print(var.ps1 + "\r")
					break
				else:
					sleep(1)

	@event.event
	def on_interrupt():
		print("")
		var.stop()

	@event.event
	def on_command(command):
		if var.session[0][0]:
			var.session[0][1].write(command + "\n")
		if var.server[0] and var.server[1]:
			status = requests.post((var.server[2] + "set/com"), data={"password": var.server[3], "data": command}).text
			if status != "200":
				print("")
				print("Đã xảy ra lỗi khi gửi lệnh tới máy chủ.")
				print("")

	def help(self):
		event.help_title("\x1b[1;39mScanner Help:\x1b[0;39m")
		tools.help("|   |-- ", " :: ", event)
		print("\033[1;32;0m")

	def portscan(self, ip):
		try:
			for p in range(1, 1500):
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				res = sock.connect_ex((ip, p))
				if res == 0:
					print("Port: %s" % str(p))
					sock.close()
		except Exception as e:
			print("Đã xảy ra lỗi khi thực thi.", e)

	def lanscan(self):
		try:
			gateways = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			gateways.connect(("8.8.8.8", 80))
			gateway = ".".join((gateways.getsockname()[0].split("."))[:len(gateways.getsockname()[0].split(".")) - 1])
			gateways.close()
			var.nm.scan(hosts=("%s.0/24" % gateway), arguments="-sP")
			lanscandev = [(x, var.nm[x]['status']['state'], var.nm[x]["hostnames"][0]["name"], var.nm[x]["hostnames"][0]["type"]) for x in var.nm.all_hosts()]
			print("Gate way: %s.0" % gateway)
			for lanscandevice in lanscandev:
				print("%s  %s  %s  %s" % (lanscandevice[0], lanscandevice[1], lanscandevice[2], lanscandevice[3]))
		except Exception as e:
			print("Đã xảy ra lỗi khi thực thi.", e)

	def hbi(self, ip):
		return socket.gethostbyname(ip)

	def speedtest(self, url):
		try:
			if "http" not in url or "://" not in url:
				url = ("https://%s" % url)
			print("Đang kiểm tra tốc độ tải xuống ...")
			start = time()
			http = urllib3.PoolManager()
			response = http.request('GET', url)
			data = response.data  # noqa: F841
			end = time()
			result = (end - start)
			return result
		except Exception as e:
			print("Đã xảy ra lỗi khi thực thi.", e)

	def speedping(self, ip):
		try:
			print("Đang kiểm tra tốc độ ping ... (Có thể yêu cầu sudo)")
			start = time()
			system("ping -c 1 %s > /dev/null" % ip)
			end = time()
			result = (end - start)
			return result
		except Exception as e:
			print("Đã xảy ra lỗi khi thực thi.", e)

	@event.command
	def domain_ip(command):
		print("")
		try:
			zw = (tools.arg("Domain: ", "domain ip ", command).replace("https://", "").replace("http://", ""))
			print(self.hbi(zw))
		except Exception as e:
			print("Đã xảy ra lỗi khi thực thi.", e)
		print("")

	@event.command
	def lan_scan(command):
		print("")
		if var.nmapinstalled:
			self.lanscan()
		else:
			print("Vui lòng cài đặt nmap.")
		print("")

	@event.command
	def ports_ip(command):
		print("")
		try:
			psi = tools.arg("IP: ", "ports ip ", command)
			self.portscan(psi)
		except Exception as e:
			print("Đã xảy ra lỗi khi thực thi.", e)
		print("")

	@event.command
	def ports_web(command):
		print("")
		try:
			psw = tools.arg("Website: ", "ports web ", command)
			psww = socket.gethostbyname(psw.replace("https://", "").replace("http://", ""))
			self.portscan(psww)
		except Exception as e:
			print("Đã xảy ra lỗi khi thực thi.", e)
		print("")

	@event.command
	def speed_down(command):
		print("")
		zw = self.speedtest(tools.arg("Website: ", "speed down ", command))
		print("Kết quả: %s giây" % zw)
		print("")

	@event.command
	def speed_ping(command):
		print("")
		zw = self.speedping(tools.arg("IP: ", "speed ping ", command))
		print("Kết quả: %s giây" % zw)
		print("")


def setup(console):
	console.ps1 = "\033[1;32;0mScanner> "
	console.add(Main(console), event)
