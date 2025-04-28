import React, { useState } from 'react';
import API from '../api/api';

const UploadVoice = () => {
  const [file, setFile] = useState(null);

  const handleUpload = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', file);

    try {
      await API.post('/voice/upload', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      alert('Voice file uploaded successfully!');
    } catch (error) {
      alert('Upload failed!');
      console.error(error);
    }
  };

  return (
    <div>
      <h2>Upload Voice</h2>
      <form onSubmit={handleUpload}>
        <input type="file" accept="audio/*" onChange={(e) => setFile(e.target.files[0])} required />
        <button type="submit">Upload</button>
      </form>
    </div>
  );
};

export default UploadVoice;

