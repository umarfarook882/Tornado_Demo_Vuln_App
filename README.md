# Injecting RASP (Runtime Application Self Protection) Security into Tornado Demo Vuln App
Tornado Demo Vulnerable Application to test SQL injection vulnerability and patch it using RASP (Runtime Application Self-Protection)
''' Support on Python 2 && python 3 


**How RASP works with the Demo Vuln App?**

    1.Hooking DbApi2 Call for execute() instruction.
    
    2.Extract the Query from the execute (query)

    For example
    Query= SELECT * from users where userid=1

    3.Lexical Analysis and token generation for the Query extracted from the execute() instruction

    Using Lexer convert the query into token
    Token = ['KEYWORD', 'WHITESPACE', 'OPERATOR', 'WHITESPACE', 'KEYWORD', 'WHITESPACE', 'STRING', 'WHITESPACE',
    'KEYWORD', 'WHITESPACE', 'STRING', 'OPERATOR', 'NUMBER']
    
    4.Run RASP in Learning mode to make it understand what is the Correct user input structure that need for application to work.
    
    5.RASP will automatically insert the rules into separate database i.e rules.db while in Learning mode
    
    6.Once application is reach the learning mode limitation i.e threshold limit, it will block no more rules to insert into
    rules database while in leaning mode.
    
    In my RASP Model, threshold limit for rules to insert into rules.db is 2 for demo purpose. so only two rules are allowed in     rules database. 
    
    7.So now, we have have the rules ready to block SQL injection attack :)
    
    8.Check the below video to see how it works.. :)
    
## Demo Video
  
   [![Alt text](https://img.youtube.com/vi/5yKH3nFZ9lY/0.jpg)](https://www.youtube.com/watch?v=5yKH3nFZ9lY)

## Credits:
* FOS Team : [Fools of Security](https://www.youtube.com/channel/UCEBHO0kD1WFvIhf9wBCU-VQ)

## Support !
 Email address: umarfarookmech712@gmail.com | foolsofsecur1ty@gmail.com for more details. <br>
 Youtube: [FOS](https://www.youtube.com/channel/UCEBHO0kD1WFvIhf9wBCU-VQ) <br>
 Blog: [FOS](https://fosecurity.blogspot.com) 

## Useful links:
1. [Ajin Abraham](http://ajinabraham.com/)
2. [Kali](https://www.kali.org/)
3. [Debuggex](https://www.debuggex.com/)
4. [Vulnerable Tornado App](https://github.com/ajinabraham/Vulnerable_Tornado_App)
6. [Sqreen](https://blog.sqreen.io/)

