# Prerequisites : NLP -
# Resources : 
https://www.youtube.com/watch?v=eTieetk2dSw

Notion Repo for rest of the notes : https://www.notion.so/Instruction-Tuning-15541d41bdfc80a1a64be990a701fc5c

# Generative Pretrained Models are built on the foundation of :
1. Unsupervised Pretraining - Web Pages 
2. Supervised Finetuning - Benchmarks[ Classic NLP Benchmarks - Question Answering , Information retrieval , Sentence Completion ]
3. More Compute + data

Adapting Large language models to new tasks :
1. zero shot learning -> Prompting 
2. Few Shot Learning : Prompting with examples
3. Fine Tuning : Dozens or fewer examples 


Prompting[Prompt Engineering]:
1. Few shot or Many shot -> Exploring LLM possibilities 
# Cheap and quick way to test out 
# Prompt models - takes hours / minutes 
# Deploying these models -> Can take days

LLMS:
Supervised Finetuning : Trained on Benchmarks -> Instruction finetuning -> Following instructions , New Benchmarks: Bias ; Toxicity
- instruction tuning enhances supervised fine-tuning
- Subset of all possible finetuning
- Associated with following instructions 



Custom Models and Gen AI apps : Fine-tuning(Specific Task) -> Fine-tuning of input output schema [How user interacts with our app ]  
- Finetuning is about dialling things in for specific tasks 


INSTRUCT TUNING : 
DOLLY 5K , OpenLLama , qLORA 

About the Dolly 5k dataset :
1. Contains 15000 high quality human generated prompt-response pairs
2. Specifically designed for instruction tuning LLMs 
3. Dataset Structure : Instruction , Context , Response , Category
4. Categories of Instructions :
a. Creative Writing 
b. Close QA
c. Open QA 
d. Summarization 
e. Information Extraction 
f. Classification
g. Brainstorming 

Dolly 2.0 and 15k can be used commercially 

Model Information: OpenLLama 
1. Reproduction of meta AI's llama 
2. 1T token 
3. Trained on Red Pajama Dataset 
4. Apache 2.0 license - commercially usable 

 