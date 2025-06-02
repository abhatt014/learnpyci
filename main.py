# main.py
def to_uppercase(text):
  """Converts a string to uppercase."""
  return text.upper()

if __name__ == "__main__":
  input_string = "Welcome to devops"
  uppercased_string = to_uppercase(input_string)
  print(f"Original: {input_string}")
  print(f"Uppercase: {uppercased_string}")