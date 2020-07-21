# Get multi-line input from terminal
print('Paste your deck list: ')
deck_list = []
while True:
    line = input()
    if line:
        # Handle special lines
        if 'Deck' in line:
            line = 'main'
            deck_list.append(line)
        # Line contains card info
        else:
            # Strip the collection number from the end (since Forge currently doesn't support importing those correctly)
            last_paren_index = line.rfind(')')
            if last_paren_index != -1:
                line = line[:last_paren_index+1]
            # Replace parentheses with pipes
            line = line.replace(')','|')
            line = line.replace(' (','|')
            deck_list.append(line)
    else:
        break

# Convert list into string
deck_string = '\n'.join(deck_list)
print(deck_string)