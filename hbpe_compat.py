"""HBPE Compatibility Layer — supports HubBasePE 0.0.1.2.01 and 0.0.2.0.00b1.
Usage: import hbpe_compat as HB (replaces 'import HubBasePE.Main as HB')
"""
import sys as _sys
import socket as _socket
import threading as _threading

HBPE_VERSION = "unknown"
HBPE_HAS_PROGRAM20 = False
HBPE_HAS_DEV_CONSOLE = False
HBPE_HAS_SOCKET = True

# Simple socket server/client for HBPE networking
_socket_server = None
_socket_server_running = False
_socket_conn = None

def socket_start_server(port=9999):
    global _socket_server, _socket_server_running
    if _socket_server_running:
        return "Server already running on port {}".format(port)
    try:
        _socket_server = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
        _socket_server.setsockopt(_socket.SOL_SOCKET, _socket.SO_REUSEADDR, 1)
        _socket_server.bind(("0.0.0.0", port))
        _socket_server.listen(1)
        _socket_server.settimeout(30)
        _socket_server_running = True
        return "HBPE Socket server listening on port {}".format(port)
    except Exception as e:
        _socket_server_running = False
        return "Socket server error: {}".format(e)

def socket_accept():
    global _socket_server, _socket_conn, _socket_server_running
    if not _socket_server_running:
        return "No server running. Start with socket_start_server(port)"
    try:
        _socket_conn, addr = _socket_server.accept()
        _socket_conn.settimeout(10)
        return "Connected to {}".format(addr)
    except _socket.timeout:
        return "Accept timed out (30s)"
    except Exception as e:
        return "Accept error: {}".format(e)

def socket_connect(host="127.0.0.1", port=9999):
    global _socket_conn
    try:
        _socket_conn = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
        _socket_conn.settimeout(10)
        _socket_conn.connect((host, port))
        return "Connected to {}:{}".format(host, port)
    except Exception as e:
        _socket_conn = None
        return "Connection error: {}".format(e)

def socket_send(msg):
    global _socket_conn
    if not _socket_conn:
        return "No connection. Use socket_connect or socket_accept first."
    try:
        _socket_conn.sendall((str(msg) + "\n").encode())
        return "Sent: {}".format(msg)
    except Exception as e:
        return "Send error: {}".format(e)

def socket_recv():
    global _socket_conn
    if not _socket_conn:
        return "No connection."
    try:
        data = _socket_conn.recv(4096)
        if data:
            return data.decode().strip()
        return "Connection closed"
    except _socket.timeout:
        return "Receive timed out"
    except Exception as e:
        return "Receive error: {}".format(e)

def socket_close():
    global _socket_conn, _socket_server, _socket_server_running
    if _socket_conn:
        _socket_conn.close()
        _socket_conn = None
    if _socket_server:
        _socket_server.close()
        _socket_server = None
    _socket_server_running = False
    return "Socket closed"

def socket_info():
    global _socket_server_running, _socket_conn
    status = "Server: {}\n".format("running" if _socket_server_running else "stopped")
    status += "Connection: {}".format("active" if _socket_conn else "none")
    return status

try:
    import HubBasePE.Main as _raw_hb

    # Re-export everything from HubBasePE.Main at this module's namespace
    _this = _sys.modules[__name__]
    for _attr in dir(_raw_hb):
        if not _attr.startswith("_"):
            setattr(_this, _attr, getattr(_raw_hb, _attr))

    # Feature detection
    HBPE_HAS_PROGRAM20 = hasattr(_this, "Programm20")
    HBPE_HAS_DEV_CONSOLE = hasattr(_this, "dev_console")

    # Ensure VipAccess/PassGuess/Login exist (0.0.1.2.01 style)
    if not hasattr(_this, "VipAccess"):
        _this.VipAccess = "F"
    if not hasattr(_this, "PassGuess"):
        _this.PassGuess = 0
    if not hasattr(_this, "Login"):
        _this.Login = "usr"

    # Get version string
    try:
        import HubBasePE as _pkg
        raw_ver = getattr(_pkg, "__version__", "")
        HBPE_VERSION = raw_ver or "detected"
    except Exception:
        HBPE_VERSION = "detected"

except ImportError:
    HBPE_VERSION = "not_installed"
