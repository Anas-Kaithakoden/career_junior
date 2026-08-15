const title = document.getElementById("title");
title.textContent = "New title";
console.log(title);

const button = document.querySelector("#button");
button.addEventListener("click", () => 
    {console.log("Button clicked");
     title.textContent ="Button clicked";
});

const postContainer = document.querySelector("#paragraphs")
const post = document.createElement("p");
post.textContent = "Hello new added"
postContainer.appendChild(post);


// Exercises 

const element = document.querySelector("#title")
element.textContent = "Anas's Tech Blog"

const button = document.querySelector("#button");
button.addEventListener("click", () => 
    {
     element.textContent = "Button clicked";
});

const button = document.querySelector("#button");
const para = document.querySelector("#message");
button.addEventListener("click", () => 
    {
     para.classList.remove("hidden")
     para.classList.add("active")
});

const form = document.querySelector("#loginForm");
form.addEventListener("submit", (event) => 
    {
    event.preventDefault();

    const password = document.querySelector("#password").value;
    const email = document.querySelector("#email").value;
    console.log(password);
    console.log(email);
});

const posts = [
    {
        id: 1,
        title: "Docker Basics",
        author: "Anas",
        published: true
    },
    {
        id: 2,
        title: "FastAPI Authentication",
        author: "Ali",
        published: false
    },
    {
        id: 3,
        title: "Deploying to AWS",
        author: "Anas",
        published: true
    }
];
const postContainer = document.querySelector("#posts");
posts.forEach(post => {
    const p = document.createElement("p");
    p.textContent = post.title;
    postContainer.appendChild(p);
});
