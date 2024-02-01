import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function To get response from LLAma 2 model

def getLLamaresponse(input_text):

    ### LLama2 model
    llm=CTransformers(model='C:/Users/seanr/OneDrive/Desktop/Projects/Blog Generation using LLAMA2/model/llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    
    ## Prompt Template

    template="""
         What is the sentiment of {input_text} ?
         

        """
    
    prompt=PromptTemplate(input_variables=["input_text"],
                          template=template)
    
    ## Generate the ressponse from the LLama 2 model
    response=llm(prompt.format(input_text=input_text))
    print(response)
    return response






st.set_page_config(page_title="Sentiment Analysis",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Sentiment Analysis 🤖")

input_text=st.text_input("Enter the comment or review")



    
submit=st.button("Generate")

## Final response
if submit:
    st.write(getLLamaresponse(input_text))