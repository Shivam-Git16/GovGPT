import { useState } from "react";
import ChatMessage from "./ChatMessage";
import ChatInput from "./ChatInput";
import axios from "axios";

function ChatWindow() {
  const [messages, setMessages] = useState([
    {
      sender: "bot",
      text: "👋 Hello! I'm GovGPT.\n\nAsk me anything about Government Services."
    }
  ]);

  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!question.trim()) return;

    const userQuestion = question;

    setMessages((prev) => [
      ...prev,
      {
        sender: "user",
        text: userQuestion,
      },
    ]);

    setQuestion("");
    setLoading(true);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/chat",
        {
          question: userQuestion,
        }
      );

      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: response.data.answer,
        },
      ]);
    } catch (error) {
      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: "❌ Unable to connect to the backend.",
        },
      ]);
    }

    setLoading(false);
  };

  return (
    <div className="chat-container">
      <div className="chat-box">
        {messages.map((msg, index) => (
          <ChatMessage
            key={index}
            sender={msg.sender}
            text={msg.text}
          />
        ))}
      </div>

      <ChatInput
        question={question}
        setQuestion={setQuestion}
        sendMessage={sendMessage}
        loading={loading}
      />
    </div>
  );
}

export default ChatWindow;