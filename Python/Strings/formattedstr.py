# Formatted strings in python
first = "Jaishree"
last = "Verma"
# full = first + " " + last  -> not that good way to write
full=f"{first} {last}"     # this is better way -> f or F represents formatted string 
print(full)
full=f"{len(first)} {len(last)}"
print(full)
full=f"{first} {5+5}"
print(full)
