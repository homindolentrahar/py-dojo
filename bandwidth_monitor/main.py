import time
import psutil

last_received = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
last_total = last_received + last_sent

while True:
    bytes_received = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent
    bytes_total = bytes_received + bytes_sent

    new_received = bytes_received - last_received
    new_sent = bytes_sent - last_sent
    new_total = bytes_total - last_total

    received_in_mb = new_received / 1024 / 1024
    sent_in_mb = new_sent / 1024 / 1024
    total_in_mb = new_total / 1024 / 1024

    print(f"{received_in_mb:.2f} MB received, {sent_in_mb:.2f} MB sent, {total_in_mb:.2f} MB total")

    last_received = bytes_received
    last_sent = bytes_sent
    last_total = bytes_total

    time.sleep(1)
