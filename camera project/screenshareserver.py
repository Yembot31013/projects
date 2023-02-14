from vidstream import StreamingServer
import threading

host = StreamingServer('127.0.0.1', 8080)
th = threading.Thread(target=host.start_server)

th.start()


while input("") != "stop":
  continue


host.stop_server()