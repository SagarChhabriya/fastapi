## What is an API?

API stands for **Application Programming Interface**.
It is a way for two software programs to communicate with each other.

For example, just like a **menu in a restaurant** tells you what dishes you can order, an API tells you what functions or data a software system provides.
You (the client) make a request, and the API (the server) gives a response.

---

## What is a Web API?

A **Web API** is an API that can be accessed over the **internet** using the **HTTP protocol**.

It allows:

* Web applications to talk to servers
* Mobile apps to fetch and send data
* Backend systems to interact with one another

---

## What is a RESTful API?

REST stands for **Representational State Transfer**. It is a set of principles for designing APIs that work over the web.

RESTful APIs:

* Use **HTTP methods** such as GET, POST, PUT, DELETE
* Are **stateless**: each request is independent and contains all the information needed
* Use **URLs** to refer to resources (e.g., `/users`, `/products/1`)
* Typically return **JSON**-formatted data

---

### REST in Action

Example: An API for managing a product catalog

| Action           | HTTP Method | URL           | Description                   |
| ---------------- | ----------- | ------------- | ----------------------------- |
| Get all products | GET         | `/products`   | Fetch a list of products      |
| Get one product  | GET         | `/products/1` | Fetch product with ID = 1     |
| Create product   | POST        | `/products`   | Send new product data         |
| Update product   | PUT         | `/products/1` | Replace product with new data |
| Delete product   | DELETE      | `/products/1` | Remove product from the list  |

---

## Other Types of APIs (Besides REST)

In addition to REST, modern developers also use other styles of APIs depending on performance needs, system design, or use case.

---

### 1. GraphQL

* Created by Facebook
* Uses a **single endpoint** (typically `/graphql`)
* Clients **request exactly the data they need**
* Useful for avoiding over-fetching or under-fetching of data

**Pros**: Highly flexible, efficient
**Cons**: More complex to implement and secure

---

### 2. gRPC (Google Remote Procedure Call)

* Created by Google
* Uses **HTTP/2** and Protocol Buffers (protobuf) for communication
* Sends **binary-encoded** data rather than JSON or XML
* Ideal for microservices and high-performance APIs

**Pros**: Very fast, strongly typed
**Cons**: Not human-readable, less browser-friendly

---

### 3. SOAP (Simple Object Access Protocol)

* XML-based protocol used primarily in older or enterprise systems
* Includes **strict schemas** and strong security features
* Highly structured but heavy and verbose

**Pros**: Secure, well-defined
**Cons**: Verbose, harder to work with compared to REST

---

### 4. WebSockets

* Not an API style but a **protocol** used for **real-time communication**
* Maintains an open connection between the client and server
* Commonly used in **chat apps**, **games**, and **live dashboards**

**Pros**: Bi-directional, real-time communication
**Cons**: Not suitable for standard request-response interactions

---

## REST vs Other API Types

| Feature           | REST     | GraphQL | gRPC      | SOAP     | WebSockets |
| ----------------- | -------- | ------- | --------- | -------- | ---------- |
| Data Format       | JSON     | JSON    | Protobuf  | XML      | Custom     |
| Endpoint Usage    | Multiple | Single  | Single    | Multiple | Single     |
| Real-time Capable | No       | No      | Partial   | No       | Yes        |
| Performance       | Good     | Good    | Excellent | Low      | Excellent  |
| Learning Curve    | Easy     | Medium  | Hard      | Hard     | Medium     |

---

## Teaching Notes

* Start with REST because it is beginner-friendly and commonly used in industry
* Use visual examples such as URL endpoints and HTTP verbs to show how RESTful APIs work
* Introduce Swagger (OpenAPI documentation) early to show instant results
* Keep data in memory for now to avoid setting up databases too early
* Compare REST to other styles later once students are confident

---

## In Short

* An **API** is a way for programs to talk to each other.
* A **Web API** is accessed over the internet, usually using HTTP.
* A **RESTful API** uses URLs and HTTP methods to retrieve and manipulate resources.
* **FastAPI** is a Python framework that helps you build RESTful APIs quickly and safely.
* Other API styles such as **GraphQL**, **gRPC**, **SOAP**, and **WebSockets** exist and are useful in specific scenarios.
