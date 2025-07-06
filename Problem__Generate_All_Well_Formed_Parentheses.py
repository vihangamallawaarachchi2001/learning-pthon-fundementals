n = 3
stack =[]
output_sample = ""
char_1 = "("
char_2 = ")"

def generate_paranthesis(n: int) -> list[str]:
    
    if n-1 != 0:
        generate_paranthesis(n-1)
    if output_sample.__len__ == 0:
        output_sample = char_1
        stack.insert(char_1)
    else:

        pass
    print(f" {output_sample} ")
    
# if 3 is the input then -> "( * 3" ,  ") * 3"
# ((()))

# 3! = 3*2*1 = 6

generate_paranthesis(3)