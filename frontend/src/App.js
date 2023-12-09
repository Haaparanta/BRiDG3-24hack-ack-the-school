import React, { useState, useEffect } from "react";
import logoYellow from "./images/logo-yellow.png";
import logoRed from "./images/logo-red.png";
import "./App.css";

function App() {
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [isSection1Started, setIsSection1Started] = useState([
    false,
    false,
    false,
    false,
  ]);
  const [progress, setProgress] = useState([0, 0, 0, 0]);
  const [showTextArea2, setShowTextArea2] = useState(false);
  const [showTextArea3, setShowTextArea3] = useState(false);
  const [textAreaContent2, setTextAreaContent2] = useState("");
  const [textAreaContent3, setTextAreaContent3] = useState("");
  const [section2Content, setSection2Content] = useState("");
  const [section3Content, setSection3Content] = useState("");
  const [theme, setTheme] = useState("angel");

  const handleSubmit = (event) => {
    event.preventDefault();
    setIsSubmitted(true);
  };

  useEffect(() => {
    // Fetch section2.txt
    fetch("/section2.txt")
      .then((response) => response.text())
      .then((text) => setSection2Content(text));

    // Fetch section3.txt
    fetch("/section3.txt")
      .then((response) => response.text())
      .then((text) => setSection3Content(text));
  }, []);

  const startProgress = (index) => {
    setIsSection1Started(
      isSection1Started.map((item, idx) => (idx === index ? true : item))
    );
    const interval = setInterval(() => {
      setProgress((progress) =>
        progress.map((prog, idx) =>
          idx === index ? Math.min(prog + 100 / 120, 100) : prog
        )
      );
    }, 1000);
    setTimeout(() => clearInterval(interval), 120 * 1000);
  };

  useEffect(() => {
    let interval2;
    let interval3;
    if (showTextArea2) {
      const sentences2 = section2Content.split(". ");
      interval2 = setInterval(() => {
        setTextAreaContent2(
          (text) => text + (text ? " " : "") + sentences2.shift()
        );
        if (!sentences2.length) clearInterval(interval2);
      }, 3000);
    }
    if (showTextArea3) {
      const sentences3 = section3Content.split(". ");
      interval3 = setInterval(() => {
        setTextAreaContent3(
          (text) => text + (text ? " " : "") + sentences3.shift()
        );
        if (!sentences3.length) clearInterval(interval3);
      }, 3000);
    }
    return () => {
      clearInterval(interval2);
      clearInterval(interval3);
    };
  }, [section2Content, section3Content,textAreaContent2, textAreaContent3, showTextArea2, showTextArea3]);

  const switchTheme = (newTheme) => {
    setTheme(newTheme);
  };

  // Apply theme-based styles
  const themeStyles =
    theme === "angel"
      ? {
          backgroundColor: "#C5EFF6", // Light blue
          color: "#EEB720", // Yellow
        }
      : {
          backgroundColor: "#1C1C1C", // Black
          color: "#E60100", // Red
        };

  // If the form has been submitted, render a different view
  if (isSubmitted) {
    return (
      <div
        className="App"
        style={{
          ...themeStyles,
          height: "100vh",
          width: "100vw",
          overflow: "hidden",
        }}
      >
        <header>
          <img
            src={theme === "angel" ? logoYellow : logoRed}
            alt="logo"
            className="App-logo"
          />
          <h1>Title of the Page</h1>
        </header>

        {/* ... (Your existing content for the submitted view) */}
        <div>
          {[...Array(4).keys()].map((index) => (
            <div key={index}>
              <button onClick={() => startProgress(index)}>
                Start {index + 1}
              </button>
              <div>Progress: {progress[index]}%</div>
            </div>
          ))}
        </div>
        {/* Section 2 */}
        <div>
          {/* Section 2 */}
          <div className="section">
            <button onClick={() => setShowTextArea2(true)}>
              Start Section 2
            </button>
            {showTextArea2 && (
              <textarea
                className="section-textarea"
                value={textAreaContent2}
                readOnly
              />
            )}
          </div>
        </div>
        {/* Section 3 */}
        <div>
          <div className="section">
            <button onClick={() => setShowTextArea3(true)}>
              Start Section 3
            </button>
            {showTextArea2 && (
              <textarea
                className="section-textarea"
                value={textAreaContent3}
                readOnly
              />
            )}
          </div>
        </div>

        <footer>
          <p>The Purgers© {new Date().getFullYear()}</p>
          <p>https://eu.junctionplatform.com/dashboard/event/24hack</p>
          <p>https://github.com/Haaparanta/BRiDG3-24hack-ack-the-school</p>
        </footer>

        <select
          onChange={(e) => switchTheme(e.target.value)}
          style={{ position: "absolute", top: 10, right: 10 }}
        >
          <option value="angel">Angel</option>
          <option value="devil">Devil</option>
        </select>
      </div>
    );
  }

  console.log("rendering default view");
  // Default view with the form
  return (
    <div
      className="App"
      style={{
        ...themeStyles,
        height: "100vh",
        width: "100vw",
        overflow: "hidden",
      }}
    >
      <header>
        <img
          src={theme === "angel" ? logoYellow : logoRed}
          alt="logo"
          className="App-logo"
        />
        <h1>Title of the Page</h1>
      </header>

      <form onSubmit={handleSubmit}>
        <div>
          <label>Email:</label>
          <input type="text" name="email" placeholder="Insert email" />
        </div>

        <div>
          <label>Password:</label>
          <input
            type="password"
            name="password"
            placeholder="Insert password"
          />
        </div>

        <div>
          <label>URL:</label>
          <input type="text" name="url" placeholder="https://moodle.tuni.fi/course/view.php?id=37071" />
        </div>

        <div>
          <label>Pick a side:</label>
          <select name="side">
            <option value="angel">Angel</option>
            <option value="devil">Devil</option>
          </select>
        </div>
        <button type="submit">Submit</button>
      </form>

      <footer>
        <p>The Purgers© {new Date().getFullYear()}</p>
        <p>https://eu.junctionplatform.com/dashboard/event/24hack</p>
        <p>https://github.com/Haaparanta/BRiDG3-24hack-ack-the-school</p>
      </footer>

      <select
        onChange={(e) => switchTheme(e.target.value)}
        style={{ position: "absolute", top: 10, right: 10 }}
      >
        <option value="angel">Angel</option>
        <option value="devil">Devil</option>
      </select>
    </div>
  );
}

export default App;
