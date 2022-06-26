ANDERSON'S FAIRY TALES CONTENT WORDS EXTRACTION

Extract content words from 18 Anderson's Fairy Tales and compare similarity between any two of them


1. Introduction

People love fairy tales, there is stereotype that fairy tales are always about fortune, happy ending
and other positive stuff.

This program lets you find out how the content words evolve from the beginning, the middle, then to
the end of a story. Hopefully, this will lead to prove why the "happy ending".

You will also see the most frequent content words of a certain type within a story. Lastly, you may
try if there are shared content words between two tales.

The content words are confined to POS of "NOUN","ADJ","ADV" and "Verb", and the stop words are not
considered.


2. Usage

Selecting one fairy tale of Anderson's, you can check one type of POS with tokens and their counts from
the beginning, the middle, then to the end as follows:

	python main.py tale1.txt  pos

Given a positive integer, you may check the N most frequent POS within a tale as follows:

	python main.py tale1.txt pos --number1 10

Given a second tale, and a second positive integer, you may compare the commonly shared POS between the
two tales with respective count as follows:

	python main.py tale1.txt pos --tale2 tale2.txt --number2 10

Note that this programming uses a non-standard library spaCy (https://spacy.io) to parse POS, and only
support English language. If you haven't downloaded the respective model, please do so by running

	python -m spacy download en_core_web_sm


For further options, see

	python main.py --help


3. Data

The "data" directory contains 18 fairy tales of H.C. Anderson, downloaded from Gutenberg ebook.

The data is available at https://www.gutenberg.org/ebooks/1597


4. Background 

# # OPTIONAL: More background on the topic.


5. References

None







