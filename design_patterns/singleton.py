from typing import Any, Optional
import abc

# 1
class SignletonA:
    _instance: Optional["SignletonA"] = None
    _init: bool = False

    def __new__(cls, *args, **kwargs) -> None:
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self) -> None:
        if not self._init:
            self._init = True
            # do initializing
            print("init")
            ...
############################################

# 2
def singleton_decorator(klass):
    instances = {}
    def get_instance(*args, **kwargs):
        if klass not in instances:
            instances[klass] = klass(*args, **kwargs)
        return instances[klass]
    return get_instance

@singleton_decorator
class SingetonB:
    def __init__(self) -> None:
        # do initializing
        print("init")
        ...
############################################

# 3
class SignletonMetaclass(type):
    _instances = {}
    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
    
class SingletonC(metaclass=SignletonMetaclass):
    def __init__(self) -> None:
        # do initializing
        print("init")
        ...
