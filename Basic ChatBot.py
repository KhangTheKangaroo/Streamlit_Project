import streamlit as st 
from hugchat import hugchat
from hugchat.login import Login

st.title('Simple ChatBot')

with st.sidebar:
    st.title('Login Hugchat')
    hf_email = st.text_input('Enter E-mail: ')
    hf_pass = st.text_input('Enter Password: ', type = 'password')
    if not (hf_email, hf_pass):
        st.warning('Please enter the correct information to your Account!')
    else:
        st.success('Enter your prompt!')
        
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [{"role": 'assistant', "content": 'How may I help you?'}]
        
    for msg in st.session_state.messages:
        with st.chat_message(msg['role']):
            st.write(msg['content'])
            
    def generate_response(input_prompt, email, passwrd):
        sign = Login(email, passwrd) 
        cookies = sign.login()
        chatbot = hugchat.ChatBot(cookies = cookies.get.dict())
        return chatbot.chat(input_prompt)
    
    if prompt := st.chat_input(disabled = not (hf_email, hf_pass)):
        st.session_state.msg.append({"role": "user", "content": 'prompt'}) 
        with st.chat_message("user"):
            st.write(prompt)
            
    if st.session_state.messages[-1] ["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_response(prompt, hf_email, hf_pass)
                st.write(response)
        message = {"role": 'assistant', "content": response}
        st.session_state.message.append(message)
