from gpiozero import MotionSensor, LED
from signal import pause
import time

# --- Cấu hình chân GPIO ---
PIR_PIN = 4   # Chân GPIO mà cảm biến PIR được kết nối (chân OUT)
LED_PIN = 17  # Chân GPIO mà đèn LED được kết nối (qua điện trở)

# --- Khởi tạo các đối tượng ---
# Khởi tạo cảm biến PIR
# motion_sensor.when_motion: hàm được gọi khi phát hiện chuyển động
# motion_sensor.when_no_motion: hàm được gọi khi không còn chuyển động
pir_sensor = MotionSensor(PIR_PIN)

# Khởi tạo đèn LED
led = LED(LED_PIN)

# --- Các hàm xử lý sự kiện ---
def motion_detected_handler():
    """
    Hàm này được gọi khi cảm biến PIR phát hiện chuyển động.
    """
    print(f"[{time.strftime('%H:%M:%S')}] Phát hiện chuyển động! Bật đèn.")
    led.on() # Bật đèn LED

def no_motion_handler():
    """
    Hàm này được gọi khi cảm biến PIR không còn phát hiện chuyển động.
    """
    print(f"[{time.strftime('%H:%M:%S')}] Không còn chuyển động. Tắt đèn.")
    led.off() # Tắt đèn LED

# --- Gán hàm xử lý cho sự kiện của cảm biến PIR ---
pir_sensor.when_motion = motion_detected_handler
pir_sensor.when_no_motion = no_motion_handler

# --- Chương trình chính ---
print("Hệ thống giám sát chuyển động đã khởi động!")
print(f"PIR kết nối GPIO {PIR_PIN}, LED kết nối GPIO {LED_PIN}")
print("Đang chờ phát hiện chuyển động...")

try:
    # `pause()` giữ cho chương trình chạy vô thời hạn để lắng nghe sự kiện
    # mà không cần vòng lặp while True
    pause()
except KeyboardInterrupt:
    # Xử lý khi người dùng nhấn Ctrl+C để thoát
    print("\nChương trình dừng.")
    led.off() # Đảm bảo tắt đèn trước khi thoát