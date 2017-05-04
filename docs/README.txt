Questions
--------------
Questions are built from sets of 21 consecutive sentences. A sentence is defined by the Stanford Core NLP sentence splitter.

An attempt is made to build a question out of every set of 21 consecutive sentences. More than one question can be built from any set of 21 consecutive sentences. To build a question there must be an instance in the 21st sentence (which becomes the 'missing word'). There must also be suitable candidates in sentences 1-20. This is the case if there are at least 9 candidates as the missing word. If this condition is not met, a question can still be built if there are sufficient instances of another word type in sentences 1-20.
