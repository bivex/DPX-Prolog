# 🦉 DPX-Prolog Architecture & Logic Pattern Findings Report

- **Target Path**: `benchmarks/real_world/swi_apply.pl`
- **Scanned Files**: `4`
- **Execution Time**: `0.0202s`
- **Total Detections**: `125`

## 📊 Category Breakdown

- **gof_behavioral**: `18`
- **gof_structural**: `2`
- **higher_order_meta**: `60`
- **logic_constraints**: `13`
- **logic_hazards**: `23`
- **solid_principles**: `9`

## 🔍 Detected Patterns & Declarative Hazards

| # | Category | Pattern Type | Target Functor | Confidence | Location | Summary |
|---|---|---|---|:---:|---|---|
| 1 | `logic_constraints` | `definite_clause_grammar` | `sign` | **95%** | `dcg_basics.pl:348` | Definite Clause Grammar (Rule --> ...) for declarative syntactic parsing and difference lists. |
| 2 | `logic_constraints` | `definite_clause_grammar` | `sign` | **95%** | `dcg_basics.pl:349` | Definite Clause Grammar (Rule --> ...) for declarative syntactic parsing and difference lists. |
| 3 | `logic_constraints` | `definite_clause_grammar` | `dot` | **95%** | `dcg_basics.pl:351` | Definite Clause Grammar (Rule --> ...) for declarative syntactic parsing and difference lists. |
| 4 | `logic_constraints` | `definite_clause_grammar` | `exp` | **95%** | `dcg_basics.pl:353` | Definite Clause Grammar (Rule --> ...) for declarative syntactic parsing and difference lists. |
| 5 | `logic_constraints` | `definite_clause_grammar` | `exp` | **95%** | `dcg_basics.pl:354` | Definite Clause Grammar (Rule --> ...) for declarative syntactic parsing and difference lists. |
| 6 | `logic_constraints` | `definite_clause_grammar` | `eol` | **95%** | `dcg_basics.pl:430` | Definite Clause Grammar (Rule --> ...) for declarative syntactic parsing and difference lists. |
| 7 | `logic_constraints` | `definite_clause_grammar` | `eol` | **95%** | `dcg_basics.pl:431` | Definite Clause Grammar (Rule --> ...) for declarative syntactic parsing and difference lists. |
| 8 | `logic_constraints` | `definite_clause_grammar` | `eol` | **95%** | `dcg_basics.pl:432` | Definite Clause Grammar (Rule --> ...) for declarative syntactic parsing and difference lists. |
| 9 | `logic_constraints` | `definite_clause_grammar` | `prolog_id_cont` | **95%** | `dcg_basics.pl:475` | Definite Clause Grammar (Rule --> ...) for declarative syntactic parsing and difference lists. |
| 10 | `logic_constraints` | `clpr_real_constraint_solving` | `CLP(R/Q)` | **92%** | `dcg_basics.pl:334` | Constraint Logic Programming over Real/Rational numbers ({Equations}) for algebraic reasoning. |
| 11 | `logic_constraints` | `clpr_real_constraint_solving` | `CLP(R/Q)` | **92%** | `dcg_basics.pl:335` | Constraint Logic Programming over Real/Rational numbers ({Equations}) for algebraic reasoning. |
| 12 | `logic_constraints` | `clpr_real_constraint_solving` | `CLP(R/Q)` | **92%** | `dcg_basics.pl:339` | Constraint Logic Programming over Real/Rational numbers ({Equations}) for algebraic reasoning. |
| 13 | `logic_constraints` | `clpr_real_constraint_solving` | `CLP(R/Q)` | **92%** | `dcg_basics.pl:340` | Constraint Logic Programming over Real/Rational numbers ({Equations}) for algebraic reasoning. |
| 14 | `higher_order_meta` | `higher_order_maplist` | `maplist` | **92%** | `swi_apply.pl:70` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 15 | `higher_order_meta` | `higher_order_maplist` | `maplist` | **92%** | `swi_apply.pl:71` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 16 | `higher_order_meta` | `higher_order_maplist` | `include` | **92%** | `swi_apply.pl:82` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 17 | `higher_order_meta` | `higher_order_maplist` | `exclude` | **92%** | `swi_apply.pl:83` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 18 | `higher_order_meta` | `higher_order_maplist` | `partition` | **92%** | `swi_apply.pl:84` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 19 | `higher_order_meta` | `higher_order_maplist` | `partition` | **92%** | `swi_apply.pl:85` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 20 | `higher_order_meta` | `higher_order_maplist` | `maplist` | **92%** | `swi_apply.pl:86` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 21 | `higher_order_meta` | `higher_order_maplist` | `maplist` | **92%** | `swi_apply.pl:87` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 22 | `higher_order_meta` | `higher_order_maplist` | `maplist` | **92%** | `swi_apply.pl:88` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 23 | `higher_order_meta` | `higher_order_maplist` | `maplist` | **92%** | `swi_apply.pl:89` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 24 | `higher_order_meta` | `higher_order_maplist` | `convlist` | **92%** | `swi_apply.pl:90` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 25 | `higher_order_meta` | `higher_order_maplist` | `foldl` | **92%** | `swi_apply.pl:91` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 26 | `higher_order_meta` | `higher_order_maplist` | `foldl` | **92%** | `swi_apply.pl:92` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 27 | `higher_order_meta` | `higher_order_maplist` | `foldl` | **92%** | `swi_apply.pl:93` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 28 | `higher_order_meta` | `higher_order_maplist` | `foldl` | **92%** | `swi_apply.pl:94` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 29 | `higher_order_meta` | `higher_order_maplist` | `include` | **92%** | `swi_apply.pl:110` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 30 | `higher_order_meta` | `higher_order_maplist` | `include` | **92%** | `swi_apply.pl:111` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 31 | `higher_order_meta` | `higher_order_maplist` | `include` | **92%** | `swi_apply.pl:116` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 32 | `higher_order_meta` | `higher_order_maplist` | `exclude` | **92%** | `swi_apply.pl:126` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 33 | `higher_order_meta` | `higher_order_maplist` | `exclude` | **92%** | `swi_apply.pl:127` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 34 | `higher_order_meta` | `higher_order_maplist` | `exclude` | **92%** | `swi_apply.pl:132` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 35 | `higher_order_meta` | `higher_order_maplist` | `partition` | **92%** | `swi_apply.pl:143` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 36 | `higher_order_meta` | `higher_order_maplist` | `partition` | **92%** | `swi_apply.pl:144` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 37 | `higher_order_meta` | `higher_order_maplist` | `partition` | **92%** | `swi_apply.pl:147` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 38 | `higher_order_meta` | `higher_order_maplist` | `partition` | **92%** | `swi_apply.pl:149` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 39 | `higher_order_meta` | `higher_order_maplist` | `partition` | **92%** | `swi_apply.pl:162` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 40 | `higher_order_meta` | `higher_order_maplist` | `partition` | **92%** | `swi_apply.pl:163` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 41 | `higher_order_meta` | `higher_order_maplist` | `partition` | **92%** | `swi_apply.pl:170` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 42 | `higher_order_meta` | `higher_order_maplist` | `partition` | **92%** | `swi_apply.pl:174` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 43 | `higher_order_meta` | `higher_order_maplist` | `partition` | **92%** | `swi_apply.pl:178` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 44 | `higher_order_meta` | `higher_order_maplist` | `maplist` | **92%** | `swi_apply.pl:209` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 45 | `higher_order_meta` | `higher_order_maplist` | `maplist` | **92%** | `swi_apply.pl:210` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 46 | `higher_order_meta` | `higher_order_maplist` | `maplist` | **92%** | `swi_apply.pl:212` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 47 | `higher_order_meta` | `higher_order_maplist` | `maplist` | **92%** | `swi_apply.pl:214` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 48 | `higher_order_meta` | `higher_order_maplist` | `maplist` | **92%** | `swi_apply.pl:215` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 49 | `higher_order_meta` | `higher_order_maplist` | `maplist` | **92%** | `swi_apply.pl:217` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 50 | `higher_order_meta` | `higher_order_maplist` | `maplist` | **92%** | `swi_apply.pl:219` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 51 | `higher_order_meta` | `higher_order_maplist` | `maplist` | **92%** | `swi_apply.pl:220` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 52 | `higher_order_meta` | `higher_order_maplist` | `maplist` | **92%** | `swi_apply.pl:222` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 53 | `higher_order_meta` | `higher_order_maplist` | `maplist` | **92%** | `swi_apply.pl:224` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 54 | `higher_order_meta` | `higher_order_maplist` | `maplist` | **92%** | `swi_apply.pl:225` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 55 | `higher_order_meta` | `higher_order_maplist` | `maplist` | **92%** | `swi_apply.pl:227` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 56 | `higher_order_meta` | `higher_order_maplist` | `convlist` | **92%** | `swi_apply.pl:244` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 57 | `higher_order_meta` | `higher_order_maplist` | `convlist` | **92%** | `swi_apply.pl:245` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 58 | `higher_order_meta` | `higher_order_maplist` | `convlist` | **92%** | `swi_apply.pl:248` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 59 | `higher_order_meta` | `higher_order_maplist` | `convlist` | **92%** | `swi_apply.pl:249` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 60 | `higher_order_meta` | `higher_order_maplist` | `foldl` | **92%** | `swi_apply.pl:285` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 61 | `higher_order_meta` | `higher_order_maplist` | `foldl` | **92%** | `swi_apply.pl:286` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 62 | `higher_order_meta` | `higher_order_maplist` | `foldl` | **92%** | `swi_apply.pl:288` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 63 | `higher_order_meta` | `higher_order_maplist` | `foldl` | **92%** | `swi_apply.pl:291` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 64 | `higher_order_meta` | `higher_order_maplist` | `foldl` | **92%** | `swi_apply.pl:292` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 65 | `higher_order_meta` | `higher_order_maplist` | `foldl` | **92%** | `swi_apply.pl:294` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 66 | `higher_order_meta` | `higher_order_maplist` | `foldl` | **92%** | `swi_apply.pl:297` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 67 | `higher_order_meta` | `higher_order_maplist` | `foldl` | **92%** | `swi_apply.pl:298` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 68 | `higher_order_meta` | `higher_order_maplist` | `foldl` | **92%** | `swi_apply.pl:300` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 69 | `higher_order_meta` | `higher_order_maplist` | `foldl` | **92%** | `swi_apply.pl:303` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 70 | `higher_order_meta` | `higher_order_maplist` | `foldl` | **92%** | `swi_apply.pl:304` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 71 | `higher_order_meta` | `higher_order_maplist` | `foldl` | **92%** | `swi_apply.pl:306` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 72 | `higher_order_meta` | `higher_order_maplist` | `maplist` | **92%** | `swi_apply.pl:373` | Declarative higher-order list processing using maplist/N, include/3, exclude/3, or foldl/4. |
| 73 | `higher_order_meta` | `all_solutions_aggregation` | `aggregate_all` | **90%** | `swi_persistency.pl:428` | Second-order aggregation predicates (findall/3, setof/3, bagof/3) collecting solution sets. |
| 74 | `gof_structural` | `gof_proxy` | `term_expansion` | **90%** | `swi_apply.pl:371` | Structural pattern intercepting and rewriting goals via goal_expansion/2 or term_expansion/2. |
| 75 | `gof_structural` | `gof_proxy` | `term_expansion` | **90%** | `swi_persistency.pl:272` | Structural pattern intercepting and rewriting goals via goal_expansion/2 or term_expansion/2. |
| 76 | `gof_behavioral` | `gof_state` | `foldl` | **95%** | `swi_apply.pl:286` | Behavioral pattern threading explicit state variables (State0 -> State1 -> StateN) through relations. |
| 77 | `gof_behavioral` | `gof_state` | `foldl` | **95%** | `swi_apply.pl:292` | Behavioral pattern threading explicit state variables (State0 -> State1 -> StateN) through relations. |
| 78 | `gof_behavioral` | `gof_state` | `foldl` | **95%** | `swi_apply.pl:298` | Behavioral pattern threading explicit state variables (State0 -> State1 -> StateN) through relations. |
| 79 | `gof_behavioral` | `gof_state` | `foldl` | **95%** | `swi_apply.pl:304` | Behavioral pattern threading explicit state variables (State0 -> State1 -> StateN) through relations. |
| 80 | `gof_behavioral` | `gof_state` | `get_option` | **95%** | `swi_option.pl:175` | Behavioral pattern threading explicit state variables (State0 -> State1 -> StateN) through relations. |
| 81 | `gof_behavioral` | `gof_state` | `get_option` | **95%** | `swi_option.pl:178` | Behavioral pattern threading explicit state variables (State0 -> State1 -> StateN) through relations. |
| 82 | `gof_behavioral` | `gof_state` | `mkval` | **95%** | `dcg_basics.pl:417` | Behavioral pattern threading explicit state variables (State0 -> State1 -> StateN) through relations. |
| 83 | `gof_behavioral` | `gof_visitor` | `TermVisitor` | **92%** | `swi_option.pl:295` | Behavioral pattern traversing compound terms using univ (=..) and term_variables/2. |
| 84 | `gof_behavioral` | `gof_visitor` | `TermVisitor` | **92%** | `swi_option.pl:298` | Behavioral pattern traversing compound terms using univ (=..) and term_variables/2. |
| 85 | `gof_behavioral` | `gof_visitor` | `TermVisitor` | **92%** | `swi_option.pl:344` | Behavioral pattern traversing compound terms using univ (=..) and term_variables/2. |
| 86 | `gof_behavioral` | `gof_visitor` | `TermVisitor` | **92%** | `swi_option.pl:348` | Behavioral pattern traversing compound terms using univ (=..) and term_variables/2. |
| 87 | `gof_behavioral` | `gof_visitor` | `TermVisitor` | **92%** | `swi_persistency.pl:221` | Behavioral pattern traversing compound terms using univ (=..) and term_variables/2. |
| 88 | `gof_behavioral` | `gof_visitor` | `TermVisitor` | **92%** | `swi_persistency.pl:222` | Behavioral pattern traversing compound terms using univ (=..) and term_variables/2. |
| 89 | `gof_behavioral` | `gof_visitor` | `TermVisitor` | **92%** | `swi_persistency.pl:225` | Behavioral pattern traversing compound terms using univ (=..) and term_variables/2. |
| 90 | `gof_behavioral` | `gof_visitor` | `TermVisitor` | **92%** | `swi_persistency.pl:247` | Behavioral pattern traversing compound terms using univ (=..) and term_variables/2. |
| 91 | `gof_behavioral` | `gof_visitor` | `TermVisitor` | **92%** | `swi_persistency.pl:248` | Behavioral pattern traversing compound terms using univ (=..) and term_variables/2. |
| 92 | `gof_behavioral` | `gof_visitor` | `TermVisitor` | **92%** | `swi_persistency.pl:258` | Behavioral pattern traversing compound terms using univ (=..) and term_variables/2. |
| 93 | `gof_behavioral` | `gof_visitor` | `TermVisitor` | **92%** | `swi_persistency.pl:259` | Behavioral pattern traversing compound terms using univ (=..) and term_variables/2. |
| 94 | `logic_hazards` | `unsafe_cut_red_cut_hazard` | `!` | **95%** | `swi_option.pl:245` | Procedural cut (!) altering logical semantics and breaking commutativity/declarative purity. |
| 95 | `logic_hazards` | `unsafe_cut_red_cut_hazard` | `!` | **95%** | `swi_option.pl:246` | Procedural cut (!) altering logical semantics and breaking commutativity/declarative purity. |
| 96 | `logic_hazards` | `unsafe_cut_red_cut_hazard` | `!` | **95%** | `swi_persistency.pl:265` | Procedural cut (!) altering logical semantics and breaking commutativity/declarative purity. |
| 97 | `logic_hazards` | `unsafe_cut_red_cut_hazard` | `!` | **95%** | `swi_persistency.pl:381` | Procedural cut (!) altering logical semantics and breaking commutativity/declarative purity. |
| 98 | `logic_hazards` | `unsafe_cut_red_cut_hazard` | `!` | **95%** | `swi_persistency.pl:576` | Procedural cut (!) altering logical semantics and breaking commutativity/declarative purity. |
| 99 | `logic_hazards` | `unsafe_cut_red_cut_hazard` | `!` | **95%** | `swi_persistency.pl:691` | Procedural cut (!) altering logical semantics and breaking commutativity/declarative purity. |
| 100 | `logic_hazards` | `unsafe_dynamic_assert_hazard` | `assert` | **92%** | `swi_persistency.pl:323` | Unmanaged assertz/retract creating memory leaks and dynamic database pollution. |
| 101 | `logic_hazards` | `unsafe_dynamic_assert_hazard` | `assert` | **92%** | `swi_persistency.pl:340` | Unmanaged assertz/retract creating memory leaks and dynamic database pollution. |
| 102 | `logic_hazards` | `unsafe_dynamic_assert_hazard` | `assert` | **92%** | `swi_persistency.pl:352` | Unmanaged assertz/retract creating memory leaks and dynamic database pollution. |
| 103 | `logic_hazards` | `unsafe_dynamic_assert_hazard` | `assert` | **92%** | `swi_persistency.pl:369` | Unmanaged assertz/retract creating memory leaks and dynamic database pollution. |
| 104 | `logic_hazards` | `unsafe_dynamic_assert_hazard` | `assert` | **92%** | `swi_persistency.pl:382` | Unmanaged assertz/retract creating memory leaks and dynamic database pollution. |
| 105 | `logic_hazards` | `unsafe_dynamic_assert_hazard` | `assert` | **92%** | `swi_persistency.pl:385` | Unmanaged assertz/retract creating memory leaks and dynamic database pollution. |
| 106 | `logic_hazards` | `unsafe_dynamic_assert_hazard` | `asserta` | **92%** | `swi_persistency.pl:388` | Unmanaged assertz/retract creating memory leaks and dynamic database pollution. |
| 107 | `logic_hazards` | `unsafe_dynamic_assert_hazard` | `asserta` | **92%** | `swi_persistency.pl:391` | Unmanaged assertz/retract creating memory leaks and dynamic database pollution. |
| 108 | `logic_hazards` | `unsafe_dynamic_assert_hazard` | `assert` | **92%** | `swi_persistency.pl:459` | Unmanaged assertz/retract creating memory leaks and dynamic database pollution. |
| 109 | `logic_hazards` | `unsafe_dynamic_assert_hazard` | `assert` | **92%** | `swi_persistency.pl:460` | Unmanaged assertz/retract creating memory leaks and dynamic database pollution. |
| 110 | `logic_hazards` | `unsafe_dynamic_assert_hazard` | `asserta` | **92%** | `swi_persistency.pl:463` | Unmanaged assertz/retract creating memory leaks and dynamic database pollution. |
| 111 | `logic_hazards` | `unsafe_dynamic_assert_hazard` | `asserta` | **92%** | `swi_persistency.pl:464` | Unmanaged assertz/retract creating memory leaks and dynamic database pollution. |
| 112 | `logic_hazards` | `unsafe_dynamic_assert_hazard` | `assert` | **92%** | `swi_persistency.pl:472` | Unmanaged assertz/retract creating memory leaks and dynamic database pollution. |
| 113 | `logic_hazards` | `unsafe_dynamic_assert_hazard` | `assert` | **92%** | `swi_persistency.pl:583` | Unmanaged assertz/retract creating memory leaks and dynamic database pollution. |
| 114 | `logic_hazards` | `unsafe_dynamic_assert_hazard` | `assert` | **92%** | `swi_persistency.pl:659` | Unmanaged assertz/retract creating memory leaks and dynamic database pollution. |
| 115 | `logic_hazards` | `unsafe_dynamic_assert_hazard` | `assert` | **92%** | `swi_persistency.pl:670` | Unmanaged assertz/retract creating memory leaks and dynamic database pollution. |
| 116 | `logic_hazards` | `unsafe_dynamic_assert_hazard` | `assert` | **92%** | `swi_persistency.pl:680` | Unmanaged assertz/retract creating memory leaks and dynamic database pollution. |
| 117 | `solid_principles` | `monolithic_module_srp` | `apply` | **85%** | `swi_apply.pl:37` | Module exports excessive predicates (>25); decompose into focused submodules. |
| 118 | `solid_principles` | `monolithic_module_srp` | `swi_option` | **85%** | `swi_option.pl:38` | Module exports excessive predicates (>25); decompose into focused submodules. |
| 119 | `solid_principles` | `monolithic_module_srp` | `dcg_basics` | **85%** | `dcg_basics.pl:37` | Module exports excessive predicates (>25); decompose into focused submodules. |
| 120 | `solid_principles` | `monolithic_module_srp` | `user_db` | **85%** | `swi_persistency.pl:96` | Module exports excessive predicates (>25); decompose into focused submodules. |
| 121 | `solid_principles` | `fat_predicate_arity_srp` | `ord_merge/8` | **85%** | `swi_option.pl:252` | Predicate declares excessive arity (>=8); refactor using compound terms or options lists. |
| 122 | `solid_principles` | `impure_state_mutation_srp` | `set_user_role/2` | **88%** | `swi_persistency.pl:117` | Mixing pure logical deduction with assertz/retract side-effects inside relations. |
| 123 | `solid_principles` | `impure_state_mutation_srp` | `compile_persistent/3` | **88%** | `swi_persistency.pl:190` | Mixing pure logical deduction with assertz/retract side-effects inside relations. |
| 124 | `solid_principles` | `impure_state_mutation_srp` | `set_dirty/2` | **88%** | `swi_persistency.pl:574` | Mixing pure logical deduction with assertz/retract side-effects inside relations. |
| 125 | `solid_principles` | `impure_state_mutation_srp` | `db_sync/2` | **88%** | `swi_persistency.pl:618` | Mixing pure logical deduction with assertz/retract side-effects inside relations. |
