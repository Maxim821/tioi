from random import choice, shuffle, randint
from time import time


def generate_simple_rules(code_max, n_max, n_generate, log_oper_choice=["and", "or", "not"]):
    """
    Генерирует список правил с простыми условиями, где каждое условие
    содержит логическую операцию (and, or, not) и список случайных элементов.
    """
    rules = []
    for j in range(0, n_generate):

        log_oper = choice(log_oper_choice)  # not means and-not (neither)
        if n_max < 2:
            n_max = 2
        n_items = randint(2, n_max)
        items = []
        for i in range(0, n_items):
            items.append(randint(1, code_max))
        rule = {
            'if': {
                log_oper: items
            },
            'then': code_max + j
        }
        rules.append(rule)
    shuffle(rules)
    return (rules)


# print(generate_simple_rules(100, 4, 1000))


def generate_stairway_rules(code_max, n_max, n_generate, log_oper_choice=["and", "or", "not"]):
    """
    Генерирует список правил, где каждое правило содержит условия,
    идущие "лестницей" (последовательно увеличивающимися числами).
    """
    rules = []
    for j in range(0, n_generate):

        log_oper = choice(log_oper_choice)  # not means and-not (neither)
        if n_max < 2:
            n_max = 2
        n_items = randint(2, n_max)
        items = []
        for i in range(0, n_items):
            items.append(i + j)
        rule = {
            'if': {
                log_oper: items
            },
            'then': i + j + 1
        }
        rules.append(rule)
    shuffle(rules)
    return (rules)


# print(generate_stairway_rules(100, 4, 1, ["or"]))


def generate_ring_rules(code_max, n_max, n_generate, log_oper_choice=["and", "or", "not"]):
    """
    Генерирует правила похожим на generate_stairway_rules способом,
    но добавляет еще одно правило, создающее "кольцо" -
    связывающее начало и конец последовательности.
    """
    rules = generate_stairway_rules(code_max, n_max, n_generate - 1, log_oper_choice)
    log_oper = choice(log_oper_choice)  # not means and-not (neither)
    if n_max < 2:
        n_max = 2
    n_items = randint(2, n_max)
    items = []
    for i in range(0, n_items):
        items.append(code_max - i)
    rule = {
        'if': {
            log_oper: items
        },
        'then': 0
    }
    rules.append(rule)
    shuffle(rules)
    return (rules)


# print(generate_ring_rules(100, 4, 10, ["or"]))


def generate_random_rules(code_max, n_max, n_generate, log_oper_choice=["and", "or", "not"]):
    """
    Генерирует список случайных правил с случайными условиями и случайными результатами.
    """
    rules = []
    for j in range(0, n_generate):

        log_oper = choice(log_oper_choice)  # not means and-not (neither)
        if n_max < 2:
            n_max = 2
        n_items = randint(2, n_max)
        items = []
        for i in range(0, n_items):
            items.append(randint(1, code_max))
        rule = {
            'if': {
                log_oper: items
            },
            'then': randint(1, code_max)
        }
        rules.append(rule)
    shuffle(rules)
    return (rules)


# print(generate_random_rules(100, 4, 10))


def generate_seq_facts(M):
    facts = list(range(0, M))
    shuffle(facts)
    return facts


# print(generate_seq_facts(10))


def generate_rand_facts(code_max, M):
    facts = []
    for i in range(0, M):
        facts.append(randint(0, code_max))
    return facts


# print(generate_rand_facts(10, 15))


def apply_rules_to_facts(facts, rules, result_facts=None):
    if result_facts is None:
        result_facts = []

    if not rules:
        return facts + result_facts

    rule = rules[0]
    conditions = rule['if']
    then_result = rule['then']

    if evaluate_conditions(conditions, facts):  # Передаем весь массив фактов
        result_facts.append(then_result)

    return apply_rules_to_facts(facts, rules[1:], result_facts)


def evaluate_conditions(conditions, facts):  # Теперь принимает весь массив фактов
    if 'or' in conditions:
        # Проверяем условие для каждого факта в массиве
        # print(f"Оценка 'or' для фактов {facts}")
        # print(f"Ответ: {any(item in conditions['or'] for item in facts)}")
        return any(item in conditions['or'] for item in facts)
    elif 'not' in conditions:
        # print(f"Оценка 'not' для фактов {facts}")
        # print(f"Ответ: {all(item not in conditions['not'] for item in facts)}")
        return all(item not in conditions['not'] for item in facts)
    elif 'and' in conditions:
        # Проверяем, что все элементы из условия содержатся в массиве фактов
        # print(f"Оценка 'and' для фактов {facts}")
        # print(f"Ответ: {all(item in facts for item in conditions['and'])}")
        return all(item in facts for item in conditions['and'])


# print(generate_rand_facts(10, 3))

"""
"правила" представляют собой логические высказывания, 
определяющие условия и результаты, а "факты" представляют собой информацию, 
которая может быть проверена на соответствие этим правилам.
"""

# # samples:
# print(generate_simple_rules(100, 4, 10))
# print(generate_random_rules(100, 4, 10))
# print(generate_stairway_rules(100, 4, 10, ["or"]))
# print(generate_ring_rules(100, 4, 10, ["or"]))
#
# generate rules and facts and check time
time_start = time()
N = 100000
M = 1000
#rules = generate_simple_rules(100, 4, N)
#facts = generate_rand_facts(100, M)
# print(f"rules {rules}")
# print(f"facts {facts}")
print(f"{N} rules generated in {time() - time_start} seconds")
#
# time_start = time()
#
rules = [{'if': {'and': [37, 38]}, 'then': 100}]
facts = [97, 23, 97, 86, 37, 38, 50, 51, 13, 75]

# Применяем правила к фактам
result = apply_rules_to_facts(facts, rules)

print(f"{M} facts validated vs {N} rules in {time() - time_start} seconds")

print("Результат применения правил к фактам:")
print(result)
