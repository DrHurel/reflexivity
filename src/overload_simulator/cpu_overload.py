import threading

from meta.pattern import Atomic


class Task:

    def start(self):...

    def cancel(self):...


class TaskHandler:...



def _cpu_intensive_task(atomic: Atomic[bool]):
    while atomic:
        pass  # Busy-wait to simulate CPU overload

def overload_cpu(atomic: Atomic[bool]) -> threading.Thread:
    return threading.Thread(target=_cpu_intensive_task, args=[atomic], daemon=True)



def stop_cpu_overload(stop: list[Atomic[bool]]) -> None:
    for s in stop:
        s.set(False)

