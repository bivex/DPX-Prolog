from enum import Enum
from dataclasses import dataclass
from typing import Optional


class PatternCategory(str, Enum):
    LOGIC_CONSTRAINTS = "logic_constraints"
    HIGHER_ORDER_META = "higher_order_meta"
    GOF_CREATIONAL = "gof_creational"
    GOF_STRUCTURAL = "gof_structural"
    GOF_BEHAVIORAL = "gof_behavioral"
    LOGIC_HAZARDS = "logic_hazards"
    SOLID_PRINCIPLES = "solid_principles"


class PatternType(str, Enum):
    # Logic & Constraints
    DEFINITE_CLAUSE_GRAMMAR = "definite_clause_grammar"
    CLPFD_CONSTRAINT_REASONING = "clpfd_constraint_reasoning"
    CLPR_REAL_CONSTRAINT_SOLVING = "clpr_real_constraint_solving"
    CONSTRAINT_HANDLING_RULES = "constraint_handling_rules"
    TABLING_MEMOIZATION_SLG = "tabling_memoization_slg"
    META_INTERPRETER_VANILLA = "meta_interpreter_vanilla"

    # Higher-Order Meta
    HIGHER_ORDER_MAPLIST = "higher_order_maplist"
    ALL_SOLUTIONS_AGGREGATION = "all_solutions_aggregation"

    # GoF Creational (5/5)
    GOF_FACTORY_METHOD = "gof_factory_method"
    GOF_ABSTRACT_FACTORY = "gof_abstract_factory"
    GOF_BUILDER = "gof_builder"
    GOF_PROTOTYPE = "gof_prototype"
    GOF_SINGLETON = "gof_singleton"

    # GoF Structural (7/7)
    GOF_ADAPTER = "gof_adapter"
    GOF_BRIDGE = "gof_bridge"
    GOF_COMPOSITE = "gof_composite"
    GOF_DECORATOR = "gof_decorator"
    GOF_FACADE = "gof_facade"
    GOF_FLYWEIGHT = "gof_flyweight"
    GOF_PROXY = "gof_proxy"

    # GoF Behavioral (11/11)
    GOF_CHAIN_OF_RESPONSIBILITY = "gof_chain_of_responsibility"
    GOF_COMMAND = "gof_command"
    GOF_INTERPRETER = "gof_interpreter"
    GOF_ITERATOR = "gof_iterator"
    GOF_MEDIATOR = "gof_mediator"
    GOF_MEMENTO = "gof_memento"
    GOF_OBSERVER = "gof_observer"
    GOF_STATE = "gof_state"
    GOF_STRATEGY = "gof_strategy"
    GOF_TEMPLATE_METHOD = "gof_template_method"
    GOF_VISITOR = "gof_visitor"

    # Logic & Safety Hazards
    UNSAFE_CUT_RED_CUT_HAZARD = "unsafe_cut_red_cut_hazard"
    UNSAFE_TERM_EVALUATION_HAZARD = "unsafe_term_evaluation_hazard"
    UNSAFE_DYNAMIC_ASSERT_HAZARD = "unsafe_dynamic_assert_hazard"
    UNSAFE_IO_SYSTEM_HAZARD = "unsafe_io_system_hazard"
    INFINITE_LEFT_RECURSION_HAZARD = "infinite_left_recursion_hazard"
    UNINSTANTIATED_VAR_NEGATION_HAZARD = "uninstantiated_var_negation_hazard"
    MISSING_MODULE_EXPORT_HAZARD = "missing_module_export_hazard"

    # SOLID Principles in Prolog
    MONOLITHIC_MODULE_SRP = "monolithic_module_srp"
    FAT_PREDICATE_ARITY_SRP = "fat_predicate_arity_srp"
    IMPURE_STATE_MUTATION_SRP = "impure_state_mutation_srp"


class ConfidenceLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    VERY_HIGH = "VERY_HIGH"


@dataclass(frozen=True)
class SourceLocation:
    file_path: str
    line_number: int
    column_number: int = 1

    def __str__(self) -> str:
        return f"{self.file_path}:{self.line_number}:{self.column_number}"


@dataclass(frozen=True)
class EvidenceItem:
    rule_name: str
    weight: float
    description: str
    location: Optional[SourceLocation] = None


@dataclass
class Confidence:
    value: float  # 0.0 to 1.0

    @property
    def level(self) -> ConfidenceLevel:
        if self.value >= 0.85:
            return ConfidenceLevel.VERY_HIGH
        if self.value >= 0.70:
            return ConfidenceLevel.HIGH
        if self.value >= 0.50:
            return ConfidenceLevel.MEDIUM
        return ConfidenceLevel.LOW

    @property
    def percentage(self) -> int:
        return int(round(self.value * 100))
