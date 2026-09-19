def clean_row(row):
  """Strips whitespace from every value in a CSV row"""
  return[value.strip() for value in row]
def leadCSV(rows):
  return[clean_row(row) for row in rows]
