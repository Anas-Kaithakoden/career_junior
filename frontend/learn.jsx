
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

import { useState, useEffect } from "react";

function Counter(){
    const [count, setCount] = useState(0);

    function handleIncrement() {
        setCount(prevCount => prevCount + 1);
    }

    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={handleIncrement}>Increment</button>
        </div>
    );
}

function NameForm(){
  const [name, setName] = useState("");

  return (
    <div>
      <label>
        Name:
        <input 
          value={name}
          onChange={event => setName(event.target.value)}
        />
      </label>

      <p>Hello, {name}</p>
    </div>
  );
}

function LoginForm(){
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

    function handleSubmit(event) {
        event.preventDefault();

        console.log("Email:", email);
        console.log("Password:", password);

        setLoading(true);

        setTimeout(() => {
            setLoading(false);
        }, 2000);
    }

  return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>
                    Email:
                    <input
                        type="email"
                        value={email}
                        onChange={event => setEmail(event.target.value)}
                    />
                </label>
            </div>

            <div>
                <label>
                    Password:
                    <input
                        type="password"
                        value={password}
                        onChange={event => setPassword(event.target.value)}
                    />
                </label>
            </div>

            <button type="submit" disabled={loading}>
                {loading ? "Logging in..." : "Login"}
            </button>

            {error && <p>{error}</p>}
        </form>
    );
}

function PostList() {
    const [posts, setPosts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        async function fetchPosts() {
            try {
                const response = await fetch("http://localhost:8000/posts");

                if (!response.ok) {
                    throw new Error("Failed to fetch posts");
                }

                const data = await response.json();
                setPosts(data);
            } catch (error) {
                setError(error.message);
            } finally {
                setLoading(false);
            }
        }

        fetchPosts();
    }, []);

    if (loading) {
        return <p>Loading...</p>;
    }

    if (error) {
        return <p>{error}</p>;
    }

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

function App() {
    return (
        <>  
            <Navbar isLoggedIn={true} />
            <Welcome />
            <Intro />
            <PostList posts={posts} />
            <ClickButton />
            <Counter/>
            <NameForm/>
            <LoginForm/>
        </>
    );
}

export default App;


