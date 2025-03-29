
import React, { useState } from 'react';

export function Dashboard({ user }) {
  const [url, setUrl] = useState('');

  const handleDownload = () => {
    fetch('http://localhost:8000/download/', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${user.access_token}`,
      },
      body: JSON.stringify({ url }),
    }).then((response) => response.json())
      .then((data) => alert(data.message));
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Paste link here"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
      />
      <button onClick={handleDownload}>Start Download</button>
    </div>
  );
}
    