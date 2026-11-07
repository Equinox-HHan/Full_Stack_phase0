import asyncio
import time
from dataclasses import dataclass


@dataclass
class ServiceTaskResult:
    service_name:str
    service_code:int
    elapsed_ms:float
    data:str


async def mock_remote_fetch(service_name:str,delay_time:float,fail:bool=False)->ServiceTaskResult:
    start_time=time.perf_counter()
    await asyncio.sleep(delay_time)

    if fail:
        raise ConnectionError("无法连接到服务器")
    duration=time.perf_counter()-start_time
    return ServiceTaskResult(service_name=service_name,service_code=200,
                             data=f"来自{service_name}的推理结果",elapsed_ms=duration)

async def run_current_service(service_configs:list[tuple[str,float]])->list[ServiceTaskResult]:
    tasks:list[asyncio.Task[ServiceTaskResult]]=[]

    async with asyncio.TaskGroup() as tg:
        for name,delay in service_configs:
            task=tg.create_task(mock_remote_fetch(name,delay))
            tasks.append(task)

    return [t.result() for t in tasks]


