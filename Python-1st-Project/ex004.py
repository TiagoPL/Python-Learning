Answer = input('Type something: ')
print(f'''What you typed is::
      Numeric? {Answer.isnumeric()}
      Alphabetic? {Answer.isalpha()}
      Alphanumeric? {Answer.isalnum()}
      Uppercase only? {Answer.isupper()}
      Lowercase only? {Answer.islower()}
      Blank Spaces only? {Answer.isspace()}
      Capitalized? {Answer.istitle()}''')
