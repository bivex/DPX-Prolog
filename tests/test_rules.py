from pattern_detector.adapters.inbound.parsers.prolog_parser import RegexPrologParser
from pattern_detector.adapters.inbound.detectors.prolog_detector import PrologPatternDetector
from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.value_objects import PatternType

COMPREHENSIVE_PROLOG_CODE = """
:- module(avionics_expert, [
    parse_flight_plan/2,
    solve_clp/2,
    solve/1
]).

:- use_module(library(clpfd)).
:- use_module(library(clpr)).
:- use_module(library(chr)).
:- table shortest_path/3.

% Logic & Constraints: DCG
flight_plan(Route) --> [takeoff], waypoint(W), [landing].
waypoint(wpt(Lat, Lon)) --> [lat, Lat, lon, Lon].

% Logic & Constraints: CLP(FD)
solve_clp(Vars, Result) :-
    Vars = [A, B, C],
    Vars ins 1..100,
    A + B #= C,
    labeling([ff], Vars),
    Result = C.

% Logic & Constraints: CLP(R)
solve_real(X, Y) :-
    { X + Y = 10.5, X - Y = 2.5 }.

% Logic & Constraints: CHR
chr_constraint leq/2.
reflexivity @ leq(X, X) <=> true.

% Logic & Constraints: Tabling
shortest_path(X, Y, D) :- edge(X, Y, D).
shortest_path(X, Y, D) :- shortest_path(X, Z, D1), edge(Z, Y, D2), D is D1 + D2.

% Logic & Constraints: Meta-Interpreter
solve(true) :- !.
solve((A, B)) :- !, solve(A), solve(B).
solve(Goal) :- clause(Goal, Body), solve(Body).

% Higher-Order Meta
process_telemetry(Input, Output) :-
    maplist(transform_point, Input, Output),
    include(valid_point, Output, Filtered),
    findall(X, member(X, Filtered), AllSol).

% 1. GoF Creational (5/5)
create_aircraft_record(Type, ID, aircraft(Type, ID)) :- !.
abstract_factory_sensor(Type, Sensor) :- factory_family_builder(Type, Sensor).
with_builder_param(Param, S0, S1) :- S1 = [Param|S0].
clone_object(Obj, Clone) :- copy_term(Obj, Clone).
singleton_state(Val) :- nb_setval(global_config, Val).

% 2. GoF Structural (7/7)
adapt_arinc_msg(ForeignMsg, StandardMsg) :- ForeignMsg =.. [arinc, Data], StandardMsg = msg(Data).
driver_execute_bridge(Backend, Query, Res) :- call(Backend, Query, Res).
eval_tree(tree(Left, Right), Res) :- eval_tree(Left, L), eval_tree(Right, R), Res is L + R.
decorate_goal_timing(Goal) :- get_time(T0), call(Goal), get_time(T1), D is T1 - T0.
flyweight_symbol(Sym, ID) :- trie_lookup(sym_table, Sym, ID).
proxy_rewrite :- goal_expansion(old_goal(X), new_goal(X)).

% 3. GoF Behavioral (11/11)
handle_alarm(Sensor, Event) :- try_primary(Sensor, Event) ; fallback_alarm(Sensor, Event).
execute_cmd(Command) :- call(Command).
eval_expr(add(A, B), Res) :- eval_expr(A, VA), eval_expr(B, VB), Res is VA + VB.
iterator_stream(Item) :- member(Item, [1, 2, 3]).
mediator_broadcast(Msg) :- blackboard_notify(Msg).
snapshot_memento(State) :- save_state(State).
subscribe_observer(Event, Handler) :- add_observer(Event, Handler).
state_step(action, S0, S) :- S is S0 + 1.
with_strategy(Strategy, Input, Res) :- call(Strategy, Input, Res).
process_pipeline_flow(Data, Res) :- algorithm_skeleton(Data, Res).
visit_term(Term) :- Term =.. [_|Args], maplist(visit_term, Args).

% Logic & Safety Hazards
unsafe_eval(Input) :- atom_to_term(Input, Term, _), call(Term).
unsafe_mutation(Item) :- assertz(cached(Item)).
unsafe_system(Cmd) :- shell(Cmd).
unsound_negation(X) :- \\+ var(X).

% SOLID Arity SRP Violation
fat_predicate(A, B, C, D, E, F, G, H, I) :- true.
"""

FACADE_MODULE = """
:- module(avionics_facade, [
    init_all/0,
    start_flight/1
]).

init_all :- true.
start_flight(F) :- true.
"""


def test_rule_evaluations():
    parser = RegexPrologParser()
    pf1 = parser.parse_file("src/avionics_expert.pl", COMPREHENSIVE_PROLOG_CODE)
    pf2 = parser.parse_file("src/avionics_facade.pl", FACADE_MODULE)

    model = CodeModel()
    model.add_file(pf1)
    model.add_file(pf2)

    detector = PrologPatternDetector()
    report = detector.detect(model)

    detected_types = {d.pattern_type for d in report.detections}

    # Logic & Constraints
    assert PatternType.DEFINITE_CLAUSE_GRAMMAR in detected_types
    assert PatternType.CLPFD_CONSTRAINT_REASONING in detected_types
    assert PatternType.CLPR_REAL_CONSTRAINT_SOLVING in detected_types
    assert PatternType.CONSTRAINT_HANDLING_RULES in detected_types
    assert PatternType.TABLING_MEMOIZATION_SLG in detected_types
    assert PatternType.META_INTERPRETER_VANILLA in detected_types

    # Higher-Order
    assert PatternType.HIGHER_ORDER_MAPLIST in detected_types
    assert PatternType.ALL_SOLUTIONS_AGGREGATION in detected_types

    # Creational (5/5)
    assert PatternType.GOF_FACTORY_METHOD in detected_types
    assert PatternType.GOF_ABSTRACT_FACTORY in detected_types
    assert PatternType.GOF_BUILDER in detected_types
    assert PatternType.GOF_PROTOTYPE in detected_types
    assert PatternType.GOF_SINGLETON in detected_types

    # Structural (7/7)
    assert PatternType.GOF_ADAPTER in detected_types
    assert PatternType.GOF_BRIDGE in detected_types
    assert PatternType.GOF_COMPOSITE in detected_types
    assert PatternType.GOF_DECORATOR in detected_types
    assert PatternType.GOF_FACADE in detected_types
    assert PatternType.GOF_FLYWEIGHT in detected_types
    assert PatternType.GOF_PROXY in detected_types

    # Behavioral (11/11)
    assert PatternType.GOF_CHAIN_OF_RESPONSIBILITY in detected_types
    assert PatternType.GOF_COMMAND in detected_types
    assert PatternType.GOF_INTERPRETER in detected_types
    assert PatternType.GOF_ITERATOR in detected_types
    assert PatternType.GOF_MEDIATOR in detected_types
    assert PatternType.GOF_MEMENTO in detected_types
    assert PatternType.GOF_OBSERVER in detected_types
    assert PatternType.GOF_STATE in detected_types
    assert PatternType.GOF_STRATEGY in detected_types
    assert PatternType.GOF_TEMPLATE_METHOD in detected_types
    assert PatternType.GOF_VISITOR in detected_types

    # Hazards
    assert PatternType.UNSAFE_CUT_RED_CUT_HAZARD in detected_types
    assert PatternType.UNSAFE_TERM_EVALUATION_HAZARD in detected_types
    assert PatternType.UNSAFE_DYNAMIC_ASSERT_HAZARD in detected_types
    assert PatternType.UNSAFE_IO_SYSTEM_HAZARD in detected_types
    assert PatternType.UNINSTANTIATED_VAR_NEGATION_HAZARD in detected_types

    # SOLID
    assert PatternType.FAT_PREDICATE_ARITY_SRP in detected_types
