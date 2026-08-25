from abc import ABC, abstractmethod
from ...domain.code_model import CodeModel
from ...domain.detection import DetectionReport


class PatternDetectorPort(ABC):
    @abstractmethod
    def detect(self, model: CodeModel) -> DetectionReport:
        pass
