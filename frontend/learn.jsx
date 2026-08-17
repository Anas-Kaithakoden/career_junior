
function Navbar({ isLoggedIn }) {
    return (
        <nav>
            {isLoggedIn ? <button>Logout</button> : <button>Login</button>}
        </nav>
    );
}


function Welcome() {
    return <h1>Welcome</h1>
}

function Intro() {
    const name = "Anas";
    const role = "Backend Developer";
    return (<div>
                <h1>Hello {name} </h1>
                <p>You are a {role}</p>
            </div>
        );
}

function PostCard({ post }) {
    return (
        <div>
            <h2>{post.title}</h2>
            <p>{post.content}</p>
        </div>
    );
}

const posts = [
    {
        id: 1,
        title: "Docker Basics",
        content: "Learning Docker"
    },
    {
        id: 2,
        title: "FastAPI",
        content: "Building APIs"
    }
];
function PostList({ posts }){

    return (
        <section>
            {posts.map(post => (
                <PostCard
                    key={post.id}
                    post={post}
                />
            ))}
        </section>
    );
}


function ClickButton(){
    function handleClick() {
        console.log("button clicked")
    }

    return (
        <button onClick={handleClick}>
            Click Me
        </button>
    )
}

function App() {
    return (
        <>  
            <Navbar isLoggedIn={true} />
            <Welcome />
            <Intro />
            <PostList posts={posts} />
            <ClickButton />
        </>
    );
}

export default App;
