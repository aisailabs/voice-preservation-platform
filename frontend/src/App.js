import React from 'react';
import Register from './components/Register';
import Login from './components/Login';
import UploadVoice from './components/UploadVoice';

function App() {
  return (
    <div>
      <h1>Voice Preservation Platform</h1>
      <Register />
      <Login />
      <UploadVoice />
    </div>
  );
}

export default App;

