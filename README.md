# Hello World
So i will be recording my python junior developer journey here 
I wish to learn
- Python
- PostgreSQL/SQL
- SQLAlchemy + Alembic
- FastAPI + REST API
- JWT Authentication
- Testing
- Git & Github
- Docker
- Github Actions
- AWS basics
- HTML,CSS,Javascript
- MongoDB
- Redis
- Pinecone
- LangChain
- React
- NodeJS
- Rust

This will be done with exercises instead of blind following theories , also no copy paste allowed, but can look up with LLMs, Will be doing projects too

Before Note: i can understand python, but most code is vibecoded I know git and github, have pulled and pushed but don’t how to work in a team repo,I know how to pull docker images and deploy, i have deployed n8n as self hosted I have used REST APIs in n8n, like get and post I know little sql queries, knows very little javascript, i had done something with FastAPI but it was vibe coded

__________________________________________________________________________________________________________________________________


## Phase 1 — Professional Python                                               [18-06-26 -- 22-06-26]
Duration: 1-2 weeks

Goal:
Write Python without AI helping every line.
Learn: 
* Functions
* Error Handling
* Collections & Comprehension
* Classes & OOP 
* Modules & Packages
* File Handling & JSON  
* Type Hints
* Generators
* Decorators (basic)
* Virtual Environments

### Module 1: Functions                                                         [18-06-26 -- 18-06-26]
Learn:
Parameters, Return values , Scope, Default arguments, *args, **kwargs

### Module 2: Error Handling                                                    [19-06-26 -- 19-06-26]
Learn:
try,except,else,finally,raising exceptions

### Module 3: Collections & Comprehensions                                      [20-06-26 -- 20-06-26]
Learn:
Lists,Tuples,Dictionaries,Sets,List comprehensions,Dictionary comprehensions

### Module 4: Classes & OOP                                                     [21-06-26 -- 21-06-26]
Learn:Classes,Objects,Constructors,Methods,Attributes,Encapsulation,Inheritance,Polymorphism 

### Module 5: Modules & Packages                                                [22-06-26 -- 22-06-26]
Learn:Importing,Creating modules,Creating packages,__init__.py

### Module 6: File Handling & JSON                                              [22-06-26 -- 22-06-26]
Learn:Reading files,Writing files,JSON loading,JSON saving

### Module 7: Type Hints                                                        [22-06-26 -- 22-06-26]
Learn:Function annotations,typing module,Optional,List,Dict

### Module 8: Generators                                                        [22-06-26 -- 22-06-26]
Learn:yield,Generator functions,Generator expressions

### Module 9: Decorators                                                        [22-06-26 -- 22-06-26]
Learn:Functions as objects,Wrapper functions,Basic decorators

### Module 10: Virtual Environments                                             [22-06-26 -- 22-06-26]
Learn:venv,pip,requirements.txt


__________________________________________________________________________________________________________________________________


## Phase 2 — SQL & PostgreSQL                                                   [24-06-26 -- 26-06-26]
Duration: 1 week

Goal:
Learn: 
* Database Fundamentals
* Install PostgreSQL
* CRUD Operations
* Primary Keys & Foreign Keys 
* Filtering Data 
* Sorting & Limiting
* JOINs
* Aggregation
* Constraints, Indexes & Transactions

### Module 1: Database Fundamentals                                              [24-06-26 -- 24-06-26]
Learn: Rows & Columns, Tables, IDs, Relationships

### Module 2: Install PostgreSQL                                                 [24-06-26 -- 24-06-26]
SQL Shell (psql), pgAdmin

### Module 3: CRUD Operations                                                    [24-06-26 -- 25-06-26]
Create, Read, Update, Delete

### Module 4: Primary Keys & Foreign Keys                                        [26-06-26 -- 26-06-26]
Foreign Key Constraint, Relationship Types

### Module 5: Filtering Data                                                     [26-06-26 -- 26-06-26]
WHERE, AND, OR, IN, BETWEEN, LIKE, IS NULL

### Module 6: Sorting & Limiting                                                 [26-06-26 -- 26-06-26]
ORDER BY, LIMIT, OFFSET                  

### Module 7: JOINs                                                              [26-06-26 -- 26-06-26]
INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN

### Module 8: Aggregation                                                        [26-06-26 -- 26-06-26]
COUNT,SUM,AVG,MIN,MAX,GROUP BY,HAVING

