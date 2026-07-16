# Hello World
So i will be recording my python junior developer journey here 
I wish to learn
- Python
- PostgreSQL/SQL
- SQLAlchemy + Alembic
- FastAPI
- REST API
- JWT Authentication
- Testing
- Git & Github
- Docker
- AWS basics
- Github Actions
- Javascript
- React
- Redis
- MongoDB
- Pinecone
- LangChain
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

### Module 2 — Error Handling                                                   [19-06-26 -- 19-06-26]
Learn:
try,except,else,finally,raising exceptions

### Module 3: Collections & Comprehensions                                      [20-06-26 -- 20-06-26]
Learn:
Lists,Tuples,Dictionaries,Sets,List comprehensions,Dictionary comprehensions

### Module 4: Classes & OOP                                                     [21-06-26 -- 21-06-26]
Learn:Classes,Objects,Constructors,Methods,Attributes,Encapsulation,Inheritance,Polymorphism 

### Module 5 — Modules & Packages                                               [22-06-26 -- 22-06-26]
Learn:Importing,Creating modules,Creating packages,__init__.py

### Module 6 — File Handling & JSON                                             [22-06-26 -- 22-06-26]
Learn:Reading files,Writing files,JSON loading,JSON saving

### Module 7: Type Hints                                                        [22-06-26 -- 22-06-26]
Learn:Function annotations,typing module,Optional,List,Dict

### Module 8 — Generators                                                       [22-06-26 -- 22-06-26]
Learn:yield,Generator functions,Generator expressions

### Module 9 — Decorators                                                       [22-06-26 -- 22-06-26]
Learn:Functions as objects,Wrapper functions,Basic decorators

### Module 10 — Virtual Environments                                            [22-06-26 -- 22-06-26]
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

### Module 3 — CRUD Operations                                                   [24-06-26 -- 25-06-26]
Create, Read, Update, Delete

### Module 4 — Primary Keys & Foreign Keys                                       [26-06-26 -- 26-06-26]
Foreign Key Constraint, Relationship Types

### Module 5 — Filtering Data                                                    [26-06-26 -- 26-06-26]
WHERE, AND, OR, IN, BETWEEN, LIKE, IS NULL

### Module 6 — Sorting & Limiting                                                [26-06-26 -- 26-06-26]
ORDER BY, LIMIT, OFFSET                  

### Module 7 — JOINs                                                              [26-06-26 -- 26-06-26]
INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN

### Module 8 — Aggregation                                                       [26-06-26 -- 26-06-26]
COUNT,SUM,AVG,MIN,MAX,GROUP BY,HAVING

### Module 9 — Constraints, Indexes & Transactions                               [26-06-26 -- 26-06-26]
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

### Module 2 — SQLAlchemy Architecture                                    [27-06-26 -- 27-06-26]
Installing SQLAlchemy,Engine,Database URL,Base class,Sessions,How SQLAlchemy connects to PostgreSQL

### Module 3 — Models                                                     [28-06-26 -- 28-06-26]
Models,__tablename__,Mapped,mapped_column(),Column types,Primary Keys,Foreign Keys,Constraints,How a Python class becomes a PostgreSQL table

### Module 4 — Relationships                                              [29-06-26 -- 29-06-26]
Why relationship() exists,One-to-Many,back_populates,One-to-One,Many-to-Many

### Module 5 — CRUD with SQLAlchemy                                       [30-06-26 -- 30-06-26]
Create,Read,Update,Delete

### Module 6 — Querying with SQLAlchemy                                   [01-07-26 -- 01-07-26]
where(),Multiple conditions (AND, OR),order_by(),limit(),offset(),Joins,Aggregation (COUNT, SUM, AVG, ...),group_by(),having()

### Module 7 — Session Management                                          [01-07-26 -- 01-07-26]
Session lifecycle,commit(),rollback(),flush(),refresh(),expire(),Identity Map

### Module 8 — Loading Strategies                                         [01-07-26 -- 01-07-26]
Lazy Loading,Eager Loading,joinedload(),selectinload(),The N+1 Query Problem

### Module 9 — Production Best Practices                                  [01-07-26 -- 01-07-26]
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

### Module 3 — Request Bodies & Pydantic Models                            [09-07-26 -- 09-07-26]
Why request bodies exist,What is a request body?,Why dictionaries aren't enough,Introduction to Pydantic,Creating Pydantic models,Automatic validation,Serialization vs deserialization,Response models,Validation errors (422)

### Module 4 — Dependency Injection                                        [09-07-26 -- 09-07-26]
What problem dependency injection solves,Why global database sessions are dangerous,What is a dependency?,Depends(),Database session lifecycle,Generator dependencies (yield),Reusing dependencies,Connecting FastAPI to your existing SQLAlchemy setup

### Module 5: Error Handling                                               [10-07-26 -- 10-07-26]
Why API error handling is different from Python exceptions,HTTP errors,HTTPException,Status codes,Returning meaningful error messages,The request lifecycle when an error occurs,Validation errors (422),Custom exception handlers,Global error handling

### Module 6 — Project Structure - add endpoints                           [11-07-26 -- 12-07-26]
Why project structure matters,Separating routers, schemas, models, and database code,Creating routers,Including routers in main.py,Configuration,Environment variables,Refactoring your Blog CLI project into a production-style FastAPI project, Pagination, Filtering & Searching


__________________________________________________________________________________________________________________________________


## Phase 5 —  JWT Authentication                                            [12-07-26]
Duration: 1 week

Goal:
Learn:
* Why Authentication Exists
* Password Security
* JWT
* Implement JWT Authentication
* Protecting Endpoints
* Authorization
* Production Best Practices


### Module 1: Why Authentication Exists                                     [12-07-26 -- 12-07-26]
Authentication vs Authorization,Why REST APIs need authentication,Stateless vs Stateful authentication,Sessions,Cookies,Tokens,JWT (concept only),Complete request flow between frontend and backend

### Module 2 — Password Security                                            [13-07-26 -- 13-07-26]
Why passwords should never be stored directly,Hashing,Salt,Why modern password hashing algorithms exist,bcrypt vs pwdlib,Password verification,Designing Register and Login endpoints,What happens internally during registration and login

### Module 3 — JWT (JSON Web Token)                                         [14-07-26 -- 14-07-26]
What JWT is, JWT structure, Header, Payload, Signature, Encoding vs Encryption, Claims, Expiration, Secret Keys

### Module 4 — Implementing JWT Authentication                              [15-07-26 -- 16-07-26]
Install the JWT library (python-jose or PyJWT—I'll explain why we'll choose one).,Create a SECRET_KEY.,Generate a JWT after successful login.,Return it from your /login endpoint.

### Module 5.1 — Protecting Endpoints                                       [16-07-26 -- 17-07-26]
Learn how FastAPI's OAuth2PasswordBearer works,Use the JWT to identify the current user,OAuth2PasswordBearer,get_current_user(),/login,Protecting your POST /posts, PUT /posts/{id}, and DELETE /posts/{id} endpoints
