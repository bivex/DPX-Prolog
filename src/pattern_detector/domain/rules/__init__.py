from typing import List
from .base import Rule
from .logic_rules import (
    DefiniteClauseGrammarRule,
    ClpfdConstraintReasoningRule,
    ClprRealConstraintSolvingRule,
    ConstraintHandlingRulesRule,
    TablingMemoizationSlgRule,
    MetaInterpreterVanillaRule,
)
from .higher_order_rules import (
    HigherOrderMaplistRule,
    AllSolutionsAggregationRule,
)
from .creational_rules import (
    FactoryMethodRule,
    AbstractFactoryRule,
    BuilderRule,
    PrototypeRule,
    SingletonRule,
)
from .structural_rules import (
    AdapterRule,
    BridgeRule,
    CompositeRule,
    DecoratorRule,
    FacadeRule,
    FlyweightRule,
    ProxyRule,
)
from .behavioral_rules import (
    ChainOfResponsibilityRule,
    CommandRule,
    InterpreterRule,
    IteratorRule,
    MediatorRule,
    MementoRule,
    ObserverRule,
    StateRule,
    StrategyRule,
    TemplateMethodRule,
    VisitorRule,
)
from .hazard_rules import (
    UnsafeCutRedCutHazardRule,
    UnsafeTermEvaluationHazardRule,
    UnsafeDynamicAssertHazardRule,
    UnsafeIoSystemHazardRule,
    InfiniteLeftRecursionHazardRule,
    UninstantiatedVarNegationHazardRule,
    MissingModuleExportHazardRule,
)
from .solid_principles_rules import (
    MonolithicModuleSrpRule,
    FatPredicateAritySrpRule,
    ImpureStateMutationSrpRule,
)


def get_all_rules() -> List[Rule]:
    return [
        # Logic & Constraints
        DefiniteClauseGrammarRule(),
        ClpfdConstraintReasoningRule(),
        ClprRealConstraintSolvingRule(),
        ConstraintHandlingRulesRule(),
        TablingMemoizationSlgRule(),
        MetaInterpreterVanillaRule(),

        # Higher-Order Meta
        HigherOrderMaplistRule(),
        AllSolutionsAggregationRule(),

        # GoF Creational (5/5)
        FactoryMethodRule(),
        AbstractFactoryRule(),
        BuilderRule(),
        PrototypeRule(),
        SingletonRule(),

        # GoF Structural (7/7)
        AdapterRule(),
        BridgeRule(),
        CompositeRule(),
        DecoratorRule(),
        FacadeRule(),
        FlyweightRule(),
        ProxyRule(),

        # GoF Behavioral (11/11)
        ChainOfResponsibilityRule(),
        CommandRule(),
        InterpreterRule(),
        IteratorRule(),
        MediatorRule(),
        MementoRule(),
        ObserverRule(),
        StateRule(),
        StrategyRule(),
        TemplateMethodRule(),
        VisitorRule(),

        # Hazards
        UnsafeCutRedCutHazardRule(),
        UnsafeTermEvaluationHazardRule(),
        UnsafeDynamicAssertHazardRule(),
        UnsafeIoSystemHazardRule(),
        InfiniteLeftRecursionHazardRule(),
        UninstantiatedVarNegationHazardRule(),
        MissingModuleExportHazardRule(),

        # SOLID Principles
        MonolithicModuleSrpRule(),
        FatPredicateAritySrpRule(),
        ImpureStateMutationSrpRule(),
    ]
