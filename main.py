# demo
import gradio as gr


def greet(name):
    return "Helloooo " + name + "!"


demo = gr.Interface(fn=greet, inputs="text", outputs="text")

demo.launch(share=True)
