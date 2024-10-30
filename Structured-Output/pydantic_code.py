'''
Pseudo-Code
class X(BaseModel):
    class Step(BaseModel):
        description: str = Field(description="Description of the steps taken")
        action: str = Field(action="Action taken to solve the issue")

    steps: list[Step]
    final_answer : str = Field(description="Final answer given to the user")
    confidence:float = Field(description="Confidence level of the answer (0-1)", ge=0 ,le=1)



    
'''