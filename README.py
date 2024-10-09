import time

def focus_timer(work_duration, break_duration):
    cycle = 1
    while True:
        print(f"Cycle {cycle}")
        print("Work time!")
        time.sleep(work_duration * 60)
        print("Break time!")
        time.sleep(break_duration * 60)
        cycle += 1

# 设置工作时间（分钟）和休息时间（分钟）
work_duration = 25  # 工作时间25分钟
break_duration = 5  # 休息时间5分钟

focus_timer(work_duration, break_duration)
