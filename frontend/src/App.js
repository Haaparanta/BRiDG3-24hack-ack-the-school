import React, { useState, useEffect } from 'react';
import logoYellow from './images/logo-yellow.png';
import logoRed from './images/logo-red.png';
import './App.css';

/* Color palette
(yellow) EEB720 
(Light blue) C5EFF6
(White) FDFBFA
(Red) E60100
(Black) 1C1C1C

if side is angel use light theme (yellow, light blue, white)
if side is devil use dark theme (red, black, white)

Make it so that when the form is submitted, the page changes to a different view
Add angel and devil selector to both pages. If angel is selected, use light theme, if devil is selected, use dark theme. Selector should be right top corner
Make page 100vh and 100vw so no scrolling avaible. Make it responsive so that it works on mobile as well
Add margins and paddings to make it look nice and clean. Content should be at center 50% width and 80% height 
Add a header with the logo and the title of the page
Add a footer with the name of the company and the year
*/

function App() {
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [isSection1Started, setIsSection1Started] = useState([false, false, false, false]);
  const [progress, setProgress] = useState([0, 0, 0, 0]);
  const [showTextArea2, setShowTextArea2] = useState(false);
  const [showTextArea3, setShowTextArea3] = useState(false);
  const [textAreaContent2, setTextAreaContent2] = useState('');
  const [textAreaContent3, setTextAreaContent3] = useState('');
  const [section2Content, setSection2Content] = useState('');
  const [section3Content, setSection3Content] = useState('');


  const handleSubmit = (event) => {
    event.preventDefault(); // Prevent default form submission behavior
    setIsSubmitted(true);  // Change state to indicate form is submitted
  };

  useEffect(() => {
    // Fetch section2.txt
    fetch('/section2.txt')
      .then(response => response.text())
      .then(text => setSection2Content(text));

    // Fetch section3.txt
    fetch('/section3.txt')
      .then(response => response.text())
      .then(text => setSection3Content(text));
  }, []);

  const startProgress = (index) => {
    setIsSection1Started(isSection1Started.map((item, idx) => (idx === index ? true : item)));
    const interval = setInterval(() => {
      setProgress(progress => progress.map((prog, idx) => idx === index ? Math.min(prog + 100 / 120, 100) : prog));
    }, 1000);
    setTimeout(() => clearInterval(interval), 120 * 1000);
  };

  useEffect(() => {
    let interval2;
    let interval3;
    if (showTextArea2) {
      const sentences2 = section2Content.split(". ");
      interval2 = setInterval(() => {
        setTextAreaContent2(text => text + (text ? " " : "") + sentences2.shift());
        if (!sentences2.length) clearInterval(interval2);
      }, 30000);
    }
    if (showTextArea3) {
      const sentences3 = section3Content.split(". ");
      interval3 = setInterval(() => {
        setTextAreaContent3(text => text + (text ? " " : "") + sentences3.shift());
        if (!sentences3.length) clearInterval(interval3);
      }, 30000);
    }
    return () => {
      clearInterval(interval2);
      clearInterval(interval3);
    };
  }, [section2Content, section3Content, showTextArea2, showTextArea3]);

  // If the form has been submitted, render a different view
  if (isSubmitted) {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logoRed} className="App-logo" alt="logo" />
          {/* Section 1 */}
          <div>
            {[...Array(4).keys()].map((index) => (
              <div key={index}>
                <button onClick={() => startProgress(index)}>Start {index + 1}</button>
                <div>Progress: {progress[index]}%</div>
              </div>
            ))}
          </div>
          {/* Section 2 */}
          <div>
            <h2>Section 2</h2>
            <button onClick={() => setShowTextArea2(true)}>Start Section 2</button>
            {showTextArea2 && <textarea value={textAreaContent2} readOnly />}
          </div>
          {/* Section 3 */}
          <div>
            <h2>Section 3</h2>
            <button onClick={() => setShowTextArea3(true)}>Start Section 3</button>
            {showTextArea3 && <textarea value={textAreaContent3} readOnly />}
          </div>
        </header>
      </div>
    );
  }

  // Default view with the form
  return (
    <div className="App">
      <header className="App-header">
        <img src={logoYellow} className="App-logo" alt="logo" />
        <form onSubmit={handleSubmit}>
            <div>
              <label>Email:</label>
              <input type="text" name="email" placeholder="Insert email" />
            </div>

            <div>
              <label>Password:</label>
              <input type="password" name="password" placeholder="Insert password" />
            </div>

            <div>
              <label>URL:</label>
              <input type="text" name="url"  placeholder="Insert URL" />
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
      </header>
    </div>
  );
}

export default App;