while True:
  mainSentence = input("Enter your sentence here: ").lower() # making everything lowercase
  letters = ""
  isCapital = 0 # Re-initializing variables to reset the sarcastic creator

  for letter in mainSentence:

    if letter == " ": # If there's a space in the sentence, add it back into the final sentence

      letters += " "



    elif isCapital == 0: # If it's not a space run it through the magic sentence converter

      compare = """1234567890-=[]\;',./`""" # List of all the special characters in a special order

      compare2 = """!@#$%^&*()_+{}|:"<>?~""" # List of all the shifted special characters in the same order

      count = 0 # Counting to retain which space the special character is in

      if letter in compare:

        for i in compare:

          count += 1 # Keeping track of what space the special character is in

          if letter == i:
            letter = compare2[count-1] # Changes the letter
            break

      elif letter in compare2: # Checks to see if the special character is a shifted one

        for i in compare2:

          count += 1 # Keeps track of the space

          if letter == i:
            letter = compare[count-1] # Changes the letter
            break

      letters += letter.capitalize() # Adds the letter and if it isn't a special character it capitalizes it
      isCapital += 1 # Allows it to alternate between capitalizing and not

    elif isCapital == 1: # If the last letter was changed just add this letter normally

      letters += letter # Adds letter to the sentence
      isCapital -= 1 # Allows next letter to be changed

  print(f"Here is your sarcastic sentence: {letters}")

  input("Press enter to continue.")
