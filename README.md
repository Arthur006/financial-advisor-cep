# financial-advisor-cep
Financial Advisor Client Engagement Platform is a web application that demonstrates my (Arthur Hoffmann) interest in modern web development. It covers design decisions & architecture.

The code backing the CEP remains private (for now) but the resulting documentation can be viewed here: [Financial Advisor CEP](https://arthur006.github.io/financial-advisor-cep/)

## Purpose
This repository holds the source code that deploys the statically generated documenation for a Financial Advisor Client Engagement Platform developed by Arthur Hoffmann.

The documenation details the purpose of the CEP, as well as architecture and design.

## Development
To run a local preview of the generated documentation, check out the repository and run:

```bash
docker compose up
```
## Docs Deployment
This project deploys documentation using **MkDocs** static site generation with PlantUML generating the diagrams.

To deploy run the following command:

```bash
mkdocs gh-deploy
```