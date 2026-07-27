import ReactMarkdown from "react-markdown";

function ChatMessage({ sender, text }) {

    return (

        <div
            className={
                sender === "user"
                    ? "message user"
                    : "message bot"
            }
        >

            <div className="avatar">

                {sender === "user" ? "🧑" : "🤖"}

            </div>

            <div style={{padding:"30px"}} className="bubble">

                <ReactMarkdown>

                    {text}

                </ReactMarkdown>
{/* <span>
    {new Date(Date.now())}
</span> */}
            </div>

        </div>

    );

}

export default ChatMessage;