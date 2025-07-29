# Financial Advisor CEP
Financial Advisor Client Engagement Platform is a project started by me (Arthur Hoffmann).

The platform aims to help Financial Advisors by eliminating some of the friction experienced when on-boarding new clients. Especially the process of data capture, and communication with Superannuation/Insurance funds. 


# 1. Introduction
For Financial Advisors to give financial advice, they typically need to access a client's superannuation/insurance policy information.
For this to happen, the advisor would send the client a third party consent form, the client would put in their policy information, sign, and send it back to the advisor.
After the financial advisor has received the signed third party consent form, they would verify the information and send it off to the client's policy's for verfication.
This process is all done via email and is slow and error prone.

To reduce the overall friction of this process, a web application was created that serves the 2 types of users (financial advisors & clients) and aims to do the following:

- Allow advisors to register new clients (via name and email)
- Provide set forms to capture client information reliably
- Allow advisors to verify clients information
- Automate advisor emails to the client's super/insurance companies

# 1. Architecture
The CEP is written using **NextJS** and is hosted on **Vercel** 

```puml
@startuml
!includeurl https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

Person(client, "Client", "Inputs financial data")
Person(advisor, "Advisor", "Manages clients")

System_Boundary(cep, "CEP Platform") {
    Container(client_fe, "Client Frontend", "Typescript, React", "Web pages generated for clients. Capture client data.")
    Container(advisor_fe, "Advisor Frontend", "Typescript, React", "Web pages generated for financial advisors. Manage clients.")
    Container(backend, "Backend", "Typescript, Node, NextJS", "Renders web-pages (SSR), expose basic CRUD APIs")
}

Rel(client, client_fe, "Uses")
Rel(advisor, advisor_fe, "Uses")
Rel(client_fe, backend, "SSR, API calls")
Rel(advisor_fe, backend, "SSR, API calls")
@enduml
```

## Following text