### Module 9: Constraints, Indexes & Transactions                                [26-06-26 -- 26-06-26]
NOT NULL,UNIQUE,CHECK,DEFAULT,FOREIGN KEY,Indexes,BEGIN,COMMIT,ROLLBACK


__________________________________________________________________________________________________________________________________


## Phase 3 —  SQLAlchemy + Alembic                                               [26-06-26 -- 02-07-26]
Duration: 1 week

Goal:
Learn:
* What is an ORM?
* Installing & Configuring SQLAlchemy
* Creating Models
* Relationships
* CRUD Operations
* Filtering, Sorting & Querying
* Session Management
* Loading Strategies 
* SQLAlchemy Production Best Practices 
* Alembic

### Module 1: What is an ORM                                              [27-06-26 -- 27-06-26]
ORM 

### Module 2: SQLAlchemy Architecture                                    [27-06-26 -- 27-06-26]
Installing SQLAlchemy,Engine,Database URL,Base class,Sessions,How SQLAlchemy connects to PostgreSQL

### Module 3: Models                                                      [28-06-26 -- 28-06-26]
Models,__tablename__,Mapped,mapped_column(),Column types,Primary Keys,Foreign Keys,Constraints,How a Python class becomes a PostgreSQL table

### Module 4: Relationships                                               [29-06-26 -- 29-06-26]
Why relationship() exists,One-to-Many,back_populates,One-to-One,Many-to-Many

### Module 5: CRUD with SQLAlchemy                                        [30-06-26 -- 30-06-26]
Create,Read,Update,Delete

### Module 6: Querying with SQLAlchemy                                    [01-07-26 -- 01-07-26]
where(),Multiple conditions (AND, OR),order_by(),limit(),offset(),Joins,Aggregation (COUNT, SUM, AVG, ...),group_by(),having()

### Module 7: Session Management                                          [01-07-26 -- 01-07-26]
Session lifecycle,commit(),rollback(),flush(),refresh(),expire(),Identity Map

### Module 8: Loading Strategies                                          [01-07-26 -- 01-07-26]
Lazy Loading,Eager Loading,joinedload(),selectinload(),The N+1 Query Problem

### Module 9: Production Best Practices                                   [01-07-26 -- 01-07-26]
How SQLAlchemy is organized in real FastAPI projects,Where engine, SessionLocal, and models live,Common beginner mistakes,Basic Repository Pattern (only what juniors should know),Performance tips,Clean project structure,What interviewers look for in junior backend candidates.

---------------------------------------------------------------------------------------------------------------------------

### Alembic 
#### Module 1: Why migrations exist (30–45 minutes)                        [01-07-26 -- 01-07-26]

#### Module 2: Initialize Alembic in our project                           [02-07-26 -- 02-07-26]
Install Alembic,Initialize Alembic,Project structure,alembic.ini,env.py,Connecting Alembic to SQLAlchemy

#### Module 3: Create, inspect, upgrade, and downgrade migrations          [02-07-26 -- 02-07-26]
revision --autogenerate,Migration files,upgrade,downgrade,alembic_version,Real development workflow

#### Module 4: Simulate real development                                   [02-07-26 -- 02-07-26]
Adding a column,Renaming a column,Creating a new table,Editing relationships,What Alembic can and cannot detect automatically

#### Module 5: Best practices and common mistakes                          [02-07-26 -- 02-07-26]


__________________________________________________________________________________________________________________________________


## Phase 4 —  FastAPI Fundamentals and REST APIs                                        [07-07-26 -- 12-07-26]
Duration: 1 week

Goal:
Learn:
* Introduction to FastAPI
* Routing & Path Operations
* Request Bodies & Pydantic
* Dependency Injection
* Error Handling
* Project Structure - add endpoints, Pagination, Filtering & Searching


### Module 1: Introduction to FastAPI                                      [07-07-26 -- 07-07-26]
Why web frameworks exist,Client vs Server,HTTP fundamentals,Request and Response,REST APIs (Introduction),JSON,Installing FastAPI,Uvicorn,First FastAPI application,Swagger UI,ReDoc,HTTP request lifecycle

### Module 2: Routing & Path Operations                                    [08-07-26 -- 08-07-26]
Why routing exists,What is a URL?,What is a Route?,Route decorators,HTTP Methods,Path Parameters,Query Parameters,Status Codes,How FastAPI matches requests internally,Production REST naming conventions

