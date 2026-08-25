import re
from typing import List
from .base import Rule
from ..code_model import CodeModel
from ..detection import Detection
from ..value_objects import PatternType, Confidence, SourceLocation, EvidenceItem


class AdapterRule(Rule):
    @property
    def name(self) -> str:
        return "GOF_ADAPTER"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        adapter_pattern = re.compile(r'^\s*([a-zA-Z0-9_]*(?:adapter|adapt_|wrap_)[a-zA-Z0-9_]*)\s*\((.*?)\)\s*:-', re.MULTILINE)
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = adapter_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    pred_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="STRUCTURAL_ADAPTER",
                        weight=0.92,
                        description=f"Predicate '{pred_name}' implements GoF Adapter reconciling incompatible predicate signatures",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.GOF_ADAPTER,
                            target_name=pred_name,
                            location=loc,
                            confidence=Confidence(0.92),
                            evidence=[ev],
                        )
                    )
        return detections


class BridgeRule(Rule):
    @property
    def name(self) -> str:
        return "GOF_BRIDGE"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        bridge_pattern = re.compile(r'^\s*([a-zA-Z0-9_]*(?:bridge|driver_execute|backend_eval)[a-zA-Z0-9_]*)\s*\((.*?)\)\s*:-', re.MULTILINE)
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = bridge_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    pred_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="STRUCTURAL_BRIDGE",
                        weight=0.90,
                        description=f"Predicate '{pred_name}' implements GoF Bridge decoupling logical operations from concrete backends",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.GOF_BRIDGE,
                            target_name=pred_name,
                            location=loc,
                            confidence=Confidence(0.90),
                            evidence=[ev],
                        )
                    )
        return detections


class CompositeRule(Rule):
    @property
    def name(self) -> str:
        return "GOF_COMPOSITE"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        comp_pattern = re.compile(r'^\s*([a-zA-Z0-9_]+)\s*\((?:tree|node|group|composite)\((.*?)\)\s*,.*?\)\s*:-', re.MULTILINE)
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = comp_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    pred_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="STRUCTURAL_COMPOSITE",
                        weight=0.92,
                        description=f"Predicate '{pred_name}' implements GoF Composite traversing recursive tree/composite structures",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.GOF_COMPOSITE,
                            target_name=pred_name,
                            location=loc,
                            confidence=Confidence(0.92),
                            evidence=[ev],
                        )
                    )
        return detections


class DecoratorRule(Rule):
    @property
    def name(self) -> str:
        return "GOF_DECORATOR"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        decorator_pattern = re.compile(r'^\s*([a-zA-Z0-9_]*(?:decorate|with_logging|with_timing|with_cache|cached_)[a-zA-Z0-9_]*)\s*\((.*?Goal.*?)\)\s*:-', re.MULTILINE)
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = decorator_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    pred_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="STRUCTURAL_DECORATOR",
                        weight=0.92,
                        description=f"Predicate '{pred_name}' implements GoF Decorator augmenting goal execution dynamically",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.GOF_DECORATOR,
                            target_name=pred_name,
                            location=loc,
                            confidence=Confidence(0.92),
                            evidence=[ev],
                        )
                    )
        return detections


class FacadeRule(Rule):
    @property
    def name(self) -> str:
        return "GOF_FACADE"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        for file in model.files:
            for mod in file.modules:
                if "facade" in mod.name.lower() or "api" in mod.name.lower() or "client" in mod.name.lower():
                    loc = SourceLocation(file_path=file.file_path, line_number=mod.line_number)
                    ev = EvidenceItem(
                        rule_name="STRUCTURAL_FACADE",
                        weight=0.92,
                        description=f"Module '{mod.name}' acts as GoF Facade exporting a simplified unified interface",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.GOF_FACADE,
                            target_name=mod.name,
                            location=loc,
                            confidence=Confidence(0.92),
                            evidence=[ev],
                        )
                    )
        return detections


class FlyweightRule(Rule):
    @property
    def name(self) -> str:
        return "GOF_FLYWEIGHT"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        flyweight_pattern = re.compile(r'\b(trie_new|trie_insert|trie_lookup|atom_intern|table_intern)\s*\(')
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = flyweight_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    fn_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="STRUCTURAL_FLYWEIGHT",
                        weight=0.90,
                        description=f"GoF Flyweight sharing immutable terms or trie tables via '{fn_name}'",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.GOF_FLYWEIGHT,
                            target_name=fn_name,
                            location=loc,
                            confidence=Confidence(0.90),
                            evidence=[ev],
                        )
                    )
        return detections


class ProxyRule(Rule):
    @property
    def name(self) -> str:
        return "GOF_PROXY"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        proxy_pattern = re.compile(r'\b(goal_expansion|term_expansion)\s*\(')
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = proxy_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    fn_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="STRUCTURAL_PROXY",
                        weight=0.90,
                        description=f"GoF Proxy intercepting and rewriting goals via macro hook '{fn_name}'",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.GOF_PROXY,
                            target_name=fn_name,
                            location=loc,
                            confidence=Confidence(0.90),
                            evidence=[ev],
                        )
                    )
        return detections
