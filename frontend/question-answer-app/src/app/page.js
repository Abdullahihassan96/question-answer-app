"use client";

import { useState } from "react";
import axios from "axios";

export default function HomePage() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const handleAsk = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/ask", {
        question,
      });
      setAnswer(response.data.answer); // Display the answer
    } catch (error) {
      console.error("Error:", error);
      setAnswer("Something went wrong. Please try again later.");
    }
  };

  return (
    <div>
      <h1>Ask a Question</h1>
      <textarea
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Type your question here..."
      />
      <button onClick={handleAsk}>Ask</button>
      {answer && (
        <div>
          <h2>Answer:</h2>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}