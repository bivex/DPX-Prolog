# 🦉 DPX-Prolog Architecture & Logic Pattern Findings Report

- **Target Path**: `benchmarks/avionics_expert_system.pl`
- **Scanned Files**: `1`
- **Execution Time**: `0.0033s`
- **Total Detections**: `57`

## 📊 Category Breakdown

- **gof_behavioral**: `13`
- **gof_creational**: `7`
- **gof_structural**: `5`
- **higher_order_meta**: `4`
- **logic_constraints**: `15`
- **logic_hazards**: `11`
- **solid_principles**: `2`

## 🔍 Detected Patterns & Declarative Hazards

| # | Category | Pattern Type | Target Functor | Confidence | Location | Summary |
|---|---|---|---|:---:|---|---|
| 1 | `logic_constraints` | `definite_clause_grammar` | `waypoint_list` | **95%** | `avionics_expert_system.pl:26` | Definite Clause Grammar (Rule --> ...) for declarative syntactic parsing and difference lists. |
| 2 | `logic_constraints` | `definite_clause_grammar` | `waypoint_list` | **95%** | `avionics_expert_system.pl:27` | Definite Clause Grammar (Rule --> ...) for declarative syntactic parsing and difference lists. |
| 3 | `logic_constraints` | `definite_clause_grammar` | `waypoint` | **95%** | `avionics_expert_system.pl:29` | Definite Clause Grammar (Rule --> ...) for declarative syntactic parsing and difference lists. |
| 4 | `logic_constraints` | `clpfd_constraint_reasoning` | `CLP(FD)` | **95%** | `avionics_expert_system.pl:8` | Constraint Logic Programming over Finite Domains (#=, #>, in, labeling/2) for combinatorial search. |
| 5 | `logic_constraints` | `clpfd_constraint_reasoning` | `CLP(FD)` | **95%** | `avionics_expert_system.pl:37` | Constraint Logic Programming over Finite Domains (#=, #>, in, labeling/2) for combinatorial search. |
| 6 | `logic_constraints` | `clpfd_constraint_reasoning` | `CLP(FD)` | **95%** | `avionics_expert_system.pl:38` | Constraint Logic Programming over Finite Domains (#=, #>, in, labeling/2) for combinatorial search. |
| 7 | `logic_constraints` | `clpfd_constraint_reasoning` | `CLP(FD)` | **95%** | `avionics_expert_system.pl:39` | Constraint Logic Programming over Finite Domains (#=, #>, in, labeling/2) for combinatorial search. |
| 8 | `logic_constraints` | `clpfd_constraint_reasoning` | `CLP(FD)` | **95%** | `avionics_expert_system.pl:40` | Constraint Logic Programming over Finite Domains (#=, #>, in, labeling/2) for combinatorial search. |
| 9 | `logic_constraints` | `clpr_real_constraint_solving` | `CLP(R/Q)` | **92%** | `avionics_expert_system.pl:9` | Constraint Logic Programming over Real/Rational numbers ({Equations}) for algebraic reasoning. |
| 10 | `logic_constraints` | `clpr_real_constraint_solving` | `CLP(R/Q)` | **92%** | `avionics_expert_system.pl:43` | Constraint Logic Programming over Real/Rational numbers ({Equations}) for algebraic reasoning. |
| 11 | `logic_constraints` | `constraint_handling_rules` | `CHR` | **95%** | `avionics_expert_system.pl:10` | Committed-choice rule-based language extension (rule @ Head <=> Guard | Body) for user-defined constraint solvers. |
| 12 | `logic_constraints` | `constraint_handling_rules` | `CHR` | **95%** | `avionics_expert_system.pl:49` | Committed-choice rule-based language extension (rule @ Head <=> Guard | Body) for user-defined constraint solvers. |
| 13 | `logic_constraints` | `constraint_handling_rules` | `CHR` | **95%** | `avionics_expert_system.pl:51` | Committed-choice rule-based language extension (rule @ Head <=> Guard | Body) for user-defined constraint solvers. |
| 14 | `logic_constraints` | `constraint_handling_rules` | `CHR` | **95%** | `avionics_expert_system.pl:52` | Committed-choice rule-based language extension (rule @ Head <=> Guard | Body) for user-defined constraint solvers. |
| 15 | `logic_constraints` | `tabling_memoization_slg` | `shortest_path/3` | **95%** | `avionics_expert_system.pl:11` | SLG Resolution tabling (:- table Pred/Arity.) preventing infinite loops in cyclic graphs. |
| 16 | `higher_order_meta` | `higher_order_maplist` | `include` | **92%** | `avionics_expert_system.pl:72` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 17 | `higher_order_meta` | `higher_order_maplist` | `maplist` | **92%** | `avionics_expert_system.pl:73` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 18 | `higher_order_meta` | `higher_order_maplist` | `maplist` | **92%** | `avionics_expert_system.pl:106` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 19 | `higher_order_meta` | `all_solutions_aggregation` | `findall` | **90%** | `avionics_expert_system.pl:74` | Second-order aggregation predicates (findall/3, setof/3, bagof/3) collecting solution sets. |
| 20 | `gof_creational` | `gof_factory_method` | `create_flight_director` | **92%** | `avionics_expert_system.pl:81` | Creational pattern constructing specialized compound functor terms based on type descriptor. |
| 21 | `gof_creational` | `gof_factory_method` | `with_waypoint_builder` | **92%** | `avionics_expert_system.pl:83` | Creational pattern constructing specialized compound functor terms based on type descriptor. |
| 22 | `gof_creational` | `gof_abstract_factory` | `abstract_factory_avionics` | **92%** | `avionics_expert_system.pl:82` | Creational pattern generating families of related logical records without specifying concrete functors. |
| 23 | `gof_creational` | `gof_builder` | `with_waypoint_builder` | **90%** | `avionics_expert_system.pl:83` | Creational pattern assembling complex terms stepwise via accumulator threading or DCG grammars. |
| 24 | `gof_creational` | `gof_builder` | `with_strategy` | **90%** | `avionics_expert_system.pl:104` | Creational pattern assembling complex terms stepwise via accumulator threading or DCG grammars. |
| 25 | `gof_creational` | `gof_prototype` | `copy_term` | **90%** | `avionics_expert_system.pl:84` | Creational pattern cloning terms with fresh variable allocations via copy_term/2 or duplicate_term/2. |
| 26 | `gof_creational` | `gof_singleton` | `nb_setval` | **92%** | `avionics_expert_system.pl:85` | Creational pattern maintaining a unique dynamic database fact or global variable (nb_setval). |
| 27 | `gof_structural` | `gof_bridge` | `driver_execute_bridge` | **90%** | `avionics_expert_system.pl:89` | Structural pattern decoupling high-level logical relations from backend database/solver drivers. |
| 28 | `gof_structural` | `gof_composite` | `eval_composite_tree` | **92%** | `avionics_expert_system.pl:90` | Structural pattern composing terms into recursive tree structures (node/2, tree/3) handled uniformly. |
| 29 | `gof_structural` | `gof_decorator` | `decorate_with_timing` | **92%** | `avionics_expert_system.pl:91` | Structural pattern dynamically wrapping goal evaluation with pre/post hooks, logging, or caching. |
| 30 | `gof_structural` | `gof_flyweight` | `trie_lookup` | **90%** | `avionics_expert_system.pl:92` | Structural pattern sharing immutable atomic terms and symbol tables using trie indexing. |
| 31 | `gof_structural` | `gof_proxy` | `goal_expansion` | **90%** | `avionics_expert_system.pl:93` | Structural pattern intercepting and rewriting goals via goal_expansion/2 or term_expansion/2. |
| 32 | `gof_behavioral` | `gof_chain_of_responsibility` | `handle_failure` | **95%** | `avionics_expert_system.pl:96` | Behavioral pattern passing requests through disjunctive clause branches until one succeeds. |
| 33 | `gof_behavioral` | `gof_command` | `driver_execute_bridge` | **95%** | `avionics_expert_system.pl:89` | Behavioral pattern encapsulating an executable goal as a reified term executed via call/N or catch/3. |
| 34 | `gof_behavioral` | `gof_command` | `execute_autopilot_cmd` | **95%** | `avionics_expert_system.pl:97` | Behavioral pattern encapsulating an executable goal as a reified term executed via call/N or catch/3. |
| 35 | `gof_behavioral` | `gof_interpreter` | `eval_ast_expr` | **90%** | `avionics_expert_system.pl:98` | Behavioral pattern evaluating domain-specific grammar or AST expression trees. |
| 36 | `gof_behavioral` | `gof_iterator` | `iterator_stream` | **92%** | `avionics_expert_system.pl:99` | Behavioral pattern generating elements sequentially on backtracking (member/2, between/3). |
| 37 | `gof_behavioral` | `gof_mediator` | `mediator_blackboard_msg` | **90%** | `avionics_expert_system.pl:100` | Behavioral pattern coordinating colleague predicates through a centralized dynamic blackboard. |
| 38 | `gof_behavioral` | `gof_memento` | `snapshot_memento_state` | **90%** | `avionics_expert_system.pl:101` | Behavioral pattern recording database snapshots and transactional state checkpoints for rollback. |
| 39 | `gof_behavioral` | `gof_observer` | `subscribe_alarm_observer` | **95%** | `avionics_expert_system.pl:102` | Behavioral pattern broadcasting events to registered listener predicates or dynamic hook tables. |
| 40 | `gof_behavioral` | `gof_state` | `with_waypoint_builder` | **95%** | `avionics_expert_system.pl:83` | Behavioral pattern threading explicit state variables (State0 -> State1 -> StateN) through relations. |
| 41 | `gof_behavioral` | `gof_state` | `state_step` | **95%** | `avionics_expert_system.pl:103` | Behavioral pattern threading explicit state variables (State0 -> State1 -> StateN) through relations. |
| 42 | `gof_behavioral` | `gof_strategy` | `with_strategy` | **92%** | `avionics_expert_system.pl:104` | Behavioral pattern injecting interchangeable algorithmic goal closures into call/N or maplist/N. |
| 43 | `gof_behavioral` | `gof_template_method` | `process_pipeline_flow` | **90%** | `avionics_expert_system.pl:105` | Behavioral pattern defining skeleton relation calling customizable multifile hook predicates. |
| 44 | `gof_behavioral` | `gof_visitor` | `TermVisitor` | **92%** | `avionics_expert_system.pl:106` | Behavioral pattern traversing compound terms using univ (=..) and term_variables/2. |
| 45 | `logic_hazards` | `unsafe_cut_red_cut_hazard` | `!` | **95%** | `avionics_expert_system.pl:63` | Procedural cut (!) altering logical semantics and breaking commutativity/declarative purity. |
| 46 | `logic_hazards` | `unsafe_cut_red_cut_hazard` | `!` | **95%** | `avionics_expert_system.pl:64` | Procedural cut (!) altering logical semantics and breaking commutativity/declarative purity. |
| 47 | `logic_hazards` | `unsafe_cut_red_cut_hazard` | `!` | **95%** | `avionics_expert_system.pl:81` | Procedural cut (!) altering logical semantics and breaking commutativity/declarative purity. |
| 48 | `logic_hazards` | `unsafe_cut_red_cut_hazard` | `!` | **95%** | `avionics_expert_system.pl:113` | Procedural cut (!) altering logical semantics and breaking commutativity/declarative purity. |
| 49 | `logic_hazards` | `unsafe_term_evaluation_hazard` | `DynamicGoalExecution` | **95%** | `avionics_expert_system.pl:117` | Evaluating untrusted goal input via call/N or atom_to_term/3 risking arbitrary code execution. |
| 50 | `logic_hazards` | `unsafe_dynamic_assert_hazard` | `assertz` | **92%** | `avionics_expert_system.pl:120` | Unmanaged assertz/retract creating memory leaks and dynamic database pollution. |
| 51 | `logic_hazards` | `unsafe_io_system_hazard` | `shell` | **95%** | `avionics_expert_system.pl:123` | Executing shell commands (shell/1, process_create/3) with unsanitized atom arguments. |
| 52 | `logic_hazards` | `infinite_left_recursion_hazard` | `shortest_path` | **92%** | `avionics_expert_system.pl:61` | Direct left recursion in clause body causing infinite loops during SLD resolution. |
| 53 | `logic_hazards` | `infinite_left_recursion_hazard` | `eval_composite_tree` | **92%** | `avionics_expert_system.pl:90` | Direct left recursion in clause body causing infinite loops during SLD resolution. |
| 54 | `logic_hazards` | `infinite_left_recursion_hazard` | `eval_ast_expr` | **92%** | `avionics_expert_system.pl:98` | Direct left recursion in clause body causing infinite loops during SLD resolution. |
| 55 | `logic_hazards` | `uninstantiated_var_negation_hazard` | `UnsoundNegation` | **90%** | `avionics_expert_system.pl:126` | Calling negation (\+ or not) on uninstantiated variables producing unsound logical answers. |
| 56 | `solid_principles` | `monolithic_module_srp` | `avionics_expert_system` | **85%** | `avionics_expert_system.pl:1` | Module exports excessive predicates (>25); decompose into focused submodules. |
| 57 | `solid_principles` | `fat_predicate_arity_srp` | `fat_telemetry_predicate/10` | **85%** | `avionics_expert_system.pl:129` | Predicate declares excessive arity (>=8); refactor using compound terms or options lists. |
