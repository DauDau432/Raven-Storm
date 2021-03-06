#!/bin/bash
echo "----------------------------------------"
echo "[i] Cài đặt"
echo "[i] Chúng tôi hiện đang kiểm tra xem bạn đang chạy hệ thống nào."
if [ -f "/etc/debian_version" ]; then
        echo "[i] Linux dựa trên Debian được phát hiện."
        echo "[i] Bây giờ chúng tôi sẽ thu thập một số thông tin...."
        sudo apt-get update > /dev/null 2>&1 || echo "[!] Không thể cập nhật thông tin."
        echo "[i] Bây giờ chúng ta sẽ cài đặt git..."
        sudo apt-get install -y git > /dev/null 2>&1 || echo "[!] Không thể cài đặt git."
        echo "[i] Bây giờ chúng ta sẽ cài đặt python3 và python3-pip..."
        sudo apt-get install -y python3 python3-pip > /dev/null 2>&1 || echo "[!] Không thể cài đặt python3."
        echo "[i] Bây giờ chúng ta sẽ cài đặt ping..."
        sudo apt-get install -y iputils-ping > /dev/null 2>&1 || echo "[!] Không thể cài đặt ping."
        echo "[i] Bây giờ chúng tôi sẽ cài đặt nmap..."
        sudo apt-get install -y nmap > /dev/null 2>&1 || echo "[!] Không thể cài đặt nmap."
        echo "[i] Bây giờ chúng tôi sẽ cài đặt bluez..."
        sudo apt-get install -y bluez > /dev/null 2>&1 || echo "[!] Không thể cài đặt bluez."
        echo "[i] Bây giờ chúng tôi sẽ cài đặt aircrack-ng..."
        sudo apt-get install -y aircrack-ng > /dev/null 2>&1 || echo "[!] Không thể cài đặt aircrack-ng."
        echo "[i] Bây giờ chúng tôi sẽ cài đặt dsniff..."
        sudo apt-get install -y dsniff > /dev/null 2>&1 || echo "[!] Không thể cài đặt dsniff."
        echo "[i] Bây giờ chúng tôi sẽ cài đặt psmisc..."
        sudo apt-get install -y psmisc > /dev/null 2>&1 || echo "[!] Không thể cài đặt psmisc."
        echo "[i] Bây giờ chúng tôi sẽ tải xuống Raven-Storm..."
        sudo git clone https://github.com/DauDau432/Raven-Storm.git > /dev/null 2>&1 || echo "[!] Không thể tải xuống Raven-Storm."
        cd Raven-Storm > /dev/null 2>&1
        echo "[i] Bây giờ chúng tôi sẽ cài đặt requirements..."
        sudo pip3 install -r requirements.txt  > /dev/null 2>&1 || echo "[!] Không thể cài đặt requirements."
        echo "[i] Bây giờ chúng tôi sẽ cài đặt Raven-Storm..."
        sudo bash ./install_to_bin.sh || echo "[!] Không thể cài đặt Raven-Storm."
elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo "[i] Darwin phát hiện."
        echo "[i] Bây giờ chúng tôi sẽ cài đặt brew nếu không tồn tại..."
        brew --help > /dev/null 2>&1 || /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
        echo "[i] Bây giờ chúng tôi sẽ cài đặt git..."
        sudo brew install git > /dev/null 2>&1  || echo "[!] Không thể cài đặt git."
        echo "[i] Bây giờ chúng ta sẽ cài đặt python3 và python3-pip..."
        sudo brew install python3 > /dev/null 2>&1  || echo "[!] Không thể cài đặt python3."
        echo "[i] Bây giờ chúng tôi sẽ cài đặt ping..."
        sudo brew install iputils-ping > /dev/null 2>&1  || echo "[!] Không thể cài đặt ping."
        echo "[i] Bây giờ chúng tôi sẽ cài đặt nmap..."
        sudo brew install nmap > /dev/null 2>&1  || echo "[!] Không thể cài đặt nmap."
        echo "[i] We will now install bluez..."
        sudo brew install bluez > /dev/null 2>&1  || echo "[!] Không thể cài đặt bluez."
        echo "[i] Bây giờ chúng tôi sẽ cài đặt aircrack-ng..."
        sudo brew install aircrack-ng > /dev/null 2>&1  || echo "[!] Không thể cài đặt aircrack-ng."
        echo "[i] Bây giờ chúng tôi sẽ cài đặt dsniff..."
        sudo brew install dsniff > /dev/null 2>&1  || echo "[!] Không thể cài đặt dsniff."
        # chắc chắn psmisc đã được cài đặt sẵn.
        echo "[i] Bây giờ chúng tôi sẽ tải xuống Raven-Storm..."
        sudo git clone https://github.com/DauDau432/Raven-Storm.git > /dev/null 2>&1  || echo "[!] Không thể tải xuống Raven-Storm."
        cd Raven-Storm > /dev/null 2>&1
        echo "[i] Bây giờ chúng tôi sẽ cài đặt requirements..."
        sudo pip3 install -r requirements.txt  > /dev/null 2>&1 || echo "[!] Không thể cài đặt requirements."
        echo "[i] Bây giờ chúng tôi sẽ cài đặt Raven-Storm..."
        sudo bash ./install_to_bin.sh  || echo "[!] Không thể cài đặt Raven-Storm."
