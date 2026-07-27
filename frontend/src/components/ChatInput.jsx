function ChatInput({ question, setQuestion, sendMessage, loading }) {
  return (
    <div className="input-area">
      <input
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask about any Government Service..."
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            sendMessage();
          }
        }}
      />

      <button onClick={sendMessage} disabled={loading}>
        {loading ? "..." : "Send"}
      </button>
    </div>
  );
}

export default ChatInput;