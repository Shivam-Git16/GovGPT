import { marked } from "marked";
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

                 dangerouslySetInnerHTML={{
    __html: marked(text),
  }}

            </div>

        </div>

    );

}

export default ChatMessage;