import re
from typing import List
from .base import Rule
from ..code_model import CodeModel
from ..detection import Detection
from ..value_objects import PatternType, Confidence, SourceLocation, EvidenceItem


class FactoryMethodRule(Rule):
    @property
    def name(self) -> str:
        return "GOF_FACTORY_METHOD"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        factory_pattern = re.compile(r'^\s*([a-zA-Z0-9_]*(?:create|make|build|construct|instantiate)[a-zA-Z0-9_]*)\s*\((.*?)\)\s*:-', re.MULTILINE)
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = factory_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    pred_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="CREATIONAL_FACTORY_METHOD",
                        weight=0.92,
                        description=f"Predicate '{pred_name}' implements GoF Factory Method generating terms based on parameters",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.GOF_FACTORY_METHOD,
                            target_name=pred_name,
                            location=loc,
                            confidence=Confidence(0.92),
                            evidence=[ev],
                        )
                    )
        return detections


class AbstractFactoryRule(Rule):
    @property
    def name(self) -> str:
        return "GOF_ABSTRACT_FACTORY"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        af_pattern = re.compile(r'^\s*([a-zA-Z0-9_]*(?:abstract_factory|factory_family|backend_factory)[a-zA-Z0-9_]*)\s*\((.*?)\)\s*:-', re.MULTILINE)
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = af_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    pred_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="CREATIONAL_ABSTRACT_FACTORY",
                        weight=0.92,
                        description=f"Predicate '{pred_name}' implements GoF Abstract Factory producing related term families",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.GOF_ABSTRACT_FACTORY,
                            target_name=pred_name,
                            location=loc,
                            confidence=Confidence(0.92),
                            evidence=[ev],
                        )
                    )
        return detections


class BuilderRule(Rule):
    @property
    def name(self) -> str:
        return "GOF_BUILDER"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        builder_pattern = re.compile(r'^\s*([a-zA-Z0-9_]*(?:builder|with_[a-z0-9_]+|set_[a-z0-9_]+|add_[a-z0-9_]+))\s*\((.*?,\s*[A-Z][a-zA-Z0-9_]*0?,\s*[A-Z][a-zA-Z0-9_]*)\)\s*:-', re.MULTILINE)
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = builder_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    pred_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="CREATIONAL_BUILDER",
                        weight=0.90,
                        description=f"Predicate '{pred_name}' implements GoF Builder using stepwise accumulator state threading",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.GOF_BUILDER,
                            target_name=pred_name,
                            location=loc,
                            confidence=Confidence(0.90),
                            evidence=[ev],
                        )
                    )
        return detections


class PrototypeRule(Rule):
    @property
    def name(self) -> str:
        return "GOF_PROTOTYPE"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        proto_pattern = re.compile(r'\b(copy_term|duplicate_term)\s*\(')
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = proto_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    fn_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="CREATIONAL_PROTOTYPE",
                        weight=0.90,
                        description=f"GoF Prototype cloning term with variable unsharing via '{fn_name}'",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.GOF_PROTOTYPE,
                            target_name=fn_name,
                            location=loc,
                            confidence=Confidence(0.90),
                            evidence=[ev],
                        )
                    )
        return detections


class SingletonRule(Rule):
    @property
    def name(self) -> str:
        return "GOF_SINGLETON"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        singleton_pattern = re.compile(r'\b(nb_setval|nb_getval|b_setval|b_getval)\s*\(')
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = singleton_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    fn_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="CREATIONAL_SINGLETON",
                        weight=0.92,
                        description=f"GoF Singleton state access via global non-backtrackable variable '{fn_name}'",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.GOF_SINGLETON,
                            target_name=fn_name,
                            location=loc,
                            confidence=Confidence(0.92),
                            evidence=[ev],
                        )
                    )
        return detections
