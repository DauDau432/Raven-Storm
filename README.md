# Raven-Storm Toolkit

<img src="https://img.shields.io/badge/Python-3.8-blue"> <img src="https://img.shields.io/badge/Status-Beta-orange"> <img src="https://img.shields.io/badge/Version-4-red"> <img src="https://img.shields.io/badge/Licence-MIT-yellowgreen"> <a href="https://taguar258.github.io/Raven-Storm/INSTALLATION"><img src="https://img.shields.io/badge/Download-Now-green"></a>

**Raven-Storm là một bộ công cụ DDoS mạnh mẽ cho các bài kiểm tra thâm nhập, bao gồm các cuộc tấn công đối với một số giao thức được viết bằng python (3.8).**

Gỡ bỏ các điểm truy cập WiFi, thiết bị trong mạng, máy chủ, dịch vụ và thiết bị Bluetooth của bạn một cách dễ dàng.

Raven (viết tắt) mong muốn giúp bạn **kiểm tra, hiểu và học hỏi từ các cuộc tấn công** kiểm tra căng thẳng.

Raven có thể **đối phó với các máy chủ mạnh** và **có thể được tối ưu hóa** cho các mục tiêu không điển hình.

Raven sẽ phù hợp với mục đích của bạn, ngay cả khi nó **làm nhiễu mạng wifi hoặc thiết bị bluetooth**.

_Tôi đã lưu trữ kho lưu trữ này vì tôi hiện không muốn làm việc trên đó._

