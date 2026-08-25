from abc import ABC, abstractmethod
from typing import List, Union
from pathlib import Path
from ...domain.code_model import CodeModel, PrologFile


class ParserPort(ABC):
    @abstractmethod
    def parse_file(self, file_path: str, content: str) -> PrologFile:
        pass

    @abstractmethod
    def parse_code_model(self, paths: List[Union[str, Path]]) -> CodeModel:
        pass
