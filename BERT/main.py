# SENTIMENT ANALYSIS USING BERT AND HUGGING FACE TRANSFORMERS
from transformers import pipeline 

classifier = pipeline("sentiment-analysis",
                      model = "bert-base-uncased",
                      tokenizer = "bert-base-uncased")

sentences = ["I hate doing my homework ", 
             " I love playing video games"]

results = classifier(sentences)

for sentence , res in zip(sentences, results):
    print(f"Sentence:{sentence}")
    print(f"Sentiment Prediction : {res['label']} | Score:{res['score']:.4f}")
