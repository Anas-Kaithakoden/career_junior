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

const firstTitle = posts[0].title ;

const title = posts.map(post => post.title);

const publishedPosts = posts.filter(post => post.published);

const activePosts = posts
.filter(post => post.published)
.map(post => post.title);


const postsNew = [
    { id: 1, title: "Docker" },
    { id: 2, title: "FastAPI" },
    { id: 3, title: "AWS" }
];

const getPostTitles = posts => posts.map(post => post.title);



// Frontend <-> backend

async function getUsers() {
    const response = await fetch("http://localhost:8000/users");
    const data = await response.json();
    console.log(data);
    
}


const user_payload = {
    name: "Anas new",
    email: "anas657@gmail.com",
    phone: "678904",
    password: "string"
};
async function createUser() {
    const response = await fetch("http://localhost:8000/users", {
        method: "POST",
        headers: {
            "Content-Type" : "application/json"
        },
        body: JSON.stringify(user_payload)
    });
    const data = await response.json();
    
}


// Authentication + JWT + CORS 

const button = document.querySelector("#button");
button.addEventListener("click", async () => 
    {
     await login();
     await createPost();
});

const login_payload = {
    email: "anas657@gmail.com",
    password: "string"
};
async function login() {
    const response = await fetch("http://localhost:8000/login", {
        method: "POST",
        headers: {
            "Content-Type" : "application/json"
        },
        body: JSON.stringify(login_payload)
    });
    const data = await response.json();
    const token = data.access_token;
    console.log(token);
    localStorage.setItem("access_token", token);
}

const post_payload = {
  "title": "strirng",
  "content": "stringneww",
  "published": true
}
async function createPost() {
    const token = localStorage.getItem("access_token");
    const response = await fetch("http://localhost:8000/posts", {
        method: "POST",
        headers: {
            "Content-Type" : "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify(post_payload)
    });
    const data = await response.json();
    console.log(data);
    
}
