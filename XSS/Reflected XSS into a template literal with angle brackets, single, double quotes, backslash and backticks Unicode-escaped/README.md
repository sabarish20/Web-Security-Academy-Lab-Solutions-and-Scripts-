# Documentation and python script for the Lab: Reflected XSS into a template literal with angle brackets, single, double quotes, backslash and backticks Unicode-escaped

![image](https://github.com/sabarish20/PortSwigger-Labs/assets/85452305/2e4905ad-9a69-4e3e-97c7-c340df4e0163)

### Understanding the JavaScript Parser

A JavaScript parser is a crucial component of a JavaScript engine, which is responsible for interpreting and executing JavaScript code in web browsers or other environments.

A backslash before a character tells the JavaScript parser that the character should be interpreted literally, and not as a special character such as a string terminator.

This means that the when we are entering a string which contains a special character like `single ( ' ) or double quotes ( " )` in it, then we use backslash before that character which tells the JavaScript parser to treat as a normal character  and not as a special character. 

So, if we want to include a single quote inside a single-quoted string, you can escape it like this:

``` Javascript
var stringWithSingleQuote = 'This is a string with a single quote \' inside it.';
```

As mentioned in the lab's description, we can check the search query by giving it  a single quote `'` as input and observe how it is getting treated.

![image](https://github.com/sabarish20/PortSwigger-Labs/assets/85452305/87cb2a6f-894d-4f0b-8b42-bb23e2c508ce)

![image](https://github.com/sabarish20/PortSwigger-Labs/assets/85452305/b2c65587-193c-4b6f-a8fd-665354de9050)

As we can see the special character is treated as a normal character by adding a backslash in front of it.

![image](https://github.com/sabarish20/PortSwigger-Labs/assets/85452305/7de9b06e-ad4c-46fa-84aa-05240317d7c5)

![image](https://github.com/sabarish20/PortSwigger-Labs/assets/85452305/29d6c751-a3ec-4cf6-bc4f-8cf5fb388bbe)

We can construct a payload that escaped the string:
```
\'; alert(1)//
```

Which gets converted into the below statement:

![image](https://github.com/sabarish20/PortSwigger-Labs/assets/85452305/26eafd2a-b275-4de8-9eb0-9a54270cc243)

Here, the first backslash means that the second backslash is interpreted literally, and not as a special character. This means that the quote is now interpreted as a string terminator, and so the attack succeeds.
