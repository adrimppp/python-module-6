def record_spell(spell_name: str, ingredients: str):
    from .validator import validate_ingredients
    valid_result = validate_ingredients(ingredients)
    if "INVALID" in valid_result:
        return f"Spell rejected: {spell_name} {valid_result}"
    else:
        return f"Spell recorded: {spell_name} {valid_result}"
