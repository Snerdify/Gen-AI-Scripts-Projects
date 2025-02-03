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
## Cheap and quick way to test out 
Prompt models - takes hours / minutes 
Deploying these models -> Can take days

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

Fine-Tuning technique
QloRa : Efficient fine-tuning of quantized models 
Idea : Downstream tasks have intrinsically low dimensions
Lot less compute required when using this technique for finetuning 
- uses bitsandbytes for quantization
- uses huggingface's PEFT techniques 
- Qlora is an improvement on LORA 



TODO:
1. IMPLEMENT LORA AND QLORA SEPERATELY TO UNDERSTAND THEIR USE BETTER 
PEFT-LORA-CHECKPOINTS is the actual collab notebook 
- About the BLOOM(BigScience Large Open-science Open-access Multilingual Language Model) 
-BLOOM is an autoregressive Large Language Model (LLM), trained to continue text from a prompt on vast amounts of text data using industrial-scale computational resources. As such, it is able to output coherent text in 46 languages and 13 programming languages that is hardly distinguishable from text written by humans. BLOOM can also be instructed to perform text tasks it hasn't been explicitly trained for, by casting them as text generation tasks.
-Decoder only 
- Causal Language Model 
- Good token max length(good level of context can be fetched)
- Good Vocab size
- Trained on fairly large set of languages , including code 
- Has a permissive license 

- why do we cast low dim params as float32 ? 

Summary of freezing weights during LORA : 
1. Freezing Parameters: Prevents updating original weights during fine-tuning.
2. Casting Small Parameters to float32: Improves numerical stability for critical layers like LayerNorm.
3. Gradient Checkpointing: Reduces memory usage by recomputing activations.
4. Input Gradients: Required for advanced fine-tuning methods (like LoRA or custom adapters).
5. Casting Outputs to float32: Ensures stable logits for downstream tasks like loss calculation


Summary of setting up LORA parameters :
1. The function provides a detailed view of the model's parameter trainability.
2. It ensures the fine-tuning setup (like LoRA or other adapter methods) is configured as intended.
3. This kind of utility is crucial when working with large models to optimize memory and computational efficiency.

Summary of LoraConfig :
This code initializes and applies a LoRA configuration to a causal language model.
By using LoRA:
The majority of the model's parameters remain frozen (not updated during training).
Only the low-rank matrices (r=16) and their scaled adaptations are trained, making the fine-tuning process lightweight and efficient.
The configuration includes dropout for better generalization, scaling for controlled adaptation, and a task-specific setting for causal language modeling.

2. Fine-Tune the llama model to create alpaca model - Sam Witteven
3. Difference between Casual modelling(decoder , text regressive models ) and seq2seq model
4. Implement QLORA - SEntDEx