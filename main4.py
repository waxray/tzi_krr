import ssl
import socket

def check_ssl_certificate(host):
    context = ssl.create_default_context()
    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=host,
    )
    conn.settimeout(1)
    try:
        conn.connect((host, 443))
        cert = conn.getpeercert()
        print(f"Сертифікат для {host}:")
        for key, value in cert.items():
            print(f"{key}: {value}")
    except ssl.SSLError as e:
        print(f"SSL помилка на {host}: {e}")
    except Exception as e:
        print(f"Помилка підключення до {host}: {e}")
    finally:
        conn.close()

check_ssl_certificate("example.com")
