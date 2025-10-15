# --- Knowledge Base ---
facts = {("Sachin", "Batsman")} # Sachin is a Batsman
rules = [("Batsman", "Cricketer")] # If x is a Batsman -> x is a Cricketer
def infer_predicates(facts, rules):
    derived = set(facts)
    changed = True
    while changed:
        changed = False
        for (entity, pred) in list(derived):
            for (cond, result) in rules:
                if pred == cond and (entity, result) not in derived:
                    derived.add((entity, result))
                    changed = True
    return derived

# --- Run inference ---
derived_facts = infer_predicates(facts, rules)
# --- Show Results --
print("Derived Knowledge:")
for entity, predicate in derived_facts:
    print(f"{entity} is a {predicate}")