elif [ -f "/etc/arch-release" ]; then  # FIXME
        echo "[i] Linux dựa trên Arch được phát hiện."
        echo "[i] Bây giờ chúng tôi sẽ cài đặt git..."
        sudo pacman --noconfirm -S git > /dev/null 2>&1  || echo "[!] Không thể cài đặt git."
        echo "[i] Bây giờ chúng ta sẽ cài đặt python3 và python3-pip..."
        sudo pacman --noconfirm -S python3 python3-pip > /dev/null 2>&1  || echo "[!] Không thể cài đặt python3."
        echo "[i] Bây giờ chúng tôi sẽ cài đặt ping..."
        sudo pacman --noconfirm -S iputils-ping > /dev/null 2>&1  || echo "[!] Không thể cài đặt ping."
        echo "[i] Bây giờ chúng tôi sẽ cài đặt nmap..."
        sudo pacman --noconfirm -S nmap > /dev/null 2>&1  || echo "[!] Không thể cài đặt nmap."
        echo "[i] Bây giờ chúng tôi sẽ cài đặt bluez..."
        sudo pacman --noconfirm -S bluez > /dev/null 2>&1  || echo "[!] Không thể cài đặt bluez."
        echo "[i] Bây giờ chúng tôi sẽ cài đặt aircrack-ng..."
        sudo pacman --noconfirm -S aircrack-ng > /dev/null 2>&1  || echo "[!] Không thể cài đặt aircrack-ng."
        echo "[i] Bây giờ chúng tôi sẽ cài đặt dsniff..."
        sudo pacman --noconfirm -S dsniff > /dev/null 2>&1  || echo "[!] Không thể cài đặt dsniff."
        echo "[i] Bây giờ chúng ta sẽ cài đặt psmisc..."
        sudo pacman --noconfirm -S psmisc > /dev/null 2>&1 || echo "[!] Không thể cài đặt psmisc."
        echo "[i] Bây giờ chúng tôi sẽ tải xuống Raven-Storm..."
        sudo git clone https://github.com/DauDau432/Raven-Storm.git > /dev/null 2>&1  || echo "[!] Không thể tải xuống Raven-Storm."
        cd Raven-Storm > /dev/null 2>&1
        echo "[i] Bây giờ chúng tôi sẽ cài đặt các yêu cầu..."
        sudo pip3 install -r requirements.txt  > /dev/null 2>&1 || echo "[!] Không thể cài đặt các yêu cầu."
        echo "[i] Bây giờ chúng tôi sẽ cài đặt Raven-Storm..."
        sudo bash ./install_to_bin.sh || echo "[!] Không thể cài đặt Raven-Storm."
elif [[ "$OSTYPE" == "win32" ]]; then
        echo "[!] Vui lòng chạy trên wsl."
else
        echo "[!] Chúng tôi không thể phát hiện hệ thống của bạn."
        echo "[i] Vui lòng cài đặt một số thứ theo cách thủ công"
        git clone https://github.com/DauDau432/Raven-Storm.git > /dev/null 2>&1 || echo "[!] Vui lòng cài đặt git"
        cd Raven-Storm
        python3 --help > /dev/null 2>&1 || echo "[!] Vui lòng cài đặt python3."
        command -v ping > /dev/null 2>&1 || echo "[!] Vui lòng cài đặt ping."
        command -v l2ping > /dev/null 2>&1 || echo "[!] Vui lòng cài đặt bluez."
        command -v aircrack-ng > /dev/null 2>&1 || echo "[!] Vui lòng cài đặt aircrack-ng."
        command -v arpspoof > /dev/null 2>&1 || echo "[!] Vui lòng cài đặt dsniff."
        command -v killall > /dev/null 2>&1 || echo "[!] Vui lòng cài đặt psmisc."
        nmap --help > /dev/null 2>&1 || echo "[!] Vui lòng cài đặt nmap."
        pip3 install -r requirements.txt  > /dev/null 2>&1 || echo "[!] Không thể cài đặt các yêu cầu."
        bash ./install_to_bin.sh || echo "[i] Không thể cài đặt."
fi

echo "[i] Xong"
exit 0
