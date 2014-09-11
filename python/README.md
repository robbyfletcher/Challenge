# Python Solution

First off, I really enjoyed this challenge. It really made me think 
creatively about how to determine if to words are friends.

So the first thing I thought about, after I imported the word list 
into an array, was where to start on deciding if words were friends
or not. Firstly, for two words to friends, their length would have 
to be within one of each other. So first I decided to focus on 
words with the same length. 

## Words with same length
If two words have the same length, determining whether or not they 
are friends becomes fairly easy. No letters are being added or 
subtracted, only replaced. So if you check letter by letter for 
equality, the difference should only be one. Anything higher and 
the Levenshtein distance is more than one.

## Words with lengths off by one
This is somewhat more tricky than before. In order for words to have
distances off by one, two things can be happening: a letter could
have been deleted, or a letter could have been added. However, if you
look at this operations, they are essentially the same, it just depends
on which of the words you are looking at. If you are looking at the 
shorter word, it will always look like an addition; If you are looking 
at the longer word, it will always look like a subtraction. So the 
first step here would be to determine which word is longer, and which
words is shorter. Once you have determined that, you can start by doing 
a modified version of what we did to words of the same length: checking
letter by letter. However, when you come to a difference, the key is to
increment to longer word forward by one letter. For example, if letter 
'i' in the shorter word is the first difference, check letter 'i' in 
the shorter word by letter 'i+1' in the longer word, and continue 
through the rest of the word. Basically, the first difference is what we
will assume to be the added letter, and the rest of the letters must be 
the same in order for them to be friends.

## Notes
While working on this project, I noticed that there were some duplicates
in the list, and that initially my algorithm would return itself, and 
words more than once. So I added in some code to check for duplicates
and copies of the original word, because in an actual social network, 
a person wouldn't be friends with themselves, nor the same person twice.
I also noticed some words contained upper-case letters, so upon checking 
the words, I converted them all to lower-case to make it case-insensitive.

Also, the algorithm I used in python is the same algorithm I used for 
the javascript code.
