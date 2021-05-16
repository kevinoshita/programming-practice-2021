def exercise_3(inputs): # DO NOT CHANGE THIS LINE
    input_history = []

    def get_input(input_prompt):
        string_input = input(input_prompt)
        input_history.append(string_input)
        return string_input

    def get_second_letter(word):
        if len(word) < 2:
            return word
        else:
            return word[1]

    def sort_by_second_letter():
        words = input_history[-1].split()
        words.sort(key = get_second_letter)

        print("List of all words ordered by the second letter from the left: ")
        for i in range(len(words)):
            print(words[i])

        print()

    def return_previous_input():
        if len(input_history) == 0:
            print("History does not have input.")
        else:
            input_history.pop()
            print(input_history[-1])

    def get_string_info():
        sentences = input_history[-1].split('. ')
        words = input_history[-1].split(' ')
        for i in range(len(sentences)):
            if sentences[i] == '':
                sentences.pop(i)
        for i in range(len(words)):
            if words[i] == '':
                words.pop(i)
        print("The amount of sentence in input is {}.".format(len(sentences)))
        print("The amount of words in input is {}.".format(len(words)))
        print()

    def find_short_words():
        words = input_history[-1].split(' ')
        print("List of words that are less than 5 letters:")
        for i in  range(len(words)):
            if len(words[i]) < 5:
                print(words[i])
        print()
        words_without_vowels = []
        vowels = ('a', 'e', 'i', 'o', 'u')
        for word in words:
            for letter in word.lower():
                if letter in vowels:
                    word = word.replace(letter, "")
            words_without_vowels.append(word)

        print(words_without_vowels)

        print("Words that have less than 5 letters, not including vowels:")
        for i in range(len(words)):
            if len(words_without_vowels[i]) < 5:
                print(words[i])
        print()
    
    
    
    
    
    
    
    
    import practice3library

    input_from_user = ""

    while input_from_user != "exit":
        input_from_user = practice3library.get_input("Please enter a sentence. To exit, input 'exit': ")
        if input_from_user == "previous":
            practice3library.return_previous_input()
        elif input_from_user == "exit":
            break
        practice3library.sort_by_second_letter()
        practice3library.get_string_info()
        practice3library.find_short_words()
        print(practice3library.input_history)
    
    
    output = inputs

    return output       # DO NOT CHANGE THIS LINE
