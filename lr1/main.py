from random import choice, shuffle, randint
from time import time

def apply_rules_to_facts(facts, rules):
    result_facts = facts.copy()

    for rule in rules:
        conditions = rule['if']
        then_result = rule['then']

        if evaluate_conditions(conditions, result_facts):
            result_facts.append(then_result)

    return result_facts

def evaluate_conditions(conditions, facts):
    if 'or' in conditions:
        return any(item in conditions['or'] for item in facts)
    elif 'not' in conditions:
        return all(item not in conditions['not'] for item in facts)
    elif 'and' in conditions:
        return all(item in facts for item in conditions['and'])

time_start = time()

N = 100000
M = 1000

print(f"{N} правил сгенерировано за {time() - time_start} секунд")

time_start = time()

rules = [{'if': {'not': [37, 3]}, 'then': 100}, {'if': {'and': [100, 38]}, 'then': 101}, {'if': {'and': [100, 38]}, 'then': 102}]
facts = [38]

# Применяем правила к фактам
result = apply_rules_to_facts(facts, rules)

print(f"{M} фактов проверено против {N} правил за {time() - time_start} секунд")

print("Результат применения правил к фактам:")
print(result)
