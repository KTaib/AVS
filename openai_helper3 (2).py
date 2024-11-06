import openai
from secret_key import openai_api_key
import json
import pandas as pd

openai.api_key = openai_api_key

def extract_data(text):
    prompt = get_prompt() 
    responses = []

    # Split the input text into chunks of maximum length allowed
    chunk_size = 100000 # 1 MB
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    # Make requests for each chunk and collect responses
    for chunk in chunks:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt + chunk}]
        )
        content = response.choices[0]['message']['content']
        responses.append(content)

    # Concatenate the responses into a single paragraph
    combined_content = ' '.join(responses)
    
     # Return the paragraph as a DataFrame
    return combined_content

def get_prompt():
 return '''
(Please start the response with "**DISCOVERY**", followed by one line of spacing, and then follow with sections 1 and 2)
**DISCOVERY**\n\n

**1 - GOALS & CHALLENGES**\n\n
• Organization Name:(Extract Organization name from the inserted report)\n
• Financial Year:(Extract financial year for the inserted report)\n

(Instrucitons are enclosed in (), Context are enclosed in [])

[Context: As a business analyst and seller at Acquia, extract value-selling related information from the provided report. Acquia is a Digital Experience Platform & Digital Experience Optimization Solution Provider]
(Instructions: Extract and detail the following, High-priority CEO goals Acquia's solutions can address.)
(When working with provided report kindly avoid final section of appendices, annexes, exhibits, attachments, or supplements to reduce the processing of unnecessary content.)
(Please present each point, on next line.\n)
**CVGs**\n
[CVGs (CEO’s Vital Goals) are a high priority CEO / Organizational goals and challenges, a seller at Acquia can attach Acquia solutions to.]
**Revenue targets:** (Should be Measurable and Time Bound and something Acquia can impact with its solutions.(Do not mention Acquia in the response.))\n\n
**Cost-saving targets:** (Should be Measurable and Time Bound and something Acquia can impact with its solutions.(Do not mention Acquia in the response.))\n\n
**Risk mitigation actions:** (Should be Measurable and Time Bound and something Acquia can impact with its solutions.(Do not mention Acquia in the response.))\n\n
(Include the financial year information.)
**FO (Functional Objectives):** (Departmental goals supporting CVGs and something Acquia can impact.(Do not mention Acquia in the response.))\n\n
**FI (Funded Initiatives):** (Projects supporting FOs and something Acquia can impact.(Do not mention Acquia in the response.))\n\n
**Insight Statement:** (Statement that sums up the CVG, functional objective and supporting funded initiatives. Should follow this structure: Based on my research I have found [insert CVG] and I imagine to deliver on this your focus areas would be Y [insert FOs] support by the following projects [insert FIs]. Is this correct?)\n\n
**Sentiment Analysis:** (As a business analyst, extract the overall impression of the data input. What would you say the overall mood of the company is, did they miss or exceed targets?)\n\n
**Business Issue:** (High-level impediment to achieving CVGs.)\n\n
(Include the financial year information.)

(If information is unavailable, return “ ”.)
**2 - DISCOVERY AND QUALIFICATION**\n\n

**Open Problem Question:**\n\n
What's preventing you from driving greater digital marketing ROI?

**Problem Probing Questions:**\n\n
(Instructions: From the problem questions listed below, extract the relevant multiple questions to be asked to the buyers and don’t limit it to one question. Determine which questions to ask based on the extracted CVGs, FOs and FIs and where Acquia is best positioned to add value based on its product offering / strengths.) 
(Present each question on a new/next line.\n)
(1.) Is it difficult to measure the impact of your content and SEO spend within your current budgets?
(2.) Are you confident your brand experiences are accessible to the widest audience and compliant with regulations?
(3.) Are you struggling to increase on-site conversions?
(4.) Are you uncertain which content optimization capabilities will have the most impact on marketing spend and team efficiency?
(5.) Do you know if brand consistency is implemented across your websites?

**Confirmation:**\n\n
Anything Else? What I’m hearing is…correct? Might we prioritize these now?

**Open Solution Question:**\n\n
What do you think it will take to solve these challenges?

**Solution Probing Questions:**\n\n
(Instructions: From the solution questions listed below, identify and extract the relevant match questions on the basis above selected problem probing questions (based on serial number), to be asked to the buyers.)
(Present each question on a new/next line.\n)
(1.) Is it important to achieve competitive advantage through optimized keyword relevance?
(2.) Would you like to ensure your digital experiences are inclusive and accessible to everyone?
(3.) Have you considered alternative solutions for conversion optimization?
(4.) Would you consider a unified solution for digital marketing optimization?
(5.) Has anyone shown you how much time and effort can be saved with automated brand policy management?

**Confirmation:**\n\n
Anything Else? If someone can deliver all of this, will you be able to ensure maximum ROI on content spend?
'''

