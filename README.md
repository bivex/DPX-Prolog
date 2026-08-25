# 🦉 DPX-Prolog: Architectural Pattern & Static Analysis Engine for ISO Prolog, SWI-Prolog, CLP(FD/R/Q) & Logic Programming

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Architecture: Hexagonal DDD](https://img.shields.io/badge/Architecture-Hexagonal%20DDD-green.svg)](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software))
[![Patterns: 45 Rules](https://img.shields.io/badge/Patterns-45%20Rules-red.svg)](#-supported-patterns--hazard-catalog)

**DPX-Prolog** is a high-performance static analysis and architectural pattern detection engine for **ISO Prolog, SWI-Prolog, Scryer Prolog, GNU Prolog, and Constraint Logic Programming** (`.pl`, `.pro`, `.prolog`, `.plt`, `.dcg`, `.chr`).

Analyzes Definite Clause Grammars (DCGs), Constraint Logic Programming (`clpfd`, `clpr`, `clpq`), Constraint Handling Rules (CHR), Meta-interpreters, Tabling/SLG memoization, Higher-order meta-predicates, all 23 Gang of Four (GoF) design patterns mapped to first-class logic relations, and critical declarative hazards (unsafe red cuts, uninstantiated negation-as-failure, unsafe dynamic database `assertz` leaks, arbitrary term execution `call(X)`).

---

## 🏛️ Architecture & Design Philosophy

DPX-Prolog follows Domain-Driven Design and Ports & Adapters (Hexagonal) architecture:

```
src/pattern_detector/
├── domain/                      # Pure Logic Programming domain model (Zero external dependencies)
│   ├── code_model.py            # AST/Code Model (PrologModule, PrologPredicate, PrologClause, PrologDirective, PrologFile)
│   ├── detection.py             # Detection & DetectionReport aggregates
│   ├── pattern.py               # 45 Pattern catalog definitions & weights
│   ├── value_objects.py         # Confidence, SourceLocation, PatternCategory, PatternType
│   └── rules/                   # 45 Pattern Detection Rules
│       ├── logic_rules.py       # DCG Grammars, CLP(FD/R/Q) Constraints, CHR Rules, Tabling SLG, Meta-Interpreters
│       ├── higher_order_rules.py# Higher-Order Meta-Predicates (maplist, foldl, include, findall/setof)
│       ├── creational_rules.py  # All 5 GoF Creational Patterns (Factory Method, Abstract Factory, Builder, Prototype, Singleton)
│       ├── structural_rules.py  # All 7 GoF Structural Patterns (Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy)
│       ├── behavioral_rules.py  # All 11 GoF Behavioral Patterns (Chain of Resp, Command, Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor)
│       ├── hazard_rules.py      # Unsafe Red Cuts, Arbitrary Goal Execution (call/N), Dynamic Assert Leaks, Flawed Negation, Left Recursion
│       └── solid_principles_rules.py # Monolithic Module SRP, Fat Predicate Arity, Impure State Mutation
├── ports/                       # Interfaces defining domain boundaries
│   ├── inbound/                 # ParserPort, PatternDetectorPort
│   └── outbound/                # ExporterPort (HTML HUD, JSON, Markdown, SARIF)
├── adapters/                    # Concrete technology implementations
│   ├── inbound/
│   │   ├── parsers/             # RegexPrologParser (Single-pass Horn clause & DCG parser)
│   │   ├── detectors/           # PrologPatternDetector engine
│   │   └── cli/                 # Typer & Rich interactive CLI
│   └── outbound/
│       └── exporters/           # Interactive HTML HUD (Logic Navy & Crimson + "Copy for AI" button), SARIF v2.1.0, JSON, Markdown
└── application/
    └── scan_service.py          # Orchestration service
```

---

## 🔍 Supported Patterns & Hazard Catalog (45 Rules)

| Category | Pattern Type | Target / Construct | Default Weight | Description |
|---|---|---|:---:|---|
| **Logic & Constraints** | `definite_clause_grammar` | `Rule --> ... / phrase/3` | 95% | Definite Clause Grammar (DCG) parsing and list accumulator difference lists |
| | `clpfd_constraint_reasoning` | `#=, #>, in, labeling/2` | 95% | Constraint Logic Programming over Finite Domains for declarative constraint solving |
| | `clpr_real_constraint_solving` | `{X + Y = 10}` | 92% | Constraint Logic Programming over Real/Rational numbers (CLP(R) / CLP(Q)) |
| | `constraint_handling_rules` | `rule @ Head <=> Guard \| Body`| 95% | Constraint Handling Rules (CHR) committed-choice language extension |
| | `tabling_memoization_slg` | `:- table Pred/Arity.` | 95% | SLG Resolution tabling avoiding infinite recursion in recursive graph traversals |
| | `meta_interpreter_vanilla` | `solve(Goal) :- ...` | 92% | Meta-circular interpreter evaluating object-level logic programs |
| **Higher-Order Meta** | `higher_order_maplist` | `maplist/N, include/3, foldl/4` | 92% | Functional higher-order list processing preserving declarative purity |
| | `all_solutions_aggregation` | `findall/3, setof/3, bagof/3` | 90% | Higher-order second-order predicates collecting non-deterministic solution sets |
| **GoF Creational (5/5)** | `gof_factory_method` | Dynamic term constructor | 92% | Factory Method pattern constructing specialized functor terms based on type descriptor |
| | `gof_abstract_factory` | Polymorphic predicate family | 92% | Abstract Factory generating families of related logical records |
| | `gof_builder` | Accumulator pair / DCG state | 90% | Builder pattern constructing complex terms via stepwise accumulator threading |
| | `gof_prototype` | `copy_term/2, duplicate_term/2` | 90% | Prototype pattern cloning terms with fresh variable bindings |
| | `gof_singleton` | Dynamic fact / `nb_setval` | 92% | Singleton pattern maintaining unique global state or single database fact |
| **GoF Structural (7/7)** | `gof_adapter` | Signature adapting predicate | 92% | Adapter pattern translating foreign predicate signatures into target protocol |
| | `gof_bridge` | Decoupled solver / driver bridge | 90% | Bridge pattern decoupling high-level query goals from backend evaluation engines |
| | `gof_composite` | Recursive tree term predicates | 92% | Composite pattern handling recursive tree structures (`node/2`, `tree/3`) uniformly |
| | `gof_decorator` | Goal wrapper / pre-post hooks | 92% | Decorator pattern dynamically augmenting predicate evaluation with logging/caching |
| | `gof_facade` | Module export unified facade | 92% | Facade pattern exposing high-level module interface concealing internal clause nets |
| | `gof_flyweight` | Atom interning / Trie lookup table | 90% | Flyweight pattern sharing immutable atomic terms and symbol dictionaries |
| | `gof_proxy` | `goal_expansion / term_expansion` | 90% | Proxy pattern intercepting and rewriting goals at compile or runtime |
| **GoF Behavioral (11/11)**| `gof_chain_of_responsibility`| Disjunctive fallback pipeline | 95% | Chain of Responsibility trying disjunctive clauses sequentially (`(A ; B ; C)`) |
| | `gof_command` | First-class goal reification | 95% | Command pattern encapsulating executable goals executed via `call/N` or `catch/3` |
| | `gof_interpreter` | AST Expression evaluator | 90% | Interpreter pattern evaluating domain-specific AST expressions |
| | `gof_iterator` | Backtracking generator | 92% | Iterator pattern generating elements sequentially on backtracking (`member/2`) |
| | `gof_mediator` | Dynamic blackboard coordinator | 90% | Mediator pattern decoupling predicates via shared dynamic blackboard |
| | `gof_memento` | Transaction snapshot & rollback | 90% | Memento pattern recording database checkpoints with undo/rollback |
| | `gof_observer` | Hook broadcast / listener table | 95% | Observer / PubSub pattern notifying registered listener predicates of events |
| | `gof_state` | Accumulator state passing (`S0 -> S1`)| 95% | State pattern altering behavior through explicit threaded state variables |
| | `gof_strategy` | Higher-order goal strategy injection | 92% | Strategy pattern injecting interchangeable evaluation goals into `call/N` |
| | `gof_template_method` | Skeleton clause calling hook | 90% | Template Method defining algorithm skeleton with `multifile` hook overrides |
| | `gof_visitor` | Recursive term walker (`=..`) | 92% | Visitor pattern traversing compound terms using univ (`=..`) and `term_variables` |
| **Logic & Safety Hazards** | `unsafe_cut_red_cut_hazard` | Non-green cut (`!`) | 95% | Procedural cut destroying declarative semantics and bidirectionality |
| | `unsafe_term_evaluation_hazard`| `call(Untrusted), atom_to_term/3` | 95% | Arbitrary goal execution vulnerability evaluating unsanitized user inputs |
| | `unsafe_dynamic_assert_hazard` | Unmanaged `assertz/retract` | 92% | State leakage and database pollution via unmanaged dynamic assertions |
| | `unsafe_io_system_hazard` | `shell/1, process_create/3` | 95% | Command injection executing unquoted shell strings |
| | `infinite_left_recursion_hazard`| Direct left recursion without table | 92% | Left-recursive clause risking stack overflow / infinite loop in SLD resolution |
| | `uninstantiated_var_negation_hazard`| `\+ var(X), not(Goal)` | 90% | Flawed negation-as-failure on uninstantiated variables violating soundness |
| | `missing_module_export_hazard` | Clauses outside module encapsulation | 88% | Global namespace pollution lacking `:- module/2` export boundary |
| **SOLID Principles in Prolog** | `monolithic_module_srp` | Module exports > 25 predicates | 85% | Monolithic module violating Single Responsibility; split into submodules |
| | `fat_predicate_arity_srp` | Predicate arity >= 8 | 85% | Excessive predicate arguments violating readability and clean composability |
| | `impure_state_mutation_srp` | Mixing pure clauses with `assertz` | 88% | Impure side-effects inside logical relation breaking referential transparency |

---

## ⚡ Installation & CLI Usage

```bash
# Clone repository
git clone https://github.com/bivex/DPX-Prolog.git
cd DPX-Prolog

# Install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

### 🚀 Running Analysis

```bash
# 1. Quick scan on Prolog codebases
dpx-prolog scan src/

# 2. Export Full Interactive HTML HUD + SARIF + JSON + Markdown
dpx-prolog scan src/ \
    -H reports/dpx_prolog_hud.html \
    -J reports/dpx_prolog_findings.json \
    -M reports/dpx_prolog_report.md \
    -S reports/dpx_prolog_report.sarif

# 3. View 45 supported pattern catalog
dpx-prolog catalog
```

---

## 🌐 The DPX Multi-Language Static Analysis Family (33 Languages)

| # | Language | Repository | Ecosystem & Focus |
|:---:|---|---|---|
| 1 | **Ada** | [`bivex/DPX-Ada`](https://github.com/bivex/DPX-Ada) | Ada 2012/2022, SPARK Contracts, Ravenscar Tasking, DO-178C Safety |
| 2 | **Clojure** | [`bivex/DPX`](https://github.com/bivex/DPX) | Lisp S-Expressions, Protocols, Multimethods |
| 3 | **C** | [`bivex/DPX-C`](https://github.com/bivex/DPX-C) | Memory Safety, Struct VTables, Idiomatic C11/C23 |
| 4 | **Cairo** | [`bivex/DPX-Cairo`](https://github.com/bivex/DPX-Cairo) | Starknet Smart Contracts, ZK-Rollup Invariants |
| 5 | **C++** | [`bivex/DPX-Cpp`](https://github.com/bivex/DPX-Cpp) | RAII, CRTP, Concepts, Modern C++20/23 |
| 6 | **C#** | [`bivex/DPX-CSharp`](https://github.com/bivex/DPX-CSharp) | .NET 9, Roslyn AST, Linq, Records |
| 7 | **Dart** | [`bivex/DPX-Dart`](https://github.com/bivex/DPX-Dart) | Dart 3.x, Flutter, BLoC, Riverpod, Isolates |
| 8 | **Elixir** | [`bivex/DPX-Elixir`](https://github.com/bivex/DPX-Elixir) | BEAM OTP, GenServer, Supervisors |
| 9 | **Erlang** | [`bivex/DPX-Erlang`](https://github.com/bivex/DPX-Erlang) | Fault Tolerance, Actor Model, OTP Behaviors |
| 10 | **Gleam** | [`bivex/DPX-Gleam`](https://github.com/bivex/DPX-Gleam) | Type-Safe BEAM, Actor Concurrency |
| 11 | **Go** | [`bivex/DPX-Go`](https://github.com/bivex/DPX-Go) | Goroutines, Channels, Composition, Interfaces |
| 12 | **Haskell** | [`bivex/DPX-Haskell`](https://github.com/bivex/DPX-Haskell) | Pure Functional, Monads, Typeclasses, Arrows |
| 13 | **Huff** | [`bivex/DPX-Huff`](https://github.com/bivex/DPX-Huff) | Low-Level EVM Bytecode & Opcodes |
| 14 | **Idris 2** | [`bivex/DPX-Idris2`](https://github.com/bivex/DPX-Idris2) | Dependent Types, QTT Linear Protocols, Totality, Proofs |
| 15 | **Java** | [`bivex/DPX-Java`](https://github.com/bivex/DPX-Java) | Spring Boot, Enterprise Java, JVM Invariants |
| 16 | **Julia** | [`bivex/DPX-Julia`](https://github.com/bivex/DPX-Julia) | Multiple Dispatch, Scientific Computing |
| 17 | **Kotlin** | [`bivex/DPX-Kotlin`](https://github.com/bivex/DPX-Kotlin) | Coroutines, Multiplatform, Functional DSLs |
| 18 | **Lua** | [`bivex/DPX-Lua`](https://github.com/bivex/DPX-Lua) | Metatables, Coroutines, LuaJIT, Neovim |
| 19 | **Mojo** | [`bivex/DPX-Mojo`](https://github.com/bivex/DPX-Mojo) | SIMD Hardware, Memory Lifetimes, AI Systems |
| 20 | **Move** | [`bivex/DPX-Move`](https://github.com/bivex/DPX-Move) | Aptos & Sui Resource Safety, Linear Types |
| 21 | **OCaml** | [`bivex/DPX-OCaml`](https://github.com/bivex/DPX-OCaml) | Algebraic Data Types, Functors, Polymorphism |
| 22 | **PHP** | [`bivex/DPX-Php`](https://github.com/bivex/DPX-Php) | Modern PHP 8.4, Attributes, Traits, Laravel |
| 23 | **Prolog** | **[`bivex/DPX-Prolog`](https://github.com/bivex/DPX-Prolog)** | **ISO Prolog, SWI-Prolog, DCG, CLP(FD/R/Q), CHR, Meta-Interpreters** |
| 24 | **Puppet** | [`bivex/DPX-Puppet`](https://github.com/bivex/DPX-Puppet) | Puppet DSL, Roles/Profiles, IaC Security, Hiera |
| 25 | **Python** | [`bivex/DPX-Py`](https://github.com/bivex/DPX-Py) | Metaprogramming, Protocols, Hexagonal DDD |
| 26 | **Ruby** | [`bivex/DPX-Ruby`](https://github.com/bivex/DPX-Ruby) | Ruby 3.x, Rails, Metaprogramming, Dry-RB, Security |
| 27 | **Rust** | [`bivex/DPX-Rust`](https://github.com/bivex/DPX-Rust) | Zero-Cost Abstractions, Borrow Checker, Traits |
| 28 | **Solidity** | [`bivex/DPX-Solidity`](https://github.com/bivex/DPX-Solidity) | DeFi Security, Reentrancy, EVM Yul/Assembly |
| 29 | **SQL** | [`bivex/DPX-SQL`](https://github.com/bivex/DPX-SQL) | PostgreSQL, MySQL, SQLite, T-SQL, PL/SQL |
| 30 | **Swift** | [`bivex/DPX-Swift`](https://github.com/bivex/DPX-Swift) | Protocol-Oriented Programming, Actors |
| 31 | **TypeScript** | [`bivex/DPX-TypeScript`](https://github.com/bivex/DPX-TypeScript) | Generics, Conditional Types, Clean Architecture |
| 32 | **Yul** | [`bivex/DPX-Yul`](https://github.com/bivex/DPX-Yul) | EVM Intermediate Representation Optimization |
| 33 | **Zig** | [`bivex/DPX-Zig`](https://github.com/bivex/DPX-Zig) | Comptime, Manual Memory Allocators, C ABI |

---

## 📄 License

MIT License © 2026 Bivex
