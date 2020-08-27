
import asyncio
import time

async def count():
    print('One')
    await asyncio.sleep(1)
    print('Two')

async def main():
    await asyncio.gather(count(), count(), count(), count(), count(), count(), count(), count(), count(), count())

if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(main())
    end = time.time() - start
    print('The asynchronous function took {} seconds to execute'.format(end))


import time

def count():
    print("One")
    time.sleep(1)
    print("Two")

def main():
    for _ in range(10):
        count()

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time() - start
    print('The synchronous function took {} seconds to execute'.format(end))
