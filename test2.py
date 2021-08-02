import asyncio


async def foo():
    print('----start foo')
    await asyncio.sleep(2)
    print('----end foo')


async def bar():
    print('****start bar')
    await asyncio.sleep(1)
    print('****end bar')


async def main():
    task1 = asyncio.create_task(foo())
    task2 = asyncio.create_task(bar())
    # task1 = foo()
    # task2 = bar()
    await task1
    await task2


if __name__ == '__main__':
    asyncio.run(main())
    asyncio.get_event_loop
