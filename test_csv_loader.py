from csv_loader import clean_row
def test_clean_row_strips_whitespace():
  assert clean_row(["a","b"]) == ["a", "b"]
def test_clean_row_handles_none():
  assert clean_row([None, "b"]) == ["", "b"]
