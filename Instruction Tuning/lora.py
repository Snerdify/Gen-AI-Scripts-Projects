# Problem with LLMs and fine tuning them : We end up with really big weights 
# A lot more compute is required to fine tune these models 
# The file sizes become huge
# t5xxl checkpoint is about 40 gb
# the 20 billion parameters that are coming out now are getting bigger and bigger

# Hence this is where the idea of parameter efficient fine tuning comes in 

# PEFT employes variety of different techniques , one of which is called LORA(low-rank-adaptation)

# Other peft techniques - 
# 1. prefix tuning 
# 2. p tuning 
# 3. Prompt tuning 
# These are being used by NVIDIA to fine tune models from the cloud
# peft and lora allow you to fine-tune only a small number of extra weights in the model
# While most of the other parameters of the pre-trained network are freezed 

# We are not actually training the original weights , we are adding some extra weights 
# And we are finetuning those extra weights
# THE Advantage of this is that we are not changing the original weights of the model
# This avoids catastrophic forgetting
# Catastrophic forgetting : Models tend to forget what they were originally trained on when we fine tune them on a new task

# PEFT also allows us to get good fine tuning even if we have got small amount of data 
# https://github.com/huggingface/peft

# a lot of ai art models , stable diffusion models are using peft as well
# At the end you end up with tiny checkpoints that are very efficient to deploy
# Fine-Tune the llama model to create alpaca model - the final checkpoint was just 12mb
# We still need to use the original weights , but we can work with a small number of extra weights  
# PEFT allows to fine-tune an entire model by just fine-tuning few extra weights

# Huggingface PEFT library :
# The HF team has taken a few papers and implemented them in the PEFT library such that it can work with the 
# transformers library and accelerate library 
# Take off the shelf pre-trained models by google , hf or meta and fine tune them with peft

# code : How to use PEFT to do LORA fine-tuning of a model
