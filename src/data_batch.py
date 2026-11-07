from collections.abc import Iterator
from dataclasses import dataclass


@dataclass(frozen=True)
class Sample[T]:
    sample_id:int
    label:int
    payload:T

class DataBatch[T]:
    def __init__(self,sample:list[Sample[T]]) -> None:
        if not isinstance(sample,list):
            raise TypeError("sample必须是list类型")
        self._sample:list[Sample[T]]=sample
    def __len__(self)->int:
        return len(self._sample)
    def __getitem__(self, key:int|slice)->Sample[T]|list[Sample[T]]:
        return self._sample[key]
    def __iter__(self)->Iterator[Sample[T]]:
        return iter(self._sample)
    def __repr__(self) -> str:
        sample_count=len(self._sample)
        sample_preview = (f"first_id={self._sample[0].sample_id}" if sample_count>0 else "empty")
        return f"DataBatch(size={sample_count},{sample_preview})"

    @property
    def labels(self)->list[int]:
        return [s.label for s in self._sample]