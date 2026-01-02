from alchemy.trasmutation.basic import lead_to_gold, stone_to_gem
from alchemy.trasmutation.advanced import philosophers_stone, elixir_of_life
import alchemy

print("Testing Absolute Imports (from basic.py):")
print(f"lead_to_gold(): {lead_to_gold()}")
print(f"stone_to_gem(): {stone_to_gem()}\n")

print("Testing Relative Imports (from advanced.py):")
print(f"philosophers_stone(): {philosophers_stone()}")
print(f"elixir_of_life(): {elixir_of_life()}")

print("Testing Package Access:")
print(f"alchemy.transmutation.lead_to_gold():"
      f" {alchemy.trasmutation.lead_to_gold()}")
print(f"alchemy.transmutation.philosophers_stone()"
      f": {alchemy.trasmutation.lead_to_gold()}\n")
print("Both pathways work! Absolute: clear, Relative: concise")
