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

console.log(activePosts);

const postsNew = [
    { id: 1, title: "Docker" },
    { id: 2, title: "FastAPI" },
    { id: 3, title: "AWS" }
];

const getPostTitles = posts => posts.map(post => post.title);

console.log(getPostTitles(postsNew));


// Frontend <-> backend

async function getUsers() {
    const response = await fetch("http://localhost:8000/users");
    const data = await response.json();
    console.log(data);
    
}
getUsers();

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
    console.log(data);
    
}
createUser();
