import tkinter as tk
import time
import threading

# 타이머 초기화 변수
timer_running = False
stop_requested = False

# 타이머 함수 정의
def start_pomodoro():
    global timer_running, stop_requested
    timer_running = True
    stop_requested = False

    def countdown(minutes):
        global timer_running, stop_requested
        total_seconds = minutes * 60
        while total_seconds > 0 and not stop_requested:
            mins, secs = divmod(total_seconds, 60)
            timer_label.config(text=f"{mins:02d}:{secs:02d}")
            window.update()
            time.sleep(1)
            total_seconds -= 1
        if not stop_requested:
            timer_label.config(text="00:00")

    # 30분 집중 타이머
    timer_label.config(text="30:00 (집중)")
    countdown(30)
    if not stop_requested:
        # 10분 휴식 타이머
        timer_label.config(text="10:00 (휴식)")
        countdown(10)
    if not stop_requested:
        timer_label.config(text="타이머 완료!")

    timer_running = False

# 타이머 시작 스레드
def start_timer_thread():
    if not timer_running:  # 이미 타이머가 실행 중이면 다시 시작하지 않음
        timer_thread = threading.Thread(target=start_pomodoro)
        timer_thread.start()

# 타이머 정지 함수
def stop_timer():
    global timer_running, stop_requested
    stop_requested = True  # 타이머 종료 요청
    timer_running = False
    timer_label.config(text="타이머를 시작하세요")  # 타이머 초기화 메시지

# GUI 설정
window = tk.Tk()
window.title("포모도로 타이머")
window.geometry("300x200")

timer_label = tk.Label(window, text="타이머를 시작하세요", font=("Helvetica", 24))
timer_label.pack(pady=20)

start_button = tk.Button(window, text="시작", command=start_timer_thread, font=("Helvetica", 14))
start_button.pack(side="left", padx=20)

stop_button = tk.Button(window, text="정지", command=stop_timer, font=("Helvetica", 14))
stop_button.pack(side="right", padx=20)

window.mainloop()
