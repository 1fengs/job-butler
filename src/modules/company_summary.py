from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_company_summary(company_name):

    prompt = f"""
    Write ONE short professional sentence about the company {company_name} without subject (directly start with a verb).

    Rules:
    - The result should come after "a chance to bring my expertise and enthusiasm for
autonomous systems, embedded software, and system integration to an organization that" and the whole sentence is coherent and cohesive
    - First letter not capitalized, and no period at the end
    - Maximum 15 words
    - Professional tone
    - Suitable for a job application cover letter
    - Focus on innovation, market position, or practical impact
    - No marketing fluff
    - No quotation marks
    - If the company is not found or no information found, return "No information available"
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=40
    )

    return response.choices[0].message.content.strip()