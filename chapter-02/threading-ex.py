from concurrent.futures import Future, ThreadPoolExecutor, ProcessPoolExecutor
from time import sleep

def worker(data) -> int:
    print(f'Working with data: {data}')
    return data * 10

def initializer(data) -> None:
    print(f'Initializing with data: {data}')
    
def main():
    executor_cls = ProcessPoolExecutor
    futures: list[Future] = []
    with executor_cls(max_workers=3, initializer=initializer, initargs=(1,)) as exe:
        for i in range(10):
                futures.append(exe.submit(worker, i))
        # exe.shutdown()

    sleep(2)
    for fut in futures:
        print(fut.done(), fut.result())

if __name__ == '__main__':
    main()