###
def extract_email_data(text):
    prompt = get_prompt_email() 
    responses = []

    # Split the input text into chunks of maximum length allowed
    chunk_size = 100000  # 1 MB
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    # Make requests for each chunk and collect responses
    for chunk in chunks:
     response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user","content": prompt + chunk}]
    )
    content = response.choices[0]['message']['content']
    responses.append(content)
    
    # Concatenate and parse the responses
    combined_content = ''.join(responses)

    return combined_content

def get_prompt_email():
 return'''
(Please start the response with "**EMAIL**", followed by one line of spacing, and then follow with Email)
**EMAIL**\n\n

(Instrucitons are enclosed in (), Context are enclosed in [])
(When working with provided report kindly avoid final section of appendices, annexes, exhibits, attachments, or supplements to reduce the processing of unnecessary content.)

(Instrucitons: Craft an email for an Acquia seller looking to prospect into a new opportunity. Be sure to use the information provided and apply it to the template below. The objective is to obtain a response from the prospect, so ensure the email is informative, value based and not too salesy.)
(Organization Name:(Extract Organization name from the inserted report))

[Context: As a business analyst and seller at Acquia, extract value-selling related information from the provided report. Acquia is a Digital Experience Platform & Digital Experience Optimization Solution Provider.
CVGs (CEO’s Vital Goals) are a high priority CEO / Organizational goals and challenges, a seller at Acquia can attach Acquia solutions to.
Revenue targets: Should be Measurable and Time Bound and something Acquia can impact with its solutions.
Cost-saving targets: Should be Measurable and Time Bound and something Acquia can impact with its solutions.
Risk mitigation actions: Should be Measurable and Time Bound and something Acquia can impact with its solutions.
(Include the financial year information.)
FO (Functional Objectives): Departmental goals supporting CVGs and something Acquia can impact.
FI (Funded Initiatives): Projects supporting FOs and something Acquia can impact.
Insight Statement: Statement that sums up the CVG, functional objective and supporting funded initiatives. Should follow this structure: Based on my research I have found [insert CVG] and I imagine to deliver on this your focus areas would be Y [insert FOs] support by the following projects [insert FIs]. Is this correct?)
Sentiment Analysis: As a business analyst, extract the overall impression of the data input. What would you say the overall mood of the company is, did they miss or exceed targets?)
Business Issue: High-level impediment to achieving CVGs.]

Hello {Customer Name},
In my research on {Organization Name}, I noticed you are {insert Corporate Objective} and highlight {measurable and time bound elements}. I imagine you are focusing on the following departmental objectives {insert FO - Functional Objectives} and developing projects in the following areas {insert FI - Funded Initiatives}.
Possible headwinds in achieving this are {highlight any recent industry / competitive news}. However I would like to explore how Acquia has helped companies similar to yours achieve results. These include {insert relevant Acquia case study}. 

**PROSPECT MAPPING**\n\n
(Instructions: Based on the "Goals & Challenges" extracted above, top four potential role, job title, responsible department at this organization (But not the C level designations), to whom Acquia sellers can best first connect with for selling Acquia Products.)
(Please answer using each point, on next line.\n)
• Display as: 
Role, Job Title, Responsible Department \n\n 
Role, Job Title, Responsible Department \n\n
Role, Job Title, Responsible Department \n\n
Role, Job Title, Responsible Department \n\n
'''

###
def extract_business_data(text):
    prompt = get_prompt_business() 
    responses = []

    # Split the input text into chunks of maximum length allowed
    chunk_size = 100000  # 1 MB
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    # Make requests for each chunk and collect responses
    for chunk in chunks:
     response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user","content": prompt + chunk}]
    )
    content = response.choices[0]['message']['content']
    responses.append(content)
    
    # Concatenate and parse the responses
    combined_content = ''.join(responses)

    return combined_content

