from dataclasses import dataclass


@dataclass
class Sample[T]:
    id:int
    label:int
    featrue:str

class BatchIter[T]:
    def __init__(self,data:list[Sample[T]],batch_size:int)->None:
        self._index=0
        self._data=data
        self._batch_size=batch_size
    def __iter__(self)->"BatchIter[T]":
        return self
    def __next__(self)->list[Sample[T]]:
        if self._index>=len(self._data):
            raise StopIteration
        batch_data=[self._index,self._index+self._batch_size]
        self._index+=1
        return batch_data

class AIDataLoader[T]:
    def __init__(self,sample:list[Sample[T]],batch_size:int=2)->None:
        self.sample=sample
        self.batch_size=batch_size
    def __len__(self)->int:
        return len(self.sample)
    def __getitem__(self, index:int)->Sample[T]:
        return self.sample[index]
    def __iter__(self)->BatchIter[T]:
        return BatchIter(self.sample,self.batch_size)
    def __repr__(self)->str:
        return f"Loader(total_sample={len(self.sample)})"
