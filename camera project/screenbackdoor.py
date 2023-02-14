from vidstream import ScreenShareClient
import threading

sender = ScreenShareClient('127.0.0.1', 8080)

th = threading.Thread(target=sender.start_stream())

th.start()