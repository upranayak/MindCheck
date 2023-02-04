import os
import openai
import gradio as gr

openai.api_key ="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"

start_sequence = "\nMindCheck AI:"
restart_sequencepy = "\nUser: "

prompt = "Discover the innovative MindCheck's AI chatbot designed to help you manage your social media addiction! With advanced algorithms, our chatbot provides personalized support 24/7, no matter where you are. Get instant access to calming techniques, mood tracking, and positive self-talk. Say goodbye to stress and hello to a happier you with our Mera Mann AI chatbot today!"

def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" User:", " MindCheck AI:"]
    )

    return response.choices[0].text



def socialdetox(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()


with block:
    gr.Markdown("""<h1><center>MindCheck AI Helper bot</center></h1>
    """)
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(socialdetox, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug = True)