def validate_ingredients(ingredients: str) -> str:
    valid_condition = ["fire", "water", "earth", "air"]

    for element in valid_condition:
        if element in ingredients:
            return f"{element} - VALID"

    return f"{ingredients} - INVALID"