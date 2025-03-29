
export const api = {
  login: async (username, password) => {
    const response = await fetch('http://localhost:8000/token', {
      method: 'POST',
      body: JSON.stringify({ username, password }),
    });
    return response.json();
  },

  download: async (url, token) => {
    const response = await fetch('http://localhost:8000/download/', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`,
      },
      body: JSON.stringify({ url }),
    });
    return response.json();
  }
};
    