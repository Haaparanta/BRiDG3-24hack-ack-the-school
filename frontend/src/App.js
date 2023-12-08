import React, { useState } from 'react';
import logo from './images/frontpage.jpg'; // Update the path to your image if needed
import './App.css';

function App() {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    url: '',
    side: 'angel',
  });

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      // Send a POST request to the backend API endpoint
      const response = await fetch('https://example.com/api/form-submit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      // Handle the response from the backend
      if (response.ok) {
        console.log('Form submitted successfully');
        // You might handle success in some way, e.g., show a success message

        // If the URL field is not empty, render a different page
        if (formData.url) {
          // Check if the URL is valid (you can use a regex or any validation method)
          const isValidUrl = true; // Replace this with your URL validation logic

          if (isValidUrl) {
            return (
              <div>
                {/* Your new-looking site */}
                <h1>New Looking Site</h1>
                {/* Add additional content here */}
              </div>
            );
          }
        }
      } else {
        console.error('Form submission failed');
        // You might handle failure in some way, e.g., show an error message
      }
    } catch (error) {
      console.error('An error occurred:', error);
    }

    // ADD HERE THE IF(FORMDATAURL)

    // If no special condition is met, render the default form
    return (
      <div className="App">
        <header className="App-header">
          {/* Display your image */}
          <img src={logo} className="App-logo" alt="logo" />

          {/* Labels and input fields */}
          <form onSubmit={handleSubmit}>
            <div>
              <label>Email:</label>
              <input type="text" name="email" value={formData.email} onChange={handleChange} placeholder="Insert email" />
            </div>

            <div>
              <label>Password:</label>
              <input type="password" name="password" value={formData.password} onChange={handleChange} placeholder="Insert password" />
            </div>

            <div>
              <label>URL:</label>
              <input type="text" name="url" value={formData.url} onChange={handleChange} placeholder="Insert URL" />
            </div>

            <div>
              <label>Pick a side:</label>
              <select name="side" value={formData.side} onChange={handleChange}>
                <option value="angel">Angel</option>
                <option value="devil">Devil</option>
              </select>
            </div>

            {/* Additional content or form elements can be added here */}

            {/* Example button to submit the form */}
            <button type="submit">Submit</button>
          </form>
        </header>
      </div>
    );
  }

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  return renderForm();
}

export default App;