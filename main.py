import time
import sys

loop=1000
stdouts=0
prints=0

stdoutList=[]
printList=[]

for j in range(loop):

    start_sys_time = time.time()
    sys.stdout.write("hello")
    end_sys_time = time.time()

    stdoutList.append(end_sys_time - start_sys_time)


    start_print_time = time.time()
    print("hello")
    end_print_time = time.time()

    printList.append(end_print_time - start_print_time)


for i in stdoutList:
    stdouts += i

for i in printList:
    prints += i


print("\n-----------------------------------------------------------\n")


print(f"stdout: {stdouts/loop}")
print(f"print: {prints/loop}")