### Module 3: Request Bodies & Pydantic Models                            [09-07-26 -- 09-07-26]
Why request bodies exist,What is a request body?,Why dictionaries aren't enough,Introduction to Pydantic,Creating Pydantic models,Automatic validation,Serialization vs deserialization,Response models,Validation errors (422)

### Module 4: Dependency Injection                                        [09-07-26 -- 09-07-26]
What problem dependency injection solves,Why global database sessions are dangerous,What is a dependency?,Depends(),Database session lifecycle,Generator dependencies (yield),Reusing dependencies,Connecting FastAPI to your existing SQLAlchemy setup

### Module 5: Error Handling                                               [10-07-26 -- 10-07-26]
Why API error handling is different from Python exceptions,HTTP errors,HTTPException,Status codes,Returning meaningful error messages,The request lifecycle when an error occurs,Validation errors (422),Custom exception handlers,Global error handling

### Module 6: Project Structure - add endpoints                           [11-07-26 -- 12-07-26]
Why project structure matters,Separating routers, schemas, models, and database code,Creating routers,Including routers in main.py,Configuration,Environment variables,Refactoring your Blog CLI project into a production-style FastAPI project, Pagination, Filtering & Searching


__________________________________________________________________________________________________________________________________


## Phase 5 —  JWT Authentication                                            [12-07-26 -- 17-07-26]
Duration: 1 week

Goal:
Learn:
* Why Authentication Exists
* Password Security
* JWT
* Implement JWT Authentication
* Protecting Endpoints
* Authorization


### Module 1: Why Authentication Exists                                     [12-07-26 -- 12-07-26]
Authentication vs Authorization,Why REST APIs need authentication,Stateless vs Stateful authentication,Sessions,Cookies,Tokens,JWT (concept only),Complete request flow between frontend and backend

### Module 2: Password Security                                             [13-07-26 -- 13-07-26]
Why passwords should never be stored directly,Hashing,Salt,Why modern password hashing algorithms exist,bcrypt vs pwdlib,Password verification,Designing Register and Login endpoints,What happens internally during registration and login

### Module 3: JWT (JSON Web Token)                                          [14-07-26 -- 14-07-26]
What JWT is, JWT structure, Header, Payload, Signature, Encoding vs Encryption, Claims, Expiration, Secret Keys

### Module 4: Implementing JWT Authentication                               [15-07-26 -- 16-07-26]
Install the JWT library (python-jose or PyJWT—I'll explain why we'll choose one).,Create a SECRET_KEY.,Generate a JWT after successful login.,Return it from your /login endpoint.

### Module 5: Protecting Endpoints                                          [16-07-26 -- 17-07-26]
Learn how FastAPI's OAuth2PasswordBearer works,Use the JWT to identify the current user,OAuth2PasswordBearer,get_current_user(),/login,Protecting your POST /posts, PUT /posts/{id}, and DELETE /posts/{id} endpoints

### Module 6: Authorization                                                 [17-07-26 -- 17-07-26]
Ownership checks (current_user.id == post.user_id),Protect PUT /posts/{id},Protect DELETE /posts/{id},RBAC (Admin vs User),Permission patterns used in production


__________________________________________________________________________________________________________________________________


## Phase 6 —  Testing                                                       [17-07-26 -- 28-07-26]
Duration: 1 week

Goal:
Learn:
* Introduction to Testing
* Testing FastAPI
* Database Testing
* CRUD Testing
* Authentication & Authorization Testing
* Fixtures
* Mocking
* Advanced Testing
* Production Testing Best Practices 

### Module 1: Introduction to Testing                                      [18-07-26 -- 19-07-26]
Why testing exists,Types of testing,Unit vs Integration vs End-to-End tests,Why backend developers write tests,Testing pyramid,What should and shouldn't be tested,Installing pytest,Project setup,Writing the first test,Test discovery,Assertions

### Module 2: Testing FastAPI                                              [20-07-26 -- 20-07-26]
TestClient,Simulating HTTP requests,Testing GET endpoints,Testing POST endpoints,Testing PUT endpoints,Testing DELETE endpoints,Understanding request and response testing

### Module 3: Database Testing                                             [20-07-26 -- 22-07-26]
Why production databases should never be used for tests,Creating a separate test database,Test isolation,Transactions and rollback,Dependency overrides,Using SQLAlchemy sessions in tests,Fixtures,nested transactions,SAVEPOINTs

