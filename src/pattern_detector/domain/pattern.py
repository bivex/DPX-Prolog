from dataclasses import dataclass
from typing import Dict
from .value_objects import PatternCategory, PatternType


@dataclass(frozen=True)
class PatternMetadata:
    pattern_type: PatternType
    name: str
    category: PatternCategory
    description: str
    default_weight: float


PATTERN_CATALOG: Dict[PatternType, PatternMetadata] = {
    # Logic & Constraints
    PatternType.DEFINITE_CLAUSE_GRAMMAR: PatternMetadata(
        pattern_type=PatternType.DEFINITE_CLAUSE_GRAMMAR,
        name="Definite Clause Grammar (DCG)",
        category=PatternCategory.LOGIC_CONSTRAINTS,
        description="Definite Clause Grammar (Rule --> ...) for declarative syntactic parsing and difference lists.",
        default_weight=0.95,
    ),
    PatternType.CLPFD_CONSTRAINT_REASONING: PatternMetadata(
        pattern_type=PatternType.CLPFD_CONSTRAINT_REASONING,
        name="CLP(FD) Constraint Reasoning",
        category=PatternCategory.LOGIC_CONSTRAINTS,
        description="Constraint Logic Programming over Finite Domains (#=, #>, in, labeling/2) for combinatorial search.",
        default_weight=0.95,
    ),
    PatternType.CLPR_REAL_CONSTRAINT_SOLVING: PatternMetadata(
        pattern_type=PatternType.CLPR_REAL_CONSTRAINT_SOLVING,
        name="CLP(R/Q) Real Constraint Solving",
        category=PatternCategory.LOGIC_CONSTRAINTS,
        description="Constraint Logic Programming over Real/Rational numbers ({Equations}) for algebraic reasoning.",
        default_weight=0.92,
    ),
    PatternType.CONSTRAINT_HANDLING_RULES: PatternMetadata(
        pattern_type=PatternType.CONSTRAINT_HANDLING_RULES,
        name="Constraint Handling Rules (CHR)",
        category=PatternCategory.LOGIC_CONSTRAINTS,
        description="Committed-choice rule-based language extension (rule @ Head <=> Guard | Body) for user-defined constraint solvers.",
        default_weight=0.95,
    ),
    PatternType.TABLING_MEMOIZATION_SLG: PatternMetadata(
        pattern_type=PatternType.TABLING_MEMOIZATION_SLG,
        name="Tabling / SLG Memoization",
        category=PatternCategory.LOGIC_CONSTRAINTS,
        description="SLG Resolution tabling (:- table Pred/Arity.) preventing infinite loops in cyclic graphs.",
        default_weight=0.95,
    ),
    PatternType.META_INTERPRETER_VANILLA: PatternMetadata(
        pattern_type=PatternType.META_INTERPRETER_VANILLA,
        name="Vanilla Meta-Interpreter",
        category=PatternCategory.LOGIC_CONSTRAINTS,
        description="Meta-circular clause evaluator (solve/1, clause/2) evaluating object-level logic programs.",
        default_weight=0.92,
    ),

    # Higher-Order Meta
    PatternType.HIGHER_ORDER_MAPLIST: PatternMetadata(
        pattern_type=PatternType.HIGHER_ORDER_MAPLIST,
        name="Higher-Order Meta-Predicates",
        category=PatternCategory.HIGHER_ORDER_META,
        description="Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4.",
        default_weight=0.92,
    ),
    PatternType.ALL_SOLUTIONS_AGGREGATION: PatternMetadata(
        pattern_type=PatternType.ALL_SOLUTIONS_AGGREGATION,
        name="All-Solutions Aggregation",
        category=PatternCategory.HIGHER_ORDER_META,
        description="Second-order aggregation predicates (findall/3, setof/3, bagof/3) collecting solution sets.",
        default_weight=0.90,
    ),

    # --- ALL 23 GANG OF FOUR (GoF) PATTERNS ---

    # 1. GoF Creational (5/5)
    PatternType.GOF_FACTORY_METHOD: PatternMetadata(
        pattern_type=PatternType.GOF_FACTORY_METHOD,
        name="GoF Factory Method",
        category=PatternCategory.GOF_CREATIONAL,
        description="Creational pattern constructing specialized compound functor terms based on type descriptor.",
        default_weight=0.92,
    ),
    PatternType.GOF_ABSTRACT_FACTORY: PatternMetadata(
        pattern_type=PatternType.GOF_ABSTRACT_FACTORY,
        name="GoF Abstract Factory",
        category=PatternCategory.GOF_CREATIONAL,
        description="Creational pattern generating families of related logical records without specifying concrete functors.",
        default_weight=0.92,
    ),
    PatternType.GOF_BUILDER: PatternMetadata(
        pattern_type=PatternType.GOF_BUILDER,
        name="GoF Builder",
        category=PatternCategory.GOF_CREATIONAL,
        description="Creational pattern assembling complex terms stepwise via accumulator threading or DCG grammars.",
        default_weight=0.90,
    ),
    PatternType.GOF_PROTOTYPE: PatternMetadata(
        pattern_type=PatternType.GOF_PROTOTYPE,
        name="GoF Prototype",
        category=PatternCategory.GOF_CREATIONAL,
        description="Creational pattern cloning terms with fresh variable allocations via copy_term/2 or duplicate_term/2.",
        default_weight=0.90,
    ),
    PatternType.GOF_SINGLETON: PatternMetadata(
        pattern_type=PatternType.GOF_SINGLETON,
        name="GoF Singleton",
        category=PatternCategory.GOF_CREATIONAL,
        description="Creational pattern maintaining a unique dynamic database fact or global variable (nb_setval).",
        default_weight=0.92,
    ),

    # 2. GoF Structural (7/7)
    PatternType.GOF_ADAPTER: PatternMetadata(
        pattern_type=PatternType.GOF_ADAPTER,
        name="GoF Adapter",
        category=PatternCategory.GOF_STRUCTURAL,
        description="Structural pattern translating foreign predicate signatures and argument layouts into target protocols.",
        default_weight=0.92,
    ),
    PatternType.GOF_BRIDGE: PatternMetadata(
        pattern_type=PatternType.GOF_BRIDGE,
        name="GoF Bridge",
        category=PatternCategory.GOF_STRUCTURAL,
        description="Structural pattern decoupling high-level logical relations from backend database/solver drivers.",
        default_weight=0.90,
    ),
    PatternType.GOF_COMPOSITE: PatternMetadata(
        pattern_type=PatternType.GOF_COMPOSITE,
        name="GoF Composite",
        category=PatternCategory.GOF_STRUCTURAL,
        description="Structural pattern composing terms into recursive tree structures (node/2, tree/3) handled uniformly.",
        default_weight=0.92,
    ),
    PatternType.GOF_DECORATOR: PatternMetadata(
        pattern_type=PatternType.GOF_DECORATOR,
        name="GoF Decorator",
        category=PatternCategory.GOF_STRUCTURAL,
        description="Structural pattern dynamically wrapping goal evaluation with pre/post hooks, logging, or caching.",
        default_weight=0.92,
    ),
    PatternType.GOF_FACADE: PatternMetadata(
        pattern_type=PatternType.GOF_FACADE,
        name="GoF Facade",
        category=PatternCategory.GOF_STRUCTURAL,
        description="Structural pattern providing a unified module interface concealing complex internal clause networks.",
        default_weight=0.92,
    ),
    PatternType.GOF_FLYWEIGHT: PatternMetadata(
        pattern_type=PatternType.GOF_FLYWEIGHT,
        name="GoF Flyweight",
        category=PatternCategory.GOF_STRUCTURAL,
        description="Structural pattern sharing immutable atomic terms and symbol tables using trie indexing.",
        default_weight=0.90,
    ),
    PatternType.GOF_PROXY: PatternMetadata(
        pattern_type=PatternType.GOF_PROXY,
        name="GoF Proxy",
        category=PatternCategory.GOF_STRUCTURAL,
        description="Structural pattern intercepting and rewriting goals via goal_expansion/2 or term_expansion/2.",
        default_weight=0.90,
    ),

    # 3. GoF Behavioral (11/11)
    PatternType.GOF_CHAIN_OF_RESPONSIBILITY: PatternMetadata(
        pattern_type=PatternType.GOF_CHAIN_OF_RESPONSIBILITY,
        name="GoF Chain of Responsibility",
        category=PatternCategory.GOF_BEHAVIORAL,
        description="Behavioral pattern passing requests through disjunctive clause branches until one succeeds.",
        default_weight=0.95,
    ),
    PatternType.GOF_COMMAND: PatternMetadata(
        pattern_type=PatternType.GOF_COMMAND,
        name="GoF Command",
        category=PatternCategory.GOF_BEHAVIORAL,
        description="Behavioral pattern encapsulating an executable goal as a reified term executed via call/N or catch/3.",
        default_weight=0.95,
    ),
    PatternType.GOF_INTERPRETER: PatternMetadata(
        pattern_type=PatternType.GOF_INTERPRETER,
        name="GoF Interpreter",
        category=PatternCategory.GOF_BEHAVIORAL,
        description="Behavioral pattern evaluating domain-specific grammar or AST expression trees.",
        default_weight=0.90,
    ),
    PatternType.GOF_ITERATOR: PatternMetadata(
        pattern_type=PatternType.GOF_ITERATOR,
        name="GoF Iterator",
        category=PatternCategory.GOF_BEHAVIORAL,
        description="Behavioral pattern generating elements sequentially on backtracking (member/2, between/3).",
        default_weight=0.92,
    ),
    PatternType.GOF_MEDIATOR: PatternMetadata(
        pattern_type=PatternType.GOF_MEDIATOR,
        name="GoF Mediator",
        category=PatternCategory.GOF_BEHAVIORAL,
        description="Behavioral pattern coordinating colleague predicates through a centralized dynamic blackboard.",
        default_weight=0.90,
    ),
    PatternType.GOF_MEMENTO: PatternMetadata(
        pattern_type=PatternType.GOF_MEMENTO,
        name="GoF Memento",
        category=PatternCategory.GOF_BEHAVIORAL,
        description="Behavioral pattern recording database snapshots and transactional state checkpoints for rollback.",
        default_weight=0.90,
    ),
    PatternType.GOF_OBSERVER: PatternMetadata(
        pattern_type=PatternType.GOF_OBSERVER,
        name="GoF Observer",
        category=PatternCategory.GOF_BEHAVIORAL,
        description="Behavioral pattern broadcasting events to registered listener predicates or dynamic hook tables.",
        default_weight=0.95,
    ),
    PatternType.GOF_STATE: PatternMetadata(
        pattern_type=PatternType.GOF_STATE,
        name="GoF State",
        category=PatternCategory.GOF_BEHAVIORAL,
        description="Behavioral pattern threading explicit state variables (State0 -> State1 -> StateN) through relations.",
        default_weight=0.95,
    ),
    PatternType.GOF_STRATEGY: PatternMetadata(
        pattern_type=PatternType.GOF_STRATEGY,
        name="GoF Strategy",
        category=PatternCategory.GOF_BEHAVIORAL,
        description="Behavioral pattern injecting interchangeable algorithmic goal closures into call/N or maplist/N.",
        default_weight=0.92,
    ),
    PatternType.GOF_TEMPLATE_METHOD: PatternMetadata(
        pattern_type=PatternType.GOF_TEMPLATE_METHOD,
        name="GoF Template Method",
        category=PatternCategory.GOF_BEHAVIORAL,
        description="Behavioral pattern defining skeleton relation calling customizable multifile hook predicates.",
        default_weight=0.90,
    ),
    PatternType.GOF_VISITOR: PatternMetadata(
        pattern_type=PatternType.GOF_VISITOR,
        name="GoF Visitor",
        category=PatternCategory.GOF_BEHAVIORAL,
        description="Behavioral pattern traversing compound terms using univ (=..) and term_variables/2.",
        default_weight=0.92,
    ),

    # Logic & Safety Hazards
    PatternType.UNSAFE_CUT_RED_CUT_HAZARD: PatternMetadata(
        pattern_type=PatternType.UNSAFE_CUT_RED_CUT_HAZARD,
        name="Unsafe Red Cut Hazard",
        category=PatternCategory.LOGIC_HAZARDS,
        description="Procedural cut (!) altering logical semantics and breaking commutativity/declarative purity.",
        default_weight=0.95,
    ),
    PatternType.UNSAFE_TERM_EVALUATION_HAZARD: PatternMetadata(
        pattern_type=PatternType.UNSAFE_TERM_EVALUATION_HAZARD,
        name="Unsafe Goal Evaluation Hazard",
        category=PatternCategory.LOGIC_HAZARDS,
        description="Evaluating untrusted goal input via call/N or atom_to_term/3 risking arbitrary code execution.",
        default_weight=0.95,
    ),
    PatternType.UNSAFE_DYNAMIC_ASSERT_HAZARD: PatternMetadata(
        pattern_type=PatternType.UNSAFE_DYNAMIC_ASSERT_HAZARD,
        name="Unsafe Dynamic Database Assertion Hazard",
        category=PatternCategory.LOGIC_HAZARDS,
        description="Unmanaged assertz/retract creating memory leaks and dynamic database pollution.",
        default_weight=0.92,
    ),
    PatternType.UNSAFE_IO_SYSTEM_HAZARD: PatternMetadata(
        pattern_type=PatternType.UNSAFE_IO_SYSTEM_HAZARD,
        name="OS Command Injection Hazard",
        category=PatternCategory.LOGIC_HAZARDS,
        description="Executing shell commands (shell/1, process_create/3) with unsanitized atom arguments.",
        default_weight=0.95,
    ),
    PatternType.INFINITE_LEFT_RECURSION_HAZARD: PatternMetadata(
        pattern_type=PatternType.INFINITE_LEFT_RECURSION_HAZARD,
        name="Infinite Left Recursion Hazard",
        category=PatternCategory.LOGIC_HAZARDS,
        description="Direct left recursion in clause body causing infinite loops during SLD resolution.",
        default_weight=0.92,
    ),
    PatternType.UNINSTANTIATED_VAR_NEGATION_HAZARD: PatternMetadata(
        pattern_type=PatternType.UNINSTANTIATED_VAR_NEGATION_HAZARD,
        name="Flawed Negation-as-Failure Hazard",
        category=PatternCategory.LOGIC_HAZARDS,
        description="Calling negation (\\+ or not) on uninstantiated variables producing unsound logical answers.",
        default_weight=0.90,
    ),
    PatternType.MISSING_MODULE_EXPORT_HAZARD: PatternMetadata(
        pattern_type=PatternType.MISSING_MODULE_EXPORT_HAZARD,
        name="Missing Module Encapsulation Hazard",
        category=PatternCategory.LOGIC_HAZARDS,
        description="Prolog file defines global predicates without :- module/2 boundary encapsulation.",
        default_weight=0.88,
    ),

    # SOLID Principles in Prolog
    PatternType.MONOLITHIC_MODULE_SRP: PatternMetadata(
        pattern_type=PatternType.MONOLITHIC_MODULE_SRP,
        name="Monolithic Module (SRP Violation)",
        category=PatternCategory.SOLID_PRINCIPLES,
        description="Module exports excessive predicates (>25); decompose into focused submodules.",
        default_weight=0.85,
    ),
    PatternType.FAT_PREDICATE_ARITY_SRP: PatternMetadata(
        pattern_type=PatternType.FAT_PREDICATE_ARITY_SRP,
        name="Fat Predicate Arity (SRP Violation)",
        category=PatternCategory.SOLID_PRINCIPLES,
        description="Predicate declares excessive arity (>=8); refactor using compound terms or options lists.",
        default_weight=0.85,
    ),
    PatternType.IMPURE_STATE_MUTATION_SRP: PatternMetadata(
        pattern_type=PatternType.IMPURE_STATE_MUTATION_SRP,
        name="Impure State Mutation (SRP Violation)",
        category=PatternCategory.SOLID_PRINCIPLES,
        description="Mixing pure logical deduction with assertz/retract side-effects inside relations.",
        default_weight=0.88,
    ),
}
