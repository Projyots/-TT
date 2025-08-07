import React, { useState } from "react";

// Helper to call backend for chat completion
async function fetchChatCompletion(prompt) {
  const res = await fetch("/api/llm", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt }),
  });
  return await res.json();
}

// Helper to call backend for embeddings
async function fetchEmbedding(text) {
  const res = await fetch("/api/embedding", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text }),
  });
  return await res.json();
}

function App() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);
  const [chatHistory, setChatHistory] = useState([]);
  const [embedding, setEmbedding] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResponse("");
    setEmbedding(null);
    try {
      // Add user message to chat history
      setChatHistory((prev) => [...prev, { role: "user", content: prompt }]);
      // Fetch chat completion
      const data = await fetchChatCompletion(prompt);
      const botResponse = data.response || data.error || "No response";
      setResponse(botResponse);
      setChatHistory((prev) => [...prev, { role: "assistant", content: botResponse }]);
      // Fetch embedding for the prompt
      const embData = await fetchEmbedding(prompt);
      setEmbedding(embData.embedding || embData.error || null);
    } catch (err) {
      setResponse("Error: " + err.message);
    }
    setLoading(false);
    setPrompt("");
  };

  return (
    <div style={{ maxWidth: 600, margin: "2rem auto", fontFamily: "sans-serif" }}>
      <h1>Azure LLM Chatbot (Flask)</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          rows={4}
          style={{ width: "100%" }}
          value={prompt}
          onChange={e => setPrompt(e.target.value)}
          placeholder="Enter your prompt..."
        />
        <button type="submit" disabled={loading || !prompt.trim()}>
          {loading ? "Loading..." : "Send"}
        </button>
      </form>
      <div style={{ marginTop: 20 }}>
        <strong>Chat History:</strong>
        <div style={{ background: "#f9f9f9", padding: 10, minHeight: 80 }}>
          {chatHistory.map((msg, idx) => (
            <div key={idx} style={{ marginBottom: 8 }}>
              <b>{msg.role === "user" ? "You" : "Bot"}:</b> {msg.content}
            </div>
          ))}
        </div>
      </div>
      <div style={{ marginTop: 20 }}>
        <strong>Latest Response:</strong>
        <pre style={{ background: "#f4f4f4", padding: 10 }}>{response}</pre>
      </div>
      <div style={{ marginTop: 20 }}>
        <strong>Prompt Embedding:</strong>
        <pre style={{ background: "#f4f4f4", padding: 10, maxHeight: 120, overflow: "auto" }}>
          {embedding ? JSON.stringify(embedding).slice(0, 300) + "..." : "No embedding"}
        </pre>
      </div>
    </div>
  );
}

export default App;