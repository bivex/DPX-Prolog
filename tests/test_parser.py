from pattern_detector.adapters.inbound.parsers.prolog_parser import RegexPrologParser

PROLOG_SAMPLE = """
:- module(math_engine, [
    eval_expr/2,
    solve_system/2
]).

:- use_module(library(clpfd)).
:- table fib/2.
:- dynamic memo/2.

% DCG grammar
expr(X) --> term(T), plus, expr(E), { X #= T + E }.
expr(T) --> term(T).

term(N) --> [N], { number(N) }.
plus --> [+].

% Fact
constant_pi(3.14159).

% Horn Clause
eval_expr(add(A, B), Result) :-
    eval_expr(A, VA),
    eval_expr(B, VB),
    Result is VA + VB.

eval_expr(num(N), N).
"""


def test_prolog_parser():
    parser = RegexPrologParser()
    pf = parser.parse_file("src/math_engine.pl", PROLOG_SAMPLE)

    assert len(pf.modules) == 1
    mod = pf.modules[0]
    assert mod.name == "math_engine"
    assert "eval_expr/2" in mod.exported_predicates
    assert "solve_system/2" in mod.exported_predicates

    assert len(pf.directives) >= 3
    assert len(pf.predicates) >= 4

    expr_pred = next((p for p in pf.predicates if p.name == "expr"), None)
    assert expr_pred is not None
    assert any(c.is_dcg for c in expr_pred.clauses)

    fact_pred = next((p for p in pf.predicates if p.name == "constant_pi"), None)
    assert fact_pred is not None
    assert fact_pred.clauses[0].is_fact is True
