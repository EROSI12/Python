from typing import Optional, List, Union, Any

# Optional Example
def get_name(name: Optional[str] = None) -> str:
    if name:
        return name
    return "Anonymous"

print(get_name())

# Union Example
def process_value(value: Union[int, str]) -> str:
    if isinstance(value, int):
        return f"Number: {value}"
    return f"String: {value}"

print(process_value("Digital School"))

# Any Example
def process_anything(value: Any) -> str:
    return f"Processed {value}"

print(process_anything([1, 2, 3]))

# List and Sum Function
def sum_list(numbers: List[int]) -> int:
    return sum(numbers)

numbers: List[int] = [1, 2, 3]
result: int = sum_list(numbers)
print(result)
