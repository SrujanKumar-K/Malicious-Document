import re
import sys


def fun_deobfucation(match):
    index=[int(i) for i in match.group(1).lstrip("{").rstrip("}").split("}{")]    #List Compression method 
    values=[i for i in match.group(2).lstrip("'").rstrip("'").split("','")]
    return "(" + "".join([values[i] for i in index]) + ")"                        # Join function 
    
def main():
    with open (sys.argv[1], "rt") as f:
        code=f.read()                                                             # Read file
    
    pattern=r"\(\"((?:\{\d+\})+)\"\s*-[fF]\s*((?:\'[^']+\'\,?)+)\)"               #Regex Pattern
    de_obsfucated=re.sub(pattern,fun_deobfucation,code.replace("`",""))           # Calling deosfucated function and repalced the Grave Char(`) with null in the code which is an Escape char in ps

    with open(sys.argv[1]+".bin", "wt") as f:
        f.write(de_obsfucated)                                                    # Write to file with an extension ".bin"


if __name__ == '__main__':                                                        #  main function 
    main()
