# Documentation and python script for the Lab: Reflected XSS into HTML context with most tags and attributes blocked

![image](https://github.com/sabarish20/PortSwigger-Labs/assets/85452305/bfcc50f8-182b-40f0-84ba-7c3646609b23)

### Testing for the `tag` which is not being blocked

When entering a known tag, the `WAF` automatically blocks it and gives a 404 response.

![image](https://github.com/sabarish20/PortSwigger-Labs/assets/85452305/e4e71238-509e-48d4-8f7a-b431807d7f7a)

![image](https://github.com/sabarish20/PortSwigger-Labs/assets/85452305/571f9651-1793-443b-afa0-c6c9ea2dbccc)

but when entering a custom tag, it wasn't getting blocked instead it got reflected back in the response.

![image](https://github.com/sabarish20/PortSwigger-Labs/assets/85452305/db08e91c-afaf-4341-ba5b-4774c805e866)

![image](https://github.com/sabarish20/PortSwigger-Labs/assets/85452305/622219ea-2cfd-444a-8573-ea557cdf9fa2)

so with this we can clearly understand that we can brute-force the tags and look for any tags that is getting reflected back in the response.

Brute-force results:

![image](https://github.com/sabarish20/PortSwigger-Labs/assets/85452305/33ec3317-a595-4ade-a5ce-05787646749a)

![image](https://github.com/sabarish20/PortSwigger-Labs/assets/85452305/2e927e6f-c8c3-4ad8-807c-edfa9bbf1373)

As we can see that the `body` tag was not getting filtered out by the WAF.

### Testing for `attribute` which is not being blocked

```
What is attribute?

HTML attributes provide additional information to HTML tags or elements.

For example:
<a href="http://example.com">Example</a>

here the <a> is the tag and href is the attribute of that tag. 
```

We can use `onload` attribute with the `body` tag.

![image](https://github.com/sabarish20/PortSwigger-Labs/assets/85452305/8f82f822-f224-4a9c-9025-4e5eb15db9b5)

![image](https://github.com/sabarish20/PortSwigger-Labs/assets/85452305/526bba29-00fb-4f73-b791-7f9d57b003f0)

Looking at the response, the `onload` attribute of the `body` tag is being blocked by the WAF.

We can again brute-force the attribute and look for anything that is getting reflected back in the response:

![image](https://github.com/sabarish20/PortSwigger-Labs/assets/85452305/5bd03081-fd69-4b53-b283-a5132ec47af9)

![image](https://github.com/sabarish20/PortSwigger-Labs/assets/85452305/1bfedf7e-9cf9-4649-9781-38598306d7a7)

We can see that there are 5 attributes which is not been blocked by the WAF:

```
onebeforeinput: The onbeforeinput event occurs when an element is about to get a input. 

onbeforetoggle: The ontoggle event occurs when the user opens or closes the details element.

onratechange: The onratechange event occurs when the playing speed of a media is changed.

onresize: The onresize event occurs when the browser window has been resized.

onscrollend: It occurs when the scroll comes to the end of the page.
```
We can see that the`onresize` element will be easy for us to craft but this requires user interaction to make the script to work. 
To make this script work without user interaction, we can use a tag called "`<iframe>`".

```
The iframe tag is used to embed another document within the current HTML document.
```

The major drawback of this exploit is that the user needs to visit the url for the script to get executed.

Lets host a server:

![image](https://github.com/sabarish20/PortSwigger-Labs/assets/85452305/d4368f20-88aa-442d-9fec-a5aec4bb497b)

Crafting the payload: 
```
<iframe src="https://EXAMPLE.web-security-academy.net/?search=<body onresize=print()>" onload=this.style.width='100px'>
```
We know that `onload` event is getting blocked by the WAF, then why did we use it ?

It is because the `onload` event is happening inside the attacker controlled page.

![image](https://github.com/sabarish20/PortSwigger-Labs/assets/85452305/6ca5722e-e8b6-41c7-8737-337fd59f932d)

click store and after click deliver the exploit, then click view exploit.

Congratulations you have solved the Lab.