### Module 4: CRUD Testing                                                 [23-07-26 -- 25-07-26]
Testing User CRUD,Testing Post CRUD,Testing Comment CRUD,Verifying database changes,Testing invalid input,Testing missing resources

### Module 5: Authentication & Authorization Testing                       [26-07-26 -- 26-07-26]
Testing login,Testing JWT generation,Testing protected endpoints,Testing unauthorized requests,Testing forbidden requests,Ownership tests,Role-based authorization tests

### Module 6: Advanced Fixtures                                            [27-07-26 -- 27-07-26]
What fixtures are,Why fixtures exist,Reusable test setup,Database fixtures,Client fixtures,Authenticated user fixtures,Fixture scopes,conftest.py,Fixture Factories,Parametrized Fixtures

### Module 7: Mocking                                                      [28-07-26 -- 28-07-26]
Why mocking exists,When to mock,unittest.mock,Monkeypatch,Mocking external services,Mocking email sending,Mocking third-party APIs,Avoiding over-mocking,patch()

### Module 8: Advanced Testing                                             [28-07-26 -- 28-07-26]
Parameterized tests,Testing validation errors,Testing exceptions,Edge cases,Regression testing,Code coverage,Organizing large test suites, pytest --cov=app,Test markers (slow, skip, xfail),Property-based testing

### Module 9: Production Testing Best Practices                            [28-07-26 -- 28-07-26]
Test naming,Arrange-Act-Assert pattern,Clean test code,Common beginner mistakes,Common interview questions,CI-ready test structure,Testing strategy for junior backend developers


__________________________________________________________________________________________________________________________________


## Phase 7 —  Git & Github                                                 [01-08-26 -- 01-08-26]
Duration: 1 day