![MOSHED](https://user-images.githubusercontent.com/36562445/90558504-77d7ca80-e19c-11ea-9dd5-6ba902934866.gif)

## Điều gì làm cho nó khác biệt

- [x] Raven-Storm bao gồm các công cụ để tạo lối tắt và làm việc hiệu quả hơn.
- [x] Raven **Hiệu quả** và **mạnh mẽ** trong việc tắt máy chủ và máy chủ.
- [x] **Kiểm tra** và hiểu biết là mục tiêu của Raven-Storm.
- [x] Raven cho phép bạn kết nối các khách hàng với nhau để tạo mạng botnet.
- [x] Có các giao thức khác nhau như UDP / TCP, ICMP, HTTP, L2CAP, ARP và IEEE.

## Cài đặt
**Trên Windows**

Tải xuống kho lưu trữ Raven-Storm

[***Bấm Vào Đây Để Tải Xuống***]()

Cài đặt python trước sau đó tải xuống gói thư viện
```
pip3 install -r requirements.txt
```
Di chuyển vào trong thư mục chính

Khởi động
```
python3 main.py
```
**Trên Linux**

Chỉ cần nhập dòng sau để cài đặt Raven-Storm trên Linux.
```
curl -s https://raw.githubusercontent.com/DauDau432/Raven-Storm/master/install.sh | sudo bash -s
```

## Gỡ cài đặt

```
sudo bash /usr/share/Raven-Storm/uninstall.sh
```
<a style="color: grey" href="https://taguar258.github.io/Raven-Storm/INSTALLATION"><b>Bấm vào đây để xem hướng dẫn cài đặt chi tiết hơn.</b></a>


<a style="color: grey" href="https://github.com/Taguar258/Raven-Storm/blob/master/README.md#info-and-warning"><b>Điều khoản sử dụng</b></a>

<a style="color: grey" href="https://github.com/Taguar258/Raven-Storm/blob/master/LICENSE">Giấy phép</a>

<a style="color: grey" href="https://github.com/Taguar258/Raven-Storm/projects/1">Trạng thái dự án / Việc cần làm</a>

<a style="color: grey" href="https://github.com/Taguar258/CLIF/">Khung CLIF</a>

## Mô-đun nào để sử dụng

| Method | Module  |
| ------- | --- |
| ping | l3 |
| udp/tcp services | l4 |
| websites | l7 |
| local devices | arp |
| bluetooth | bl |
| wifi | wifi |
| botnet | server |

_Hãy thử sử dụng đòn tấn công L4 nếu L7 không thành công._

<!--![Screenshot_20190405_181220](https://user-images.githubusercontent.com/36562445/55641522-60c65180-57ce-11e9-8c65-084edc2bfb45.jpg)-->
![Preview1](https://user-images.githubusercontent.com/36562445/98484349-152c2300-220f-11eb-84a0-1c3c57415d64.png)

![Preview2](https://user-images.githubusercontent.com/36562445/98694260-8552ba00-2371-11eb-9e20-fd5432c90849.png)
<!--![Screenshot_20190405_181220](https://user-images.githubusercontent.com/36562445/63696325-bdc4b180-c81a-11e9-89b8-a7ce24df08ca.png)-->

## Ví dụ

![Gif](https://user-images.githubusercontent.com/36562445/98694347-a0252e80-2371-11eb-95ec-925e8c98948f.gif)
<!--![render1581110570685](https://user-images.githubusercontent.com/36562445/74067207-f9ce8600-49f8-11ea-9d54-97a056169cf7.gif)-->

## Cách chạy một cuộc tấn công DDoS

_Bạn có thể đã biết sự khác biệt giữa DoS và DDoS:_
_Một cuộc tấn công DoS được thực hiện bởi một Maschine duy nhất và một cuộc tấn công DDoS bởi nhiều._

_Nhưng làm cách nào để thực hiện Tấn công DDoS bằng Raven-Storm?_


Để kết nối nhiều phiên bản của Raven-Storm, bạn sẽ cần phải mở một máy chủ.
Chỉ cần thực hiện lệnh `server` và xác định mật khẩu tùy chỉnh để ngăn người khác can thiệp.
Khi chạy, bạn sẽ nhận được một URL mà bạn có thể kết nối khi thực hiện lệnh `ddos`.


## Thông tin và Cảnh báo

__THE CREATOR (Taguar258) CỦA CÔNG CỤ RAVEN-STORM KHÔNG CHỊU BẤT CỨ TRÁCH NHIỆM NÀO VỀ THIỆT HẠI GÂY RA. NGƯỜI DÙNG CÒN CHỊU TRÁCH NHIỆM, HÃY LÀ: BÃO RAVEN-STORM ĐỂ PHÙ HỢP VỚI CÁC MỤC ĐÍCH BẤT HỢP PHÁP HOẶC THIỆT HẠI TAI NẠN DO RAVEN-STORM gây ra.
NHÀ SÁNG TẠO KHÔNG DUYỆT RAVEN-STORM LÀM CÔNG CỤ CHO CÁC MỤC ĐÍCH BẤT HỢP PHÁP VÀ DO đó KHÔNG HỖ TRỢ BẤT KỲ LÚC NÀO BẤT HỢP PHÁP NÀO CỦA CÔNG CỤ NÀY.
BẰNG CÁCH SỬ DỤNG PHẦN MỀM NÀY, BẠN PHẢI ĐỒNG Ý CHỊU TRÁCH NHIỆM ĐẦY ĐỦ VỀ THIỆT HẠI DO BÃO RAVEN gây ra theo BẤT KỲ CÁCH NÀO CHO RIÊNG BẠN.
NHÀ SÁNG TẠO KHÔNG MUỐN NGƯỜI DÙNG SỬ DỤNG RAVEN-STORM NẾU HỌ KHÔNG CÓ KINH NGHIỆM VỚI CÁC ĐIỂM BAO GỒM.
MỌI ĐÓNG GÓP SẼ GÂY RA THIỆT HẠI TẠM THỜI, NHƯNG THIỆT HẠI DÀI HẠN LÀ CÓ KHẢ NĂNG CHỊU TRÁCH NHIỆM.
RAVEN-STORM KHÔNG NÊN ĐỀ XUẤT NHỮNG NGƯỜI THỰC HIỆN CÁC HOẠT ĐỘNG BẤT HỢP PHÁP.__

__PHẦN MỀM ĐƯỢC CUNG CẤP "NGUYÊN TRẠNG", KHÔNG BẢO HÀNH BẤT KỲ HÌNH THỨC NÀO, RÕ RÀNG HOẶC
NGỤ Ý, BAO GỒM NHƯNG KHÔNG GIỚI HẠN ĐỐI VỚI CÁC BẢO ĐẢM VỀ KHẢ NĂNG LÃNH ĐẠO,
PHÙ HỢP VỚI MỤC ĐÍCH CỤ THỂ VÀ SỰ KHÔNG HỢP LỆ. KHÔNG CÓ SỰ KIỆN NÀO SẼ GẶP
TÁC GIẢ HOẶC CHỦ NHÂN BẢN QUYỀN CHỊU TRÁCH NHIỆM PHÁP LÝ ĐỐI VỚI BẤT KỲ KHIẾU NẠI, THIỆT HẠI HOẶC KHÁC
TRÁCH NHIỆM TRÁCH NHIỆM PHÁP LÝ ĐỐI VỚI MỘT HÀNH VI HỢP ĐỒNG, KHAI THÁC HOẶC KHAI THÁC KHÁC, PHÁT SINH TỪ,
NGOÀI HOẶC KẾT NỐI VỚI PHẦN MỀM HOẶC VIỆC SỬ DỤNG HOẶC KINH DOANH KHÁC TRONG
PHẦN MỀM.__

### Nguồn [**MIT Taguar258 2020**](https://github.com/Taguar258/Raven-Storm/)

