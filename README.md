# DLP_DIPLOM

## Для запуска API сервера
```
pip3 install django mitmdump mitmproxy sanic requests customtkinter

cd api_server
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

## Для запуска прокси необходимо сгенерировать сертификаты и запустить сам прокси сервер
```
cd ./proxy_server
./generate_certificates.sh 
............+...+......+.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*.+......+...+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*..........+..+.+..+....+.....+...+...+..........+...+..+.........+.+..+...............+.......+.....+...................+...........+.+...+..............
Enter Export Password: [ENTER]
Verifying - Enter Export Password: [ENTER]

./start_proxy.sh
```

## Для установки сертификатов на разных системах
```

Firefox

    Open Options -> Privacy & Security and click View Certificates... at the bottom of the page.
    Click Import... and select the downloaded certificate.
    Enable Trust this CA to identify websites and click OK.

Android 10+

    Open the downloaded CER file.
    Enter mitmproxy (or anything else) as the certificate name.
    For credential use, select VPN and apps.
    Click OK.

Some Android distributions require you to install the certificate via Settings -> Security -> Advanced -> Encryption and credentials -> Install a certificate -> CA certificate (or similar) instead.


macOS Manual Installation

    Double-click the PEM file to open the Keychain Access application.
    Locate the new certificate "mitmproxy" in the list and double-click it.
    Change Secure Socket Layer (SSL) to Always Trust.
    Close the dialog window and enter your password if prompted.

Automated Installation

    sudo security add-trusted-cert -d -p ssl -p basic -k /Library/Keychains/System.keychain mitmproxy-ca-cert.pem



Ubuntu/Debian

    mv mitmproxy-ca-cert.pem /usr/local/share/ca-certificates/mitmproxy.crt
    sudo update-ca-certificates


Windows Manual Installation

    Double-click the P12 file to start the import wizard.
    Select a certificate store location. This determines who will trust the certificate – only the current Windows user or everyone on the machine. Click Next.
    Click Next again.
    Leave Password blank and click Next.
    Select Place all certificates in the following store, then click Browse, and select Trusted Root Certification Authorities.
    Click OK and Next.
    Click Finish.
    Click Yes to confirm the warning dialog.

Automated Installation

    Run certutil.exe -addstore root mitmproxy-ca-cert.cer (details).



```
### Сами сертификаты лежат в ./proxy_server/certs/
