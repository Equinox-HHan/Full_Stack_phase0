import functools
import time
from collections.abc import Callable
from typing import Literal


def timer[**P,R](unit:Literal["ms","s"]="ms",verbose:bool=True)->Callable[[Callable[P,R]],Callable[P,R]]:
    def decorator(func:Callable[P,R])->Callable[P,R]:
        @functools.wraps(func)
        def wrapper(*args:P.args,**kwargs:P.kwargs)->R:
            start_time=time.perf_counter()
            result=func(*args,**kwargs)
            duration=time.perf_counter()-start_time

            if verbose:
                match unit.lower():
                    case "ms":
                        display_time=f"{duration*1000.0:.3f} ms"
                    case "s":
                        display_time=f"{duration:.4f} s"
                    case _:
                        display_time=f"{duration:.4f} s"
                print(f"{func.__name__}执行{display_time}")

            return result
        return wrapper
    return decorator

def retry[**P,R](max_attempts:int=5,initial_delay:float=0.5,backoff_factor:float=2.0,
                 exception:tuple[type[Exception],...]=(Exception,))->Callable[[Callable[P,R]],Callable[P,R]]:
    def decorator(func:Callable[P,R])->Callable[P,R]:
        @functools.wraps(func)
        def wrapper(*args:P.args,**kwargs:P.kwargs)->R:
            delay=initial_delay

            for attempt in range(1,max_attempts+1):
                try:
                    return func(*args,**kwargs)
                except exception as E:
                    if attempt==max_attempts:
                        print(f"{func.__name__}达到最大次数{max_attempts}")
                        raise
                    print(f"{(attempt/max_attempts)}--{func.__name__}"+f"{E}"+f"{delay:.2f}重试")
                time.sleep(delay)
                delay*=attempt
            raise RuntimeError("Unreachable")

        return wrapper
    return decorator
