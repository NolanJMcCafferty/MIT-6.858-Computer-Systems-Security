import symex.fuzzy as fuzzy

def make_a_test_case():
  concrete_values = fuzzy.ConcreteValues()
  concrete_values.add('i', 861)
  return concrete_values
