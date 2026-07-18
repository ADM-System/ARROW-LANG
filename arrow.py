"""
Arrow Programming Language
Interpreter v0.2 Genesis

Flow Programming Language
"""


import sys
import re

from stdlib import STD_FUNCTIONS



# =====================================
# ENVIRONMENT
# =====================================


class Environment:

    def __init__(self, parent=None):

        self.vars={}
        self.functions={}
        self.parent=parent



    def set(self,name,value):

        self.vars[name]=value



    def get(self,name):

        if name in self.vars:
            return self.vars[name]

        if self.parent:
            return self.parent.get(name)

        return None



env=Environment()

# =====================================
# STRUCT OBJECT
# =====================================


class ArrowStruct:


    def __init__(self, name, fields, values):

        self.type = name

        self.fields = {}


        for field, val in zip(fields, values):

            self.fields[field] = val



    def get(self, name):

        return self.fields.get(name)



    def set(self, name, value):

        self.fields[name] = value



    def __repr__(self):

        return str(self.fields)



env.structs={}

env.structs={}


# =====================================
# TOKENIZER
# =====================================


def tokenize(line):

    pattern = r'''
        "[^"]*"
        |\[(.*?)\]
        |(\d+)
        |([A-Za-z_][A-Za-z0-9_\.\[\]]*)
        |(==|!=|>=|<=|\$>|£>|>>|<<|->|<-|§)
        |([+\-*/%><=&|!])
    '''

    result = []


    for m in re.finditer(
        pattern,
        line,
        re.VERBOSE
    ):

        token = m.group(0)

        result.append(token)


    return result



# =====================================
# VALUES
# =====================================


def value(x,local=env):


    if x=="true":
        return True


    if x=="false":
        return False



    if x.startswith('"') and x.endswith('"'):

        return x[1:-1]



    if x.isdigit():

        return int(x)



    # array access

    if "[" in x:

        name,index=x.split("[")

        index=int(
            index.replace("]","")
        )

        arr=local.get(name)

        return arr[index]



        # STRUCT ACCESS

    if "." in x:

        parts=x.split(".")


        obj=local.get(
            parts[0]
        )


        for p in parts[1:]:

            if isinstance(
                obj,
                ArrowStruct
            ):

                obj=obj.get(p)



        return obj



    return local.get(x)



# =====================================
# EXPRESSIONS
# =====================================


def expression(tokens,local=env):


    if len(tokens)==1:

        return value(
            tokens[0],
            local
        )



    left=value(
        tokens[0],
        local
    )


    op=tokens[1]


    right=value(
        tokens[2],
        local
    )


    if op=="+":
        return left+right

    if op=="-":
        return left-right

    if op=="*":
        return left*right

    if op=="/":
        return left/right


    if op=="==":
        return left==right

    if op=="!=":
        return left!=right

    if op==">":
        return left>right

    if op=="<":
        return left<right

    if op==">=":
        return left>=right

    if op=="<=":
        return left<=right


    if op=="&":
        return left and right


    if op=="|":
        return left or right


    return None


# =====================================
# PIPELINE
# =====================================


def pipeline(tokens, local=env):

    current = value(
        tokens[0],
        local
    )

    i = 1

    while i < len(tokens):

        if tokens[i] == "->":

            func = tokens[i + 1]


            if func in STD_FUNCTIONS:

                current = STD_FUNCTIONS[func](
                    current
                )


            elif func in local.functions:

                current = local.functions[func].call(
                    [current]
                )


            i += 2


        else:

            i += 1


    return current
# =====================================
# BLOCK PARSER
# =====================================


def clean_lines(code):

    lines=[]

    for line in code.split("\n"):

        line=line.rstrip()


        if not line:
            continue


        if line.strip().startswith("//"):
            continue


        lines.append(line)


    return lines



