# this is one way to do str outputs via an api - Function calling

# The idea behind func calling -> 
# func calling is based on setting tools (strict:true) in the func def 

# output via tools is possible by setting strict:true withing function definition
# above technique works with all models that supports tools - gpt-4-0613 and gpt-3.5-turbo-0613 and later. 

# when structured outputs are enabled , then output will match exactly the tool definition. 



{"model":"gpt-4o-2024-08-06",
 "messages":[{
     "role":"system",
     "content":"You are a helpful assistant...."

 },
 {
     "role":"user",
     "content":"What is the weather like today?"
 }], 
 "tools":[
     {
         "type":"function",
         "function":{
             "name":"query",
             "description":"execute a query",
             "strict": True,
             "params":{
                 
             }

                               },

     }
 ]
 }
