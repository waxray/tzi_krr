import socket

def check_port(host, port):
    """
    Перевірка відкритого порту на вказаному хості.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1) 
    try:
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Порт {port} на {host} відкритий.")
        else:
            print(f"Порт {port} на {host} закритий.")
    except Exception as e:
        print(f"Помилка при підключенні до {host}:{port} - {e}")
    finally:
        sock.close()

host = "example.com"
ports_to_check = [80, 443, 22]
for port in ports_to_check:
    check_port(host, port)
