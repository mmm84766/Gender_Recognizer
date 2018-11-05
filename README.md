# IdentifyGender
Python code to identify a gender given a first name for the person.

*. Simple Implementation -  A simple piece of python code which classifies first names based on the idea that most names end with the vowels 'a', 'e' or 'i'. Though the 'confidence' level of this method is low , it is easy and fast to implement and works just fine for most Indian names.

Assumption : We just have access to the first name and nothing else. 

Source : Coded based on inputs from [Quora](https://www.quora.com/Is-there-a-phonetic-linguistic-difference-between-male-and-female-names)

*. From Datasets - We can filter the first names from large datasets , which are readily available in public domain with high confidence level. On the downside, it will work only if the names are present in the dataset. Please note that I have used the gender_detector package shared under GNU GP Licence.

Assumption: The names entered cater to country codes and the names available in the dataset are considered for gender classification.

# How to run?

The entire code is written in Python3, So any Python 3.x release would run the code without any hiccups. Now run the identify_gender.py file from each one of the two folders in IdentifyGender folder to test the code.
