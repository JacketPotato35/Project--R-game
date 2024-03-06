import random
import sqlite3

connection_obj=sqlite3.connect("QUESTION.db")
cursor_obj=connection_obj.cursor()
def operator_questions():
    function_name="modulus"
    for i in range(1,5):
        a=random.randint(1,20)
        b=random.randint(1,5)
        pre_written_code=[f"A={a}"]
        end_written_code=[f"return A"]
        comment=f"use the modulus operator to find A modulus by {b} when A={a}"
        answer=a%b
        conditions=[b,"%"]
        print(comment,answer)
        sql_code=f"""
        INSERT INTO question ( function_name, comments, pre_written_code, end_written_code, conditions, answer, code_topic)
        VALUES ("{function_name}", "{comment}", "{pre_written_code}", "{end_written_code}", "{conditions}", "{answer}", "operators");
        """
        cursor_obj.execute(sql_code)
        connection_obj.commit()
    function_name="exponential"
    for i in range(1,5):
        a=random.randint(1,10)
        b=random.randint(1,3)
        pre_written_code=[f"A={a}"]
        end_written_code=[f"return A"]
        comment=f"use the exponential operator to find A to the power of {b} when A={a}"
        answer=a**b
        conditions=[b,"**"]
        print(comment,answer)
        sql_code=f"""
        INSERT INTO question ( function_name, comments, pre_written_code, end_written_code, conditions, answer, code_topic)
        VALUES ("{function_name}", "{comment}", "{pre_written_code}", "{end_written_code}", "{conditions}", "{answer}", "operators");
        """
        cursor_obj.execute(sql_code)
        connection_obj.commit()
    function_name="floor_division"
    for i in range(1,5):
        a=random.randint(1,50)
        b=random.randint(1,10)
        pre_written_code=[f"A={a}"]
        end_written_code=[f"return A"]
        comment=f"use the floor division operator to find A floor divided by {b} when A={a}"
        answer=a//b
        conditions=[b,"//"]
        print(comment,answer)
        sql_code=f"""
        INSERT INTO question ( function_name, comments, pre_written_code, end_written_code, conditions, answer, code_topic)
        VALUES ("{function_name}", "{comment}", "{pre_written_code}", "{end_written_code}", "{conditions}", "{answer}", "operators");
        """
        cursor_obj.execute(sql_code)
        connection_obj.commit()
def iteration_questions():
    function_name="while_loop"
    for i in range(1,5):
        a=random.randint(1,5)
        b=random.randint(10,20)
        pre_written_code=[f"A=0"]
        end_written_code=[f"return A"]
        comment=f"use a while loop, that adds {a} to A until A is greater than {b}"
        c=a
        d=b
        e=0
        while e<d:
            e+=c
        answer=e
        conditions=["while","+"]
        print(comment,answer)
        sql_code=f"""
        INSERT INTO question ( function_name, comments, pre_written_code, end_written_code, conditions, answer, code_topic)
        VALUES ("{function_name}", "{comment}", "{pre_written_code}", "{end_written_code}", "{conditions}", "{answer}", "iteration");
        """
        cursor_obj.execute(sql_code)
        connection_obj.commit()
    function_name="for_loop"
    for i in range(1,5):
        a=[]
        for i in range(5):
            a.append(int(random.randint(1,5)))
        pre_written_code=[f"""A=({a[0]},{a[1]},{a[2]},{a[3]},{a[4]})"""]
        end_written_code=[f"return B"]
        comment=f"use a for loop, to make B the sum of all numbers in A"
        total=0
        for i in a:
            total+=i
        answer=total
        conditions=["for","+"]
        print(comment,answer)
        sql_code=f"""
        INSERT INTO question ( function_name, comments, pre_written_code, end_written_code, conditions, answer, code_topic)
        VALUES ("{function_name}", "{comment}", "{pre_written_code}", "{end_written_code}", "{conditions}", "{answer}", "iteration");
        """
        cursor_obj.execute(sql_code)
        connection_obj.commit()
def if_statement():
    function_name="if_statements"
    for i in range(1,5):
        a=random.randint(1,20)
        b=random.randint(1,5)
        pre_written_code=[f"A={a}"]
        end_written_code=[f"return A"]
        comment=f"use the modulus operator to find A modulus by {b} when A={a}"
        answer=a%b
        conditions=[b,"%"]
        print(comment,answer)
        sql_code=f"""
        INSERT INTO question ( function_name, comments, pre_written_code, end_written_code, conditions, answer, code_topic)
        VALUES ("{function_name}", "{comment}", "{pre_written_code}", "{end_written_code}", "{conditions}", "{answer}", "if_statements");
        """
        cursor_obj.execute(sql_code)
        connection_obj.commit()