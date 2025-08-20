from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Load DialoGPT model and tokenizer
model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Use text-generation pipeline
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

print("ChatBot: Hi! Type 'bye' to exit.")

chat_history = ""
while True:
    user = input("You: ")
    if user.lower() == "bye":
        print("ChatBot: Goodbye!")
        break

    # Append user input to chat history
    chat_history += f"User: {user}\nChatBot:"

    # Generate response (fixed: use max_new_tokens + truncation)
    response = generator(
        chat_history,
        max_new_tokens=100,       # number of tokens the bot generates
        pad_token_id=tokenizer.eos_token_id,
        truncation=True           # explicitly truncate long history
    )[0]["generated_text"]

    # Extract chatbot's latest reply
    reply = response.split("ChatBot:")[-1].split("User:")[0].strip()
    print("ChatBot:", reply)

    # Keep history for context
    chat_history += f" {reply}\n"
