# An LLM keeps predicting the next word in a sentence in an iterative way 
# A NEXT TOKEN PREDICTION TASK 
# Its a Deep Neural Network 

Data Preparation and Sampling :
To prepare a dataset for pre-training , give an input word to the LLM and let it predict the next , without giving access of the word after it. Continue building the dataset by giving the LLM learning tasks where one word is missing and it has to predict that next word. 

HOW DOES THE TRAINING FUNCTION WORK ? 


BATCHING : Put multiple training inputs into a batch , they are implemented as tensors , hence you can think of them as a matrix .

Sample text : In the heart of city , stood an old library

Tensor : x = tensor(["In","the","heart","of"],
            ["city","stood","an","old"],
            ["library"])

Input text len : 256 for smaller models and >1024 for large ones

HOW DO LLMs GENERATE MULTI-WORD OUTPUTS ? 


WHAT ARE PEFT ADAPTERS ? 