def get_prompt_business():
 return'''
(Please start the response with "**BUSINESS CASE**", followed by one line of spacing, and then follow with Email)
**BUSINESS CASE** 
 
(Instructions are enclosed in (), Context are enclosed in []) 

(When working with a provided report, kindly avoid the final section of appendices, annexes, exhibits, attachments, or supplements to reduce the processing of unnecessary content.)

(Instructions: From the provided information, please generate a comprehensive business case for an Acquia seller based on customer organization’s CVGs, FOs & FIs. The business case should focus on how Acquia’s solutions will address the organization’s challenges and drive measurable value and improvements in their business performance. Please structure the business case using the following elements:

• CEO’s Vital Goals (CVGs): 
-Identify the primary goals set by the CEO that align with enhancing customer engagement, conversion, experience, satisfaction, overall business growth in revenue, reducing costs and mitigating risks. 
-[CVGs (CEO’s Vital Goals) are a high priority CEO goal a seller can attach Acquia solutions to.]
• Functional Objectives (FOs): 
-Outline specific departmental objectives that support the overall business strategy, focusing on customer insights, marketing automation, and content delivery. 
[Departmental goals to support the CVG]
• Functional Initiatives (FIs): 
-Detail actionable initiatives that will be undertaken to achieve the functional objectives, including journey orchestration, analytics integration, and loyalty program enhancements. 
-Additionally, include measurable goals where applicable, and where not specified, indicate goals as ’by X%’. 
-Ensure the report highlights how Acquia’s solutions can address current challenges and drive measurable improvements in business performance.
[Projects that support the FO])

• Display as: 
**Organization Name:** \n\n (Extract Organization name from the inserted report) \n\n By Acquia (Create and place an headline for this business case) \n\n 
**Problem Statement:** (Please answer using each point, on next line.\n) \n\n Opportunity: (Please answer using each point, on next line.\n) \n\n 
**Recommended Approach:** (Please answer using each point, on next line.\n) \n\n 
**Targeted Outcomes:** (Please answer using each point, on next line. Additionally, include measurable goals where applicable, and where not specified, indicate goals as ’by X%’.\n) \n\n 
**Conclusion:** (Please answer using each point, on next line.\n) \n\n

[Acquia: “Acquia is a leading software-as-a-service (SaaS) company that specializes in providing a digital experience platform (DXP) built around the open-source content management system (CMS) Drupal. Co-founded by Dries Buytaert, Acquia empowers organizations to create, manage, and optimize their digital experiences across various channels. The company offers a suite of solutions designed to enhance customer engagement, streamline operations, and drive business growth.
Acquia Solutions Overview:
Digital Experience Optimization (DXO)
• Enhances content relevance, search performance, and conversions, ensuring seamless customer engagement and satisfaction.
• Integrates Acquia SEO, Acquia Convert, and Monsido to optimize content visibility, user experience, and compliance.
Cloud Platform Support
• Ensures optimal performance and scalability of digital experiences, with features like dynamic scaling and enterprise caching.
Multi-site Management
• Facilitates efficient governance and streamlined updates across multiple websites from a single dashboard.
Low-code Site Development
• Enables users to create and manage visually appealing websites without extensive coding knowledge, ensuring brand consistency and faster time to market.
Centralized Digital Asset Management
• Streamlines the management of digital assets, enhancing content accessibility and collaboration.
Customer Data Platform (CDP)
• Unifies customer data to personalize experiences and generate actionable insights.
Marketing Automation Tools
• Orchestrates multichannel marketing campaigns, enhancing customer engagement through targeted messaging.
Personalization Engine
• Delivers tailored experiences based on user data, improving engagement and satisfaction.
Content Delivery Network (CDN)
• Improves website performance by distributing content closer to users, reducing load times.
Visual Design Systems
• Allows designers and developers to create custom themes and layouts visually.
Analytics and Machine Learning Integration
• Provides insights into user behavior and enhances personalization through predictive analytics.
Scalability and Security Measures
• Supports growth in user base and content volume while ensuring data protection and compliance with regulations.
Conclusion: Acquia’s solutions are designed to empower organizations to deliver exceptional digital experiences while maintaining flexibility and scalability. By leveraging Acquia’s suite of solutions, businesses can enhance customer engagement, streamline operations, and adapt to the evolving digital landscape, ultimately driving growth and success in their respective markets”] 
'''
