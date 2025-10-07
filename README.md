# Python Review 4 

Python File handling
https://drive.google.com/file/d/1sIv9rb6PizW9sfts9eVu0BkLYWLjysiT/view

---

## Exercise 1

**Problem:**

Input n numbers as list and write each number to a file called numbers.txt, one number per line.

**Example:**

    Example Input:
        [10,20,30,40,50]
    
    File Output (numbers.txt):
        10
        20
        30
        40
        50


---

## Exercise 2

**Problem:**

Read numbers from the file numbers.txt.
Calculate and print the sum of all numbers.

**Example:**

    Example File Content (numbers.txt):
        10
        20
        30
        40
        50
    
    Program Output:
        150

---

## Exercise 3

**Problem:**

Create a text file data.txt with some text.
Count and print the number of lines and the total number of words in the file.

**Example**

    Example File Content (data.txt):
        Python is fun.
        It helps you learn programming.
        File handling is important.

    Program Output:
        3,12   # lines = 3 words = 12

---

## Exercise 4

**Problem:**

Write a program that reads a file and prints the longest word.

**Example**

    Example File Content (data.txt):
        What's the longest word in here?
    
    Program Output:
         "longest"

    
---

## Exercise 5 (Optional)

**Problem:**

Word Guessing Game (like Hangman)

-Store a list of words in a file called words.txt.
-The program randomly picks a word from the file.
-The user guesses letters until they find the word (limit wrong guesses to 6).
-Save the game result (win or lose) to results.txt.

**Example**

    Example 1:
    Word Guessing Game!
    The word has 7 letters: _ _ _ _ _ _
    
    Guess a letter: y
    Good guess! _ y _ _ _ _
    
    Guess a letter: e
    Wrong guess! 5 tries left.
    
    Guess a letter: p
    Good guess! p y _ _ _ _ 
    
    ...
    
    Congratulations! You guessed the word: "python"
    Game result saved to results.txt

    Example 2:
    Word Guessing Game!
    The word has 6 letters: _ _ _ _ _ _
    
    Guess a letter: z
    Wrong guess! 5 tries left.
    
    ...
    
    Sorry, you lost! The word was: "school"
    Game result saved to results.txt

---

