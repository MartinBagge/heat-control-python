from multiprocessing import Process, Queue
import utils, gpio, camera
import time

restarts = 0
first_restart = 0

def start_cam(queue):
    camera.start_recording(queue)

def notify():
    print("NOTIFY!!!")

def main():
    global restarts, first_restart
    queue = Queue()
    camera_p = Process(target=start_cam, args=(queue,), daemon=True)
    camera_p.start()
    while True:
        indicators = []
        for i in range(queue.qsize()):
            indicators.append(queue.get())
        if utils.calculate_on_off(indicators) and restarts != 3:
            #gpio.punch_relay()
            print("punched relay")
            if restarts == 0:
                first_restart = time.time()
            restarts += 1
        else:
            restarts += 1
            print("no punch")
        if restarts == 4:
            notify()
            break
        elif (restarts < 4) and (time.time()-first_restart > 60*60):
            restarts = 0
        #time.sleep(60*10)
        time.sleep(30)
main()