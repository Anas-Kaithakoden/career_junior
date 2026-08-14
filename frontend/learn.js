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
