import psutil
# from time import sleep



class CPU:
    def __init__(self):
        self.interval = 1
        self.per_cpu = False
        self.is_first = True
        
        
    def cpu_percent(self):
        if self.is_first:
            cpu = psutil.cpu_percent(interval=self.interval, percpu=self.per_cpu)
            self.is_first = False
        else:
            cpu = psutil.cpu_percent(percpu=self.per_cpu)

        return cpu
        
        
# cpu = CPU()
# 
# for i in range(10):
#         print cpu.cpu_percent()
#         sleep(1)