def find_block_end(lines,start,end_word):

    depth=0


    for i in range(start,len(lines)):

        text=lines[i].strip()


        if text.startswith(end_word):

            if depth==0:
                return i


        if text.startswith(
            "if "
        ) or text.startswith(
            "wh "
        ) or text.startswith(
            "for "
        ):

            depth+=1



    return len(lines)-1



# =====================================
# EXECUTE SINGLE LINE
# =====================================


def execute(line,local=env):


    tokens=tokenize(line)
    # =====================================
    # INPUT UTENTE
    # =====================================

    if len(tokens) >= 4 and tokens[0] == "$>" and tokens[2] == ">>":

        prompt = value(
            tokens[1],
            local
        )

        result = input(prompt)

        local.set(
            tokens[3],
            result
        )

        return result

    # =====================================
    # INPUT CLI
    # =====================================

    if len(tokens) >= 4 and tokens[0] == "£>" and tokens[2] == ">>":

        index = int(
            value(
                tokens[1],
                local
            )
        )


        try:

            result = sys.argv[
               index + 2
            ]


        except IndexError:

            raise Exception(
                f"CLI argument {index} not found."
            )


        local.set(
            tokens[3],
            result
        )


        return result

    


    if not tokens:
        return None



    # RETURN

    if tokens[0]=="<-":

        return (
            "RETURN",
            expression(
                tokens[1:],
                local
            )
        )



    # OUTPUT

    if tokens[-1]=="<<":


        data=tokens[:-1]


        if "->" in data:

            result=pipeline(
                data,
                local
            )

        else:

            result=expression(
                data,
                local
            )


        print(result)

        return



    # ASSIGNMENT
        # STRUCT CREATION

    if "§" in tokens:


        pos=tokens.index(
            "§"
        )


        struct_name=tokens[0]


        values=[]


        for item in tokens[pos+1:]:

            if item == ">>":
                break


            values.append(
                value(item,local)
           )

        obj=ArrowStruct(
            struct_name,
            env.structs[struct_name],
            values
        )


        name=tokens[
            tokens.index(">>")+1
        ]


        local.set(
            name,
            obj
        )


        return

    if ">>" in tokens:


        pos=tokens.index(
            ">>"
        )


        left=tokens[:pos]


        name=tokens[pos+1]


        if "->" in left:

            result=pipeline(
                left,
                local
            )

        else:

            result=expression(
                left,
                local
            )


        # STRUCT FIELD ASSIGNMENT

        if "." in name:

            parts=name.split(".")


            obj=local.get(
                parts[0]
            )


            if isinstance(
                obj,
                ArrowStruct
            ):

                obj.set(
                    parts[1],
                    result
                )

                return



    local.set(
        name,
        result
    )
    return



# =====================================
# RUN BLOCK
# =====================================


def run_block(lines,local=env):


    i=0


    while i<len(lines):


        line=lines[i].strip()



        # ---------------------
        # IF
        # ---------------------

        if line.startswith("if "):


            condition=expression(
                tokenize(
                    line[3:]
                ),
                local
            )


            end=find_block_end(
                lines,
                i+1,
                "-if"
            )


            block=lines[
                i+1:end
            ]


            else_block=[]


            for index,l in enumerate(block):

                if l.strip()=="else":

                    else_block=block[index+1:]

                    block=block[:index]

                    break



            if condition:

                result=run_block(
                    block,
                    local
                )

            else:

                if else_block:

                    result=run_block(
                        else_block,
                        local
                    )


            i=end



        # ---------------------
        # WHILE
        # ---------------------

        elif line.startswith("wh "):


            end=find_block_end(
                lines,
                i+1,
                "-wh"
            )


            condition=line[3:]


            while expression(
                tokenize(condition),
                local
            ):

                result=run_block(
                    lines[i+1:end],
                    local
                )

                if isinstance(result,tuple):
                    return result



            i=end


	# ---------------------
        # FOR LOOP
        # ---------------------

        elif line.startswith("for "):


            parts=line.split()


            variable=parts[1]


            array_name=parts[3]



            end=find_block_end(
                lines,
                i+1,
                "-for"
            )


            array=local.get(
                array_name
            )



            for item in array:


                local.set(
                    variable,
                    item
                )


                result=run_block(
                    lines[i+1:end],
                    local
                )


            i=end
        # ---------------------
        # NORMAL LINE
        # ---------------------

        else:

            result=execute(
                line,
                local
            )


            if isinstance(result,tuple):

                return result



        i+=1



    return None

# =====================================
# ARROW FUNCTIONS
# =====================================


class ArrowFunction:


    def __init__(self,params,body):

        self.params=params
        self.body=body



    def call(self,args):

        local=Environment(
            env
        )


        for name,val in zip(
            self.params,
            args
        ):

            local.set(
                name,
                val
            )


        result=run_block(
            self.body,
            local
        )


        if isinstance(result,tuple):

            if result[0]=="RETURN":

                return result[1]


        return None




# =====================================
# FUNCTION PARSER
# =====================================


def parse_functions(lines):


    i=0


    clean=[]


    while i<len(lines):


        line=lines[i].strip()



        if line.startswith("fn "):


            parts=line.split()


            name=parts[1]


            params=parts[2:]



            end=find_block_end(
                lines,
                i+1,
                "-fn"
            )


            body=lines[
                i+1:end
            ]


            env.functions[name]=ArrowFunction(
                params,
                body
            )


            i=end



        else:

            clean.append(
                lines[i]
            )


        i+=1



    return clean



# =====================================
# FUNCTION CALL IN PIPELINE
# =====================================


def call_pipeline_function(
    name,
    value
):


    fn=env.functions.get(
        name
    )


    if fn:

        return fn.call(
            [value]
        )


    return None

# =====================================
# STRUCT PARSER
# =====================================


def parse_structs(lines):

    i = 0

    clean = []


    while i < len(lines):

        line = lines[i].strip()


        if line.startswith("ST "):

            name = line.split()[1]


            end = find_block_end(
                lines,
                i + 1,
                "-ST"
            )


            fields = []


            for f in lines[i+1:end]:

                fields.append(
                    f.strip()
                )


            env.structs[name] = fields


            i = end


        else:

            clean.append(
                lines[i]
            )


        i += 1


    return clean
# =====================================
# PROGRAM LOADER
# =====================================


def run(code):


    lines=clean_lines(
        code
    )


    lines=parse_functions(
        lines
    )
    
    lines=parse_structs(
        lines
    )


    run_block(
        lines
    )



# =====================================
# REPL
# =====================================


def repl():

    print(
        "Arrow Programming Language 0.2 Genesis"
    )


    while True:

        try:

            line=input(
                "Arrow > "
            )


            execute(
                line
            )


        except KeyboardInterrupt:

            break


        except Exception as e:

            print(
                "Error:",
                e
            )



# =====================================
# MAIN
# =====================================


if __name__=="__main__":


    if len(sys.argv)>1:


        with open(
            sys.argv[1],
            encoding="utf8"
        ) as file:


            run(
                file.read()
            )


    else:

        repl()

# =====================================
# STRUCT SYSTEM
# =====================================


class ArrowStruct:


    def __init__(self,name,fields,values):

        self.type=name

        self.fields={}


        for field,value in zip(
            fields,
            values
        ):

            self.fields[field]=value



    def get(self,name):

        return self.fields.get(
            name
        )



    def set(self,name,value):

        self.fields[name]=value



    def __repr__(self):

        return str(
            self.fields
        )



env.structs={}

# =====================================
# STRUCT PARSER
# =====================================


def parse_structs(lines):


    i=0

    clean=[]


    while i<len(lines):


        line=lines[i].strip()


        if line.startswith("ST "):


            name=line.split()[1]


            end=find_block_end(
                lines,
                i+1,
                "-ST"
            )


            fields=[]


            for f in lines[i+1:end]:

                fields.append(
                    f.strip()
                )


            env.structs[name]=fields


            i=end



        else:

            clean.append(
                lines[i]
            )


        i+=1



    return clean