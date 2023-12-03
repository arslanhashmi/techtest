# Candidate information
company_applied_at_context = "Coinbase uses technology to push forward to future of web3 with cryptocurrencies, blockchain, and more."
candidate_info = {
    "candidate": "Alfredo Lin",
    "candidate_current_company": "Roblox",
    "candidate_current_role": "Software Engineer",
    "candidate_specialties": ["Web3", "Vue", "Django"],
    "candidate_bio": "Hi! I'm a bay area based software engineer with a love for the outdoors. Outside of work, I love snowboarding and skiing. You can catch me in my favorite local coffee shop, Coupa Cafe",
    "role_applied_for": "Senior Software Engineer III",
    "company_applied_for": "Coinbase",
}

# Generate the prompt
prompt = f"""
Write a professional and engaging recruitment email from "{candidate_info['company_applied_for']}" to "{candidate_info['candidate']}", a "{candidate_info['candidate_current_role']}" at "{candidate_info['candidate_current_company']}" with specialties in {', '.join(candidate_info['candidate_specialties'])}.\n\n
This candidate's bio is as follow:\n"{candidate_info['candidate_bio']}"\n\n
The email should acknowledge his interests and how they align with the role of "{candidate_info['role_applied_for']}" at "{candidate_info['company_applied_for']}"\n\n
More about the {candidate_info['company_applied_for']} company:\n"{company_applied_at_context}"\n\n
The tone should be friendly, personalized, and enthusiastic about the potential of "{candidate_info['candidate']}" joining the "{candidate_info['company_applied_for']}" team.
"""

# Write the prompt to a text file
with open("prompt.txt", "w") as file:
    file.write(prompt)
