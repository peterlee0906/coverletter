import os
import streamlit as st
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

if openai.api_key:
    print("OpenAI API Key:", openai.api_key)
else:
    print("OpenAI API Key not found.")


def generate_cover_letter(model, prompt):
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

def write():
    st.title("Cover Letter Generator")

    model = "text-davinci-002"

    name = st.text_input("Name:")
    email = st.text_input("Email:")
    phone = st.text_input("Phone Number:")
    job_title = st.text_input("Job Title:")
    company = st.text_input("Company Name:")
    description = st.text_area("Job Description:")

    if st.button("Generate Cover Letter"):
        prompt = (f"Dear Hiring Manager,\n\n"
                  f"My name is {name} and I am writing to apply for the {job_title} position at {company}.\n\n"
                  f"{description}\n\n"
                  f"Thank you for considering my application. I look forward to the opportunity to further discuss my qualifications with you.\n\n"
                  f"Best regards,\n\n"
                  f"{name}\n"
                  f"{email}\n"
                  f"{phone}")
        cover_letter = generate_cover_letter(model, prompt)
        st.write("Generated Cover Letter:")
        st.write("-" * 20)
        st.write(cover_letter)

if __name__ == '__main__':
    write()
