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
The CEP is written using **NextJS** and is hosted on **Vercel**.
Hosting on Vercel has its limitations (free tier hosting limits process execution time) and has driven a lot of the design decisions.
This includes breaking out CPU intensive functionality to AWS lambdas. 

```puml
@startuml

!includeurl https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

!$ICONURL = "https://raw.githubusercontent.com/tupadr3/plantuml-icon-font-sprites/v3.0.0/icons"
!include $ICONURL/common.puml
!include $ICONURL/devicons2/supabase.puml
!include $ICONURL/devicons2/vercel_original_wordmark.puml
!include $ICONURL/devicons2/amazonwebservices_wordmark.puml

Person(client, "Client", "Inputs financial data")
Person(advisor, "Advisor", "Manages clients")

System(cep, "CEP Platform", "NextJS fullstack webapp", $sprite="vercel_original_wordmark") 
System(supa, "Supabase", "User relationship management, authentication, long term object storage")
System(aws, "AWS", "File resize service, email servie", $sprite="amazonwebservices_wordmark")

Rel(client, cep, "Uses")
Rel(advisor, cep, "Uses")
Rel(cep, supa, "Uses")
Rel(cep, aws, "Uses")
@enduml
```

```puml
@startuml

!$ICONURL = "https://raw.githubusercontent.com/tupadr3/plantuml-icon-font-sprites/v3.0.0/icons"
!define AWSPuml https://raw.githubusercontent.com/awslabs/aws-icons-for-plantuml/v20.0/dist
!includeurl https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml
!include $ICONURL/common.puml
!include $ICONURL/devicons2/supabase.puml
!include AWSPuml/AWSCommon.puml
!include AWSPuml/Storage/SimpleStorageService.puml
!include AWSPuml/Compute/Lambda.puml

LAYOUT_WITH_LEGEND()

Person(client, "Client", "Inputs financial data")
Person(advisor, "Advisor", "Manages clients")

System_Boundary(cep, "CEP Platform") {
    Container(client_fe, "Client Frontend", "Typescript, React", "Web pages generated for clients. Capture client data.")
    Container(advisor_fe, "Advisor Frontend", "Typescript, React", "Web pages generated for financial advisors. Manage clients.")
    Container(backend, "Backend", "Typescript, Node, NextJS", "Renders web-pages (SSR), expose basic CRUD APIs")
}

Enterprise_Boundary(supa, "Supabase") {
    ContainerDb(supa_db, "Database", "PostgreSQL", $sprite="supabase")
    Container_Ext(supa_bucket, "Bucket", $sprite="supabase")
}

Enterprise_Boundary(aws, "AWS") {
    Container_Ext(aws_s3, "S3", "User images", $sprite="SimpleStorageService") 
    Container(aws_resizer, "Image processor", "Javascript", "Resize images", $sprite="Lambda") 
    Container(aws_emailer, "Emailer", "Javascript", "Structure and send emails to funds", $sprite="Lambda") 
}

Rel(client, client_fe, "Uses")
Rel(advisor, advisor_fe, "Uses")
Rel(client_fe, backend, "SSR, API calls")
Rel(advisor_fe, backend, "SSR, API calls")
Rel(client_fe, aws_s3, "Upload via signed URL")
Rel(advisor_fe, aws_s3, "Upload via signed URLs")
Rel(aws_s3, aws_resizer, "Trigger on PUT")
Rel(aws_resizer, supa_bucket, "Service Upload")
Rel(backend, supa_db, "CRUD queries & User authentication")
Rel(backend, aws_emailer, "Trigger email process")

@enduml
```

## Following text
