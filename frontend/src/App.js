import React, { useState } from 'react';
import { Button, TextField, Box, Typography, Paper, Divider } from '@mui/material';

function App() {
  const [query, setQuery] = useState('');
  const [chat, setChat] = useState([]);

  const send = async () => {
    try {
      const res = await fetch('http://localhost:8000/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: query }),
      });

      const data = await res.json();
      const botReply =
        typeof data.answer === 'string'
          ? data.answer
          : data.answer?.text ?? 'No valid response';

      setChat([...chat, { user: query, bot: botReply }]);
    } catch {
      setChat([...chat, { user: query, bot: 'Network or server error' }]);
    }

    setQuery('');
  };

  return (
    <Box
      sx={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        p: 4,
        backgroundColor: '#f5f5f5',
        minHeight: '100vh',
      }}
    >
      <Typography variant="h4" gutterBottom>
        AI LinkedIn Assistant (Demo)
      </Typography>

      <Paper
        sx={{
          width: '100%',
          maxWidth: 600,
          mb: 3,
          p: 2,
          height: '70%',
          overflowY: 'auto',
          borderRadius: 2,
        }}
      >
        {chat.map((c, i) => (
          <Box key={i} sx={{ mb: 2 }}>
            <Box sx={{ bgcolor: '#c8e6c9', p: 1, borderRadius: 2 }}>
              <Typography><strong>You:</strong> {c.user}</Typography>
            </Box>
            <Divider sx={{ my: 1 }} />
            <Box sx={{ bgcolor: '#e0f7fa', p: 1, borderRadius: 2 }}>
              <Typography><strong>Coach:</strong> {c.bot}</Typography>
            </Box>
          </Box>
        ))}
      </Paper>

      <Box sx={{ display: 'flex', width: '100%', maxWidth: 600 }}>
        <TextField
          fullWidth
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask a question..."
        />
        <Button sx={{ ml: 2 }} variant="contained" onClick={send}>
          Send
        </Button>
      </Box>
    </Box>
  );
}

export default App;
