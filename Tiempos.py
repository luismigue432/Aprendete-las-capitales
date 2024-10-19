import time

def Cuenta_regresiva():
    for i in range(3, -1,-1):
        print(f"\r{i}", end=" ", flush=True)
        time.sleep(1)