Goal: Relearn commands
Learn: [https://learngitbranching.js.org/]
* branch
* merge
* rebase
* checkout
* HEADS
* reset, revert 
* restore
* clone
* fetch
* pull

### Module 1: Git commands                                                [01-08-26 -- 01-08-26]
git branch new_branch_name, git checkout branch_name, git checkout -b new_branch_name[create and use]
git merge branch_name[merges to main], git rebase main[from current branch to main]
git checkout HEAD^[move a commit up], git checkout HEAD~2[move 2 commits up]
git reset HEAD^, git revert HEAD^
git restore --staged file_name: unstage a file (move it back out of the staging area, keeping your edits),
git restore file_name: discard your edits to a file entirely (careful, this throws the changes away!)

### Module 2: GitHub commands                                             [01-08-26 -- 01-08-26]
git clone, git fetch, git pull, git push, git pull --rebase


__________________________________________________________________________________________________________________________________



## Phase 8 —  Docker                                                      [02-08-26 -- 03-08-26]
Duration: 2 days

Goal:
Learn:
* Installation & Docker CLI Refresher
* Dockerizing the FastAPI Application
* Docker Volumes
* Docker Compose
* Docker Networking
* Alembic Inside Docker
* Development Workflow
* Debugging Docker
* Production Dockerfile

### Module 1: Installation & Docker CLI Refresher                        [02-08-26 -- 02-08-26]
docker pull, docker images, docker run IMAGE [docker run -d --name my-nginx -p 8080:80 nginx], docker ps -a, docker exec -it my-nginx sh

### Module 2: Dockerizing your FastAPI Blog API                          [02-08-26 -- 02-08-26]
Creating the Dockerfile,Choosing a base image,WORKDIR,COPY,RUN,Installing dependencies,EXPOSE,CMD,.dockerignore,
Building the image [docker build -t blog-api .]
Running the container [docker run -d --name blog-api-co -p 8000:8000 blog-api]

### Module 3: Docker Volumes                                             [02-08-26 -- 02-08-26]
Named volumes [docker volume create postgres_data],Bind mounts [docker run -d --name blog-api-co -p 8000:8000 -v ${PWD}:/app blog-api],
Persisting PostgreSQL data [docker run -d --name postgres -v postgres_data:/var/lib/postgresql/data postgres:17],
Mounting source code,Development workflow
 
### Module 4: Docker Compose                                             [03-08-26 -- 03-08-26]
docker-compose.yml,Services,Networks,Volumes,Environment variables,depends_on
docker compose up -d --build  
docker compose restart api
docker compose exec api sh

### Module 5: Docker Networking                                          [03-08-26 -- 03-08-26]
Bridge networks,Container communication,Service names,Port mapping,FastAPI ↔ PostgreSQL communication
docker network ls, docker network inspect project_name_default

### Module 6: Alembic Inside Docker                                      [03-08-26 -- 03-08-26]
Running migrations, Running management commands, docker compose exec, docker compose run, Startup order, Database readiness
docker compose exec api alembic upgrade head
docker compose exec api alembic revision --autogenerate -m "Add categories"
docker compose exec api python -m pytest

### Module 7: Development Workflow                                       [03-08-26 -- 03-08-26]
Live reload, Mounting source code, Rebuilding images, Container lifecycle, Useful Docker commands during development

### Module 8: Debugging Docker                                           [03-08-26 -- 03-08-26]
docker logs my-nginx, docker inspect my-nginx
docker compose build --no-cache

### Module 9: Production Dockerfile                                      [03-08-26 -- 03-08-26]
Multi-stage builds, Image optimisation, Security best practices, Non-root users, Environment variables, Health checks, Production CMD


__________________________________________________________________________________________________________________________________



## Phase 9 —  Github Actions (CI/CD)                                     [04-08-26 -- 05-08-26]
Duration: 2 days

Goal:
Learn:
* CI/CD Fundamentals
* GitHub Actions Fundamentals
* Running Tests Automatically
* Secrets & Environment Variables
* Docker Automation
* Simple Deployment Pipeline
* Debugging Workflows


### Module 1: CI/CD Fundamentals                                          [04-08-26 -- 04-08-26]
What Continuous Integration is, What Continuous Deployment is, What Continuous Delivery is, Why automation exists, Manual vs automated workflows, Typical backend development workflow

### Module 2: GitHub Actions Fundamentals                                 [04-08-26 -- 04-08-26]
Workflow files[.github/workflows/], Events (push, pull_request, workflow_dispatch), Jobs, Steps, Runners, GitHub-hosted runners, Basic YAML structure, How a workflow executes internally

### Module 3: Running Tests Automatically                                 [04-08-26 -- 04-08-26]
Setting up Python, Installing dependencies, Running Pytest, Viewing workflow logs, Failing builds, Status badges

### Module 4: Secrets & Environment Variables                             [04-08-26 -- 04-08-26]
GitHub Secrets, Environment variables, Why secrets should never be committed, Passing secrets to workflows, Common security mistakes

### Module 5: Docker Automation                                           [05-08-26 -- 05-08-26]
Building Docker images, Running Docker inside GitHub Actions, Image tagging, Docker Hub (high level), GitHub Container Registry (overview)

### Module 6: Simple Deployment Pipeline                                  [05-08-26 -- 05-08-26]
What deployment automation is, Basic deployment workflow, Deploying to an EC2 server (high level), SSH deployment (simple example), Rolling back failed deployments (concept)

### Module 7: Debugging Workflows                                         [05-08-26 -- 05-08-26]
Reading workflow logs, Common YAML mistakes, Dependency installation failures, Missing secrets, Permission errors, Typical CI failures

### Module 8: Interview Preparation                                       [05-08-26 -- 05-08-26]
Common GitHub Actions interview questions, CI/CD terminology, Explaining your own workflow, Reviewing a sample workflow, Scenario-based questions


__________________________________________________________________________________________________________________________________


 
## Phase 10 —  AWS basics                                                  [07-08-26]
Duration: 3 days

Goal:
Learn:
* Understanding AWS & Cloud Foundations
* EC2, Networking & IAM
* Deploying Our FastAPI Blog API
* Databases, Storage & Monitoring
* Production Architecture & AWS Ecosystem
* Deployment Review, Troubleshooting & Interview Preparation


### Module 1: Understanding AWS & Cloud Foundations                        [07-08-26 -- 07-08-26]
What Cloud Computing Actually Is, What AWS Actually Is, Global Infrastructure, Shared Responsibility Model, Core AWS Services Overview, AWS Pricing Basics, How Our Blog API Fits Into AWS

### Module 2: EC2, IAM, Networking & Security                             [08-08-26 -- 08-08-26]
EC2, Storage, Networking Basics, Security Groups, IAM, Principle of Least Privilege, Launching Our First EC2        
