# doc_diff_instruct = '''Generate a new question based on the provided document.
# Before I give you the document, I'll give you three examples:
# ###Examples:
# Example 1:
# ###document:
# I got off the plane, grabbed my bags, I saw she on the other side of the door waiting for me, my legs were shaking, my heart was beating fast, breathing breathlessly, I walked up to her, I dropped his bags and gave the best hug of my life for the most perfect girl I've ever seen. I felt floating in the clouds. Tomorrow I'll be miles away but I'll still be able to feel her in my arms. (via divine-infection)
# ###New Question:
# How does the use of immersive virtual reality technology enhance the experience of exploring ancient ruins, and what are the potential ethical considerations when reconstructing historical sites for virtual tours?
# Example 2:
# ###document:
# tag:blogger.com,1999:blog-18922786044488938322014-10-04T19:53:09.407-07:00Little Bob's BlogJust a place for me to rant that is not on facebook!Bob Heathcote Android Market works only with devices with cell/data servicesHa, I was right: <br />.<br /><br /.<br /><br />That is why you need a cell service to have Android Market on your Android tablet. <br />OK, they could have Market on a device without a IMSI, but a lot of apps would not install and complain there is no IMSI to tie the license to.<br /><br />Source: <a href=\"\">Android Developers page</a> <br /><br /><br />More on <a href=\"\">IMSI</a>Bob Heathcote Laguna Seca race reportIt was a pretty good race, up until the oil filter failed on the leading car. Incredible<br /><br />Pretty good read <a href=\"\">here</a>Bob Heathcote 500 on the come back?<p class=\"MsoNormal\"? </p> <p class=\"MsoNormal\"><o:p> That said the race will probably be a total let down with a Penske/Helio runaway</o:p></p> <p class=\"MsoNormal\"><o:p> Discuss?</o:p></p>Bob Heathcote
# ###New Question:
# Write a Python script that parses an HTML blog post and extracts the relevant metadata, such as the date, title, and links. The script should handle any malformed HTML tags, such as unclosed or misplaced <br> or <p> tags, and ensure the data is correctly formatted for further processing.
# Example 3:
# ###document:
# law relating the apparent contrast, Note 1 to entry: The formula is sometimes written where the exponent, Note 2 to entry: Taking into account the relationship between atmospheric transmissivity, Note 3 to entry: The contrast is taken to be the quotient of the difference between the luminance of the object and the luminance of the background, and the luminance of the background.  Note 4 to entry: This entry was numbered 845-11-22 in IEC 60050-845:1987.  Note 5 to entry: This entry was numbered 17-629 in CIE S 017:2011.
# ###New Question:
# An object is placed in front of a lens with a focal length of \\( f = 50 \\, \\text{{cm}} \\). The object is positioned at a distance of \\( d_o = 150 \\, \\text{{cm}} \\) from the lens, and an external factor, such as the medium's refractive index, changes the object distance by a factor of \\( r = 0.8 \\). How would you calculate the apparent image distance \\( d_i \\) using the lens equation: \\(\\frac{{1}}{{f}} = \\frac{{1}}{{d_o}} + \\frac{{1}}{{d_i}}\\).
# ###Your task:
# ###document:
# {doc}
# ###important:
# 1. Do not reuse information from the original document for the new question.
# 2. The new question should be able to be answered without information from the documentation.
# 3. You should capture the difference and correlation between the document and the question in the examples I've provided.
# 4. Ensure that the new question you generate is of high quality.
# 5. Do not provide a solution or answer to the question.
# Your output should be as follows:
# ###New Question: Here is the new question.
# '''
# Example 1:
# ###document:
# I got off the plane, grabbed my bags, I saw she on the other side of the door waiting for me, my legs were shaking, my heart was beating fast, breathing breathlessly, I walked up to her, I dropped his bags and gave the best hug of my life for the most perfect girl I've ever seen. I felt floating in the clouds. Tomorrow I'll be miles away but I'll still be able to feel her in my arms. (via divine-infection)
# ###New Question:
# How does the use of immersive virtual reality technology enhance the experience of exploring ancient ruins, and what are the potential ethical considerations when reconstructing historical sites for virtual tours?


# doc_diff_instruct = '''Generate a new question based on the provided document.
# Before I give you the document, I'll give you four examples:
# Example 1:
# ###document:
# tag:blogger.com,1999:blog-18922786044488938322014-10-04T19:53:09.407-07:00Little Bob's BlogJust a place for me to rant that is not on facebook!Bob Heathcote Android Market works only with devices with cell/data servicesHa, I was right: <br />.<br /><br /.<br /><br />That is why you need a cell service to have Android Market on your Android tablet. <br />OK, they could have Market on a device without a IMSI, but a lot of apps would not install and complain there is no IMSI to tie the license to.<br /><br />Source: <a href=\"\">Android Developers page</a> <br /><br /><br />More on <a href=\"\">IMSI</a>Bob Heathcote Laguna Seca race reportIt was a pretty good race, up until the oil filter failed on the leading car. Incredible<br /><br />Pretty good read <a href=\"\">here</a>Bob Heathcote 500 on the come back?<p class=\"MsoNormal\"? </p> <p class=\"MsoNormal\"><o:p> That said the race will probably be a total let down with a Penske/Helio runaway</o:p></p> <p class=\"MsoNormal\"><o:p> Discuss?</o:p></p>Bob Heathcote
# ###New Question:
# Write a Python script that parses an HTML blog post and extracts the relevant metadata, such as the date, title, and links. The script should handle any malformed HTML tags, such as unclosed or misplaced <br> or <p> tags, and ensure the data is correctly formatted for further processing.
# Example 2:
# ###document:
# law relating the apparent contrast, Note 1 to entry: The formula is sometimes written where the exponent, Note 2 to entry: Taking into account the relationship between atmospheric transmissivity, Note 3 to entry: The contrast is taken to be the quotient of the difference between the luminance of the object and the luminance of the background, and the luminance of the background.  Note 4 to entry: This entry was numbered 845-11-22 in IEC 60050-845:1987.  Note 5 to entry: This entry was numbered 17-629 in CIE S 017:2011.
# ###New Question:
# An object is placed in front of a lens with a focal length of \\( f = 50 \\, \\text{{cm}} \\). The object is positioned at a distance of \\( d_o = 150 \\, \\text{{cm}} \\) from the lens, and an external factor, such as the medium's refractive index, changes the object distance by a factor of \\( r = 0.8 \\). How would you calculate the apparent image distance \\( d_i \\) using the lens equation: \\(\\frac{{1}}{{f}} = \\frac{{1}}{{d_o}} + \\frac{{1}}{{d_i}}\\).
# Example 3:
# ###document:
# About Marie McGinley\nShe is truly an expert with an impressive and broad knowledge of IP law\" - Chambers Europe 2017\nMarie is a Partner and Head of Intellectual Property, Technology and Data Protection. Marie practises in both contentious and commercial intellectual property/technology matters for a broad range of domestic and international clients. She is also a registered Irish Trade Mark Agent. Marie advises on commercial, regulatory and transactional matters.\nMarie has particular experience in intellectual property/technology development, procurement and licensing deals, including managed services, systems integration, technology and business process outsourcing for both domestic and international clients. data protection compliance.\nMarie is also involved in strategic legal due diligence and transitional services arrangements in relation to corporate acquisitions, disposals and restructurings.\nMarie is a member of the IP and Technology Committee and Commercial Law Committee of the Dublin Solicitor Bar Association.\nMarie has spoken at the National Data Protection Conference run by the Irish Computer Society in collaboration with the Association of Data Protection Officers in relation to various data protection matters, including direct marketing initiatives.\nMarie regularly contributes to the E-Commerce Law Report and PLC.\nMarie lectures and tutors in the area of Intellectual Property and Information Technology at the Law Society of Ireland.
# ###New Question:
# What are the legal implications and challenges of enforcing intellectual property rights across multiple jurisdictions, particularly when dealing with digital products and services?
# Example 4:
# ###document:
# The stock market is down Monday, with the Dow Jones Industrial Average down 0.42%, the Nasdaq down 0.18% and the S&P 500 down 0.43%. Today's winners include a pharmaceutical providing a positive update to one of its drug trials and a medical application manufacturer getting bought. Today's only loser is a for-profit educator settling a case with Sallie Mae. Here are Monday's market winners and loser. Biggest Winners Shares of Peregrine Pharmaceuticals, Inc. (NASDAQ: PPHM) are up 82.89% to $2.47 on trading volume of 29.0 million shares. The pharmaceutical company provided strong results of its review of a lung-cancer drug trial, as the company pointed out discrepancies were more limited than the company initially thought. The 52-week high is $5.50. Shares of Epocrates, Inc. (NASDAQ: EPOC) are up 21.58% to $11.70 on trading volume of 3.5 million shares. AthenaHealth, Inc. (NASDAQ: ATHN) will buy the firm for $11.75 per share, or about $292 million. The 52-week high is $11.97 Biggest Loser Shares of ITT Educational Services Inc. (NYSE: ESI) are down 15.76% to $16.25 on trading volume of 3.2 million shares. The for-profit educator will pay Sallie Mae $46 million to settle litigation involving student loans. Before Monday, the 52-week low was $16.37. Follow Samuel on Twitter: SWeigley Samuel Weigley
# ###New Question:
# A company observes that its stock price follows a quadratic trend over time. The price \( P(t) \) is modeled by the equation \( P(t) = at^2 + bt + c \), where \( t \) is the time in days, and \( a \), \( b \), and \( c \) are constants. If the stock price was \$20 on day 0, \$25 on day 1, and \$30 on day 2, determine the values of \( a \), \( b \), and \( c \).
# ###Your task:
# ###document:
# {doc}
# ###important:
# 1. Do not reuse information from the original document for the new question.
# 2. The new question should be able to be answered without information from the documentation.
# 3. You should capture the difference and correlation between the document and the question in the examples I've provided.
# 4. Do not focusing too much on the question and the form of the question in the example.
# 5. Ensure that the new question you generate is of high quality.
# 6. Do not provide a solution or answer to the question.
# Your output should be as follows:
# ###New Question: Here is the new question.
# '''

doc_diff_instruct_0 = '''Generate a new question based on the provided document.
Before I give you the document, I'll give you four examples:
Example 1:
### document:
{doc1}
### New Question:
{question1}
Example 2:
### document:
{doc2}
### New Question:
{question2}
Example 3:
### document:
{doc3}
### New Question:
{question3}
### Your task:
### document:
{doc}
### important:
1. Do not reuse information from the original document for the new question.
2. The new question should be able to be answered without information from the documentation.
3. You should capture the difference and correlation between the document and the question in the examples I've provided.
4. Ensure that the new question you generate is of high quality.
5. Do not provide a solution or answer to the question.
Your output should be as follows:
### New Question: Here is the new question.
'''

doc_diff_instruct = '''Generate a new question based on the provided document.
Before I give you the document, I'll give you four examples:
Example 1:
### document:
tag:blogger.com,1999:blog-18922786044488938322014-10-04T19:53:09.407-07:00Little Bob's BlogJust a place for me to rant that is not on facebook!Bob Heathcote Android Market works only with devices with cell/data servicesHa, I was right: <br />.<br /><br /.<br /><br />That is why you need a cell service to have Android Market on your Android tablet. <br />OK, they could have Market on a device without a IMSI, but a lot of apps would not install and complain there is no IMSI to tie the license to.<br /><br />Source: <a href=\"\">Android Developers page</a> <br /><br /><br />More on <a href=\"\">IMSI</a>Bob Heathcote Laguna Seca race reportIt was a pretty good race, up until the oil filter failed on the leading car. Incredible<br /><br />Pretty good read <a href=\"\">here</a>Bob Heathcote 500 on the come back?<p class=\"MsoNormal\"? </p> <p class=\"MsoNormal\"><o:p> That said the race will probably be a total let down with a Penske/Helio runaway</o:p></p> <p class=\"MsoNormal\"><o:p> Discuss?</o:p></p>Bob Heathcote
### New Question:
Write a Python script that parses an HTML blog post and extracts the relevant metadata, such as the date, title, and links. The script should handle any malformed HTML tags, such as unclosed or misplaced <br> or <p> tags, and ensure the data is correctly formatted for further processing.
Example 2:
### document:
law relating the apparent contrast, Note 1 to entry: The formula is sometimes written where the exponent, Note 2 to entry: Taking into account the relationship between atmospheric transmissivity, Note 3 to entry: The contrast is taken to be the quotient of the difference between the luminance of the object and the luminance of the background, and the luminance of the background.  Note 4 to entry: This entry was numbered 845-11-22 in IEC 60050-845:1987.  Note 5 to entry: This entry was numbered 17-629 in CIE S 017:2011.
### New Question:
An object is placed in front of a lens with a focal length of \\( f = 50 \\, \\text{{cm}} \\). The object is positioned at a distance of \\( d_o = 150 \\, \\text{{cm}} \\) from the lens, and an external factor, such as the medium's refractive index, changes the object distance by a factor of \\( r = 0.8 \\). How would you calculate the apparent image distance \\( d_i \\) using the lens equation: \\(\\frac{{1}}{{f}} = \\frac{{1}}{{d_o}} + \\frac{{1}}{{d_i}}\\).
Example 3:
### document:
I got off the plane, grabbed my bags, I saw she on the other side of the door waiting for me, my legs were shaking, my heart was beating fast, breathing breathlessly, I walked up to her, I dropped his bags and gave the best hug of my life for the most perfect girl I've ever seen. I felt floating in the clouds. Tomorrow I'll be miles away but I'll still be able to feel her in my arms. (via divine-infection)
### New Question:
How does the use of immersive virtual reality technology enhance the experience of exploring ancient ruins, and what are the potential ethical considerations when reconstructing historical sites for virtual tours?
### Your task:
### document:
{doc}
### important:
1. Do not reuse information from the original document for the new question.
2. The new question should be able to be answered without information from the documentation.
3. You should capture the difference and correlation between the document and the question in the examples I've provided.
4. Ensure that the new question you generate is of high quality.
5. Do not provide a solution or answer to the question.
You can refer to the format of the question below:
{lima_question}
Your output should be as follows:
### New Question: Here is the new question.
'''
# Refer to the properties I gave
# ### Changed Attributes:
# <attribute 1>: Description of the attribute changed in the new question.
# <attribute 2>: Description of the attribute changed in the new question.
# ...
# Here are some common attributes that make up a document:
# subtopic, writing style, resource, scene, skill.
doc_keypoint_prompt_few_shot = '''Please summarize the attributes that make up the provided document and change all of them to generate a more varied question.
Before I give you the document, I'll give you some examples:
### Examples:
Example 1:
### document:
Roseboro Lodge hosts tournament and support Leopards\nSpring Branch Lodge No. 336 hosted its first annual basketball tournament July 19 and 20.\nThe tournament hosted four teams and provided an opportunity for everyone who attended to participate in this event, transforming it from a basketball tournament to an event for the whole family. The championship game included the Enforcers, a team out of Fayetteville, playing Team Chaos, a team constructed of men from the Roseboro and Clinton areas, with the Enforcers coming in first place.\nThe remaining teams were Team 28382-CT and Team Crusaders.\nActivities to allow spectators in the stands to participate included a free throw competition between the women and a half court competition for anyone interested in participating, with prizes awarded. The children were allowed to make a basket anywhere on the court they could shoot, with prizes being awarded to each child that participated.\nTournament proceeds were given support to the Lakewood High School Lady Leopards and Camp Lead-Up 2013.\nWeather\nLocal Gas Prices\nFeatured Business
### Attributes:
Subtopic: A local basketball tournament organized by a community lodge.
Writing Style: Informative and community-focused.
Resource: Details about the tournament's events, teams, and proceeds.
Scene: A basketball court and community setting with various participants.
Skill: Organizing and hosting community events.
### New Question:
What are some effective strategies for organizing an inclusive music festival?
### Changed Attributes:
Subtopic: Changed from a basketball tournament to a music festival.
Writing Style: Changed to advisory and strategy-focused.
Resource: General guidelines and best practices instead of event details.
Scene: Changed from a basketball court to an outdoor or indoor music festival venue.
Skill: Changed from event hosting to inclusive planning and management.

Example 2:
### document:
Create an Account - Increase your productivity, customize your experience, and engage in information you care about.\nSergeant Craig Hamilton oversees five full-time officers who are crime prevention trained. They are dedicated to increasing community awareness of crime-related problems and ways in which to address them. In addition to crime prevention activities, the officers provide public safety information to residents of our community.\nCrime prevention enhances the Police Department\u2019s image through the many positive public relations contacts within the community. The division is also responsible in the operation of the Citizen\u2019s Police Academy, Trunk-or-Treat, and Officer Santa programs.\nAdditionally, this unit has adopted a new program in which victims of residential and business burglaries are contacted by telephone or in person. The goal of this program is for a Community Service officer to perform a home security survey of a victim\u2019s property and inform the citizens of changes that should be made to decrease the probability of being victimized in the future.
### Attributes:
Purpose: Focuses on increasing productivity, enhancing experiences, and addressing user-specific concerns.
Roles: Mentions specific individuals (e.g., Sergeant) and their responsibilities in managing a team focused on a particular goal.
Initiatives: Highlights programs and activities intended to improve public engagement and address specific problems.
Public Interaction: Emphasizes outreach efforts through direct contact and public events.
Program Goals: Outlines intentions, such as reducing risks and enhancing safety for individuals affected by specific challenges.
### New Question:
How can a leadership team effectively implement innovative community programs to foster stronger public engagement and address safety concerns?
### Changed Attributes:
Purpose: The focus is shifted to leadership and its role in developing community-focused innovations.
Roles: Describes the broader concept of leadership teams rather than specific individuals.
Initiatives: Generalizes the concept of programs to innovative community solutions without referencing specific examples.
Public Interaction: Broadened to include fostering public engagement in diverse ways.
Program Goals: Reframed to emphasize overall safety and engagement outcomes without detailing the means.

Your task:
### document:
{doc}
### important:
1. Do not reuse information from the original document for the new question.
2. The new question should be able to be answered without information from the document.
3. The new question should be based on the changed attributes and be independent of the original document.
4. The attributes you summarize should not be too specific, but should be general.
5. Ensure that the new question you generate is of high quality.
6. Do not provide a solution or answer to the question.
Your output should be as follows:
### Attributes:
<attribute 1>: Description of the attribute in the original document.
<attribute 2>: Description of the attribute in the original document.
...
### New Question: Here is the new question.
### Changed Attributes:
<attribute 1>: Description of the attribute changed in the new question.
<attribute 2>: Description of the attribute changed in the new question.
...
'''


# ### Selected Attributes:
# <attribute 1>: Here is the content.
# <attribute 2>: Here is the content.
# <attribute 3>: Here is the content.
# ### Changed Attributes:
# <attribute 1>: Here is the content.
# <attribute 2>: Here is the content.
# <attribute 3>: Here is the content.
# 1. Do not reuse information from the original document for the new question.
# 2. The new question can be answered without information from the document.
# 3. You can not generate questions about the selected attributes.
# 4. The new question should be **independent** of the original document.
# most suitable
doc_keypoint_prompt_change = '''Here are some common attributes that make up a document:
{sl_attributions}
Please select **2** most suitable attributes that make up the following document and change them to generate a new question.
### document:
{doc}
### important:
1. You need to explain the selected attributes before and after the change.
2. Do not provide a solution or answer to the question.
Your output should be as follows:
### Selected Attributes:
1. <selected attributes 1>
2. <selected attributes 2>
### Explaination:
1. The <selected attributes 1> changes from ? to ?.
2. The <selected attributes 2> changes from ? to ?.
### New Question:
An question that aligns with the changed attributes, but is unrelated to the document.
### Check:
1. Check the irrelevance between the new question and the document(The information from the document has not been disclosed to the new question, and the response to the new question does not require information from the document).
2. Check the completeness of the new question(If you are only provided with this new question without any other information, you can answer this question).
2. Check the logical consistency of the new question.
3. Check the consistency with the changed attributes of the new question.
'''

# 1. <selected attributes 1>: <value>
# ### Question Format:
# {format}
# 3. Refer to the example question format, but don't copy it exactly.
doc_keypoint_prompt = '''Here are some common attributes that make up a document:
{sl_attributions}
Please select **1** most suitable attribute that make up the following document and generate a new question based on the value of the attribute in the original document.
### Document:
{doc}
### Example Question:
{lima_question1}
### important:
1. The format of the new question should be similar to that of the example question, but the content should be unrelated.
2. You need to explain the value of the selected attribute in the original document.
3. You need to check the new question and output the results of your check.
4. Do not provide a solution or answer to the question.
Your output should be as follows:
### Selected Attribute and Value:
<selected attribute>: <value>
### New Question:
Here is the new question.
### Check:
1. Ensure that the new question aligns with the selected attribute value.
2. The information from the document has not been disclosed to the new question, and the response to the new question does not require information from the document.
3. Check the completeness of the new question(If you are only provided with this new question without any other information, you can answer this question).
4. Check the logical consistency of the new question.
'''

doc_keypoint_prompt_few_atr = '''Here are some common attributes that make up a document:
{sl_attributions}
Please select **2** most suitable attributes that make up the following document and generate a new question based on the value of the attribute in the original document.
### Document:
{doc}
### Example Question:
{lima_question1}
### important:
1. The format of the new question should be similar to that of the example question, but the content should be unrelated.
2. You need to explain the values of the selected attributes in the original document.
3. You need to check the new question and output the results of your check.
4. Do not provide a solution or answer to the question.
Your output should be as follows:
### Selected Attributes and Values:
<selected attribute 1>: <value of selected attribute 1>
<selected attribute 2>: <value of selected attribute 2>
### New Question:
<Here is the new question>
### Check:
1. Ensure that the new question aligns with the selected attributes values.
2. The information from the document has not been disclosed to the new question, and the response to the new question does not require information from the document.
3. Check the completeness of the new question(If you are only provided with this new question without any other information, you can answer this question).
4. Check the logical consistency of the new question.
'''

doc_keypoint_prompt_math = '''Here are some common attributes that make up a document:
{sl_attributions}
Please select **1** most suitable attribute that make up the following document and generate a new question based on the value of the attribute in the original document.
### Document:
{doc}
### important:
1. You need to explain the value of the selected attribute in the original document.
2. You need to check the new question and output the results of your check.
3. Do not provide a solution or answer to the question.
Your output should be as follows:
### Selected Attribute and Value:
<selected attribute>: <value>
### New Question:
Here is the new question.
### Check:
1. Ensure that the new question aligns with the selected attribute value.
2. The information from the document has not been disclosed to the new question, and the response to the new question does not require information from the document.
3. Check the completeness of the new question(If you are only provided with this new question without any other information, you can answer this question).
4. Check the logical consistency of the new question.
'''

# ### Question Format:
# {format}

doc_keypoint_prompt_self_1_shot = '''Please summarize the attributes that make up the provided document, select **1** attribute, and generate a new question based on the value of the selected attribute in the original document.
### Document:
{doc}
### Example Question:
{lima_question1}
### important:
1. The format of the new question should be similar to that of the example question, but the content should be unrelated.
2. You need to explain the value of the selected attribute in the original document.
3. You need to check the new question and output the results of your check.
4. Do not provide a solution or answer to the question.
Your output should be as follows:
### Attributes and Values:
<attribute 1>: <value of attribute 1 in the original document>
<attribute 2>: <value of attribute 2 in the original document>
...
### Selected Attributes and Values:
<selected attribute>: <value of selected attribute in the original document>
### New Question:
Here is the new question.
### Check:
1. Ensure that the new question aligns with the selected attribute value and it is independent of other attributes.
2. The information from the document has not been disclosed to the new question, and the response to the new question does not require information from the document.
3. Check the completeness of the new question(If you are only provided with this new question without any other information, you can answer this question).
4. Check the logical consistency of the new question.
'''

doc_keypoint_prompt_self_1_shot_n_question = '''Please summarize the attributes that make up the provided document, select the appropriate attributes, and generate a new question based on the value of each selected attribute.
### Document:
{doc}
### Example Question:
{lima_question1}
### important:
1. The format of the new question should be similar to that of the example question, but the content should be unrelated.
2. You need to explain the value of the selected attribute in the original document.
3. You need to check the new question and output the results of your check.
4. Do not provide a solution or answer to the question.
Your output should be as follows:
### Attributes and Values:
Here are the attributes and their corresponding values from the original document.
### Selected Attributes and Values:
Here are the selected attributes and their corresponding values from the original document.
### New Question:
1. <new question 1>
2. <new question 2>
...
n. <new question n>
### Check:
1. Ensure that each new question is aligned with its respective attribute value, and that the new questions should have no relation to each other.
2. The information from the document has not been disclosed to the new question, and the response to the new question does not require information from the document.
'''

doc_keypoint_prompt_self_n_question = '''Please summarize the attributes that make up the provided document, select the appropriate attributes, and generate a new question based on the value of each selected attribute.
### Document:
{doc}
### important:
1. You need to explain the value of the selected attribute in the original document.
2. You need to check the new question and output the results of your check.
3. Do not provide a solution or answer to the question.
Your output should be as follows:
### Attributes and Values:
Here are the attributes and their corresponding values from the original document.
### Selected Attributes and Values:
Here are the selected attributes and their corresponding values from the original document.
### New Question:
1. <new question 1>
2. <new question 2>
...
n. <new question n>
### Check:
1. Ensure that each new question is aligned with its respective attribute value, and that the new questions should have no relation to each other.
2. The information from the document has not been disclosed to the new question, and the response to the new question does not require information from the document.
'''

doc_keypoint_prompt_self = '''Please summarize the attributes that make up the provided document, select **1** attributes, and generate a new question based on the value of the selected attribute in the original document.
### Document:
{doc}
### important:
1. You need to explain the value of the selected attribute in the original document.
2. You need to check the new question and output the results of your check.
3. Do not provide a solution or answer to the question.
Your output should be as follows:
### Attributes and Values:
<attribute 1>: <value of attribute 1 in the original document>
<attribute 2>: <value of attribute 2 in the original document>
...
### Selected Attributes and Values:
<selected attribute>: <value of selected attribute in the original document>
### New Question:
Here is the new question.
### Check:
1. Ensure that the new question aligns with the selected attribute value and it is independent of other attributes.
2. The information from the document has not been disclosed to the new question, and the response to the new question does not require information from the document.
3. Check the completeness of the new question(If you are only provided with this new question without any other information, you can answer this question).
4. Check the logical consistency of the new question.
'''

doc_keypoint_prompt_self_test = '''Please summarize the attributes that make up the provided document, select **1** attributes, and generate a new question based on the selected attribute.
### Document:
{doc}
### important:
1. The new question should be **unrelated** to the original document.
2. The new question aligns with the selected attribute and it is independent of other attributes.
3. The response to the new question does not require information from the document.
4. Do not provide a solution or answer to the question.
Your output should be as follows:
### Attributes:
Here are the attributes.
### Selected Attribute:
Here is the selected attribute.
### New Question:
Here is the new question.
'''

doc_keypoint_prompt_self_n_test = '''Please summarize the attributes that make up the provided document, and generate a new question based on each attribute.
### Document:
{doc}
### important:
1. The new questions should be **unrelated** to the original document.
2. The new questions should align with the selected attribute and it is independent of other attributes.
3. The new questions should be independent of each other.
4. The response to the new question does not require information from the document.
5. Do not provide a solution or answer to the question.
Your output should be as follows:
### Attributes:
Here are the attributes.
### New Questions:
Here are the new questions.
'''

#  value
# 1. Do not reuse information from the original document for the new question.
# 2. The new question should be able to be answered without information from the documentation.
# 3. You should capture the difference and correlation between the document and the question in the examples I've provided.
# 4. Do not focusing too much on the question and the form of the question in the example.
# 5. The new question you generate is **independent** of the questions in the examples.


# doc_diff_instruct = '''Generate a new question based on the provided document.
# Before I give you the document, I'll give you four examples:
# Example 1:
# ###document:
# tag:blogger.com,1999:blog-18922786044488938322014-10-04T19:53:09.407-07:00Little Bob's BlogJust a place for me to rant that is not on facebook!Bob Heathcote Android Market works only with devices with cell/data servicesHa, I was right: <br />.<br /><br /.<br /><br />That is why you need a cell service to have Android Market on your Android tablet. <br />OK, they could have Market on a device without a IMSI, but a lot of apps would not install and complain there is no IMSI to tie the license to.<br /><br />Source: <a href=\"\">Android Developers page</a> <br /><br /><br />More on <a href=\"\">IMSI</a>Bob Heathcote Laguna Seca race reportIt was a pretty good race, up until the oil filter failed on the leading car. Incredible<br /><br />Pretty good read <a href=\"\">here</a>Bob Heathcote 500 on the come back?<p class=\"MsoNormal\"? </p> <p class=\"MsoNormal\"><o:p> That said the race will probably be a total let down with a Penske/Helio runaway</o:p></p> <p class=\"MsoNormal\"><o:p> Discuss?</o:p></p>Bob Heathcote
# ###New Question:
# Write a Python script that parses an HTML blog post and extracts the relevant metadata, such as the date, title, and links. The script should handle any malformed HTML tags, such as unclosed or misplaced <br> or <p> tags, and ensure the data is correctly formatted for further processing.
# Example 2:
# ###document:
# law relating the apparent contrast, Note 1 to entry: The formula is sometimes written where the exponent, Note 2 to entry: Taking into account the relationship between atmospheric transmissivity, Note 3 to entry: The contrast is taken to be the quotient of the difference between the luminance of the object and the luminance of the background, and the luminance of the background.  Note 4 to entry: This entry was numbered 845-11-22 in IEC 60050-845:1987.  Note 5 to entry: This entry was numbered 17-629 in CIE S 017:2011.
# ###New Question:
# An object is placed in front of a lens with a focal length of \\( f = 50 \\, \\text{{cm}} \\). The object is positioned at a distance of \\( d_o = 150 \\, \\text{{cm}} \\) from the lens, and an external factor, such as the medium's refractive index, changes the object distance by a factor of \\( r = 0.8 \\). How would you calculate the apparent image distance \\( d_i \\) using the lens equation: \\(\\frac{{1}}{{f}} = \\frac{{1}}{{d_o}} + \\frac{{1}}{{d_i}}\\).
# Example 3:
# ###document:
# About Marie McGinley\nShe is truly an expert with an impressive and broad knowledge of IP law\" - Chambers Europe 2017\nMarie is a Partner and Head of Intellectual Property, Technology and Data Protection. Marie practises in both contentious and commercial intellectual property/technology matters for a broad range of domestic and international clients. She is also a registered Irish Trade Mark Agent. Marie advises on commercial, regulatory and transactional matters.\nMarie has particular experience in intellectual property/technology development, procurement and licensing deals, including managed services, systems integration, technology and business process outsourcing for both domestic and international clients. data protection compliance.\nMarie is also involved in strategic legal due diligence and transitional services arrangements in relation to corporate acquisitions, disposals and restructurings.\nMarie is a member of the IP and Technology Committee and Commercial Law Committee of the Dublin Solicitor Bar Association.\nMarie has spoken at the National Data Protection Conference run by the Irish Computer Society in collaboration with the Association of Data Protection Officers in relation to various data protection matters, including direct marketing initiatives.\nMarie regularly contributes to the E-Commerce Law Report and PLC.\nMarie lectures and tutors in the area of Intellectual Property and Information Technology at the Law Society of Ireland.
# ###New Question:
# What are the legal implications and challenges of enforcing intellectual property rights across multiple jurisdictions, particularly when dealing with digital products and services?
# Example 4:
# ###document:
# The stock market is down Monday, with the Dow Jones Industrial Average down 0.42%, the Nasdaq down 0.18% and the S&P 500 down 0.43%. Today's winners include a pharmaceutical providing a positive update to one of its drug trials and a medical application manufacturer getting bought. Today's only loser is a for-profit educator settling a case with Sallie Mae. Here are Monday's market winners and loser. Biggest Winners Shares of Peregrine Pharmaceuticals, Inc. (NASDAQ: PPHM) are up 82.89% to $2.47 on trading volume of 29.0 million shares. The pharmaceutical company provided strong results of its review of a lung-cancer drug trial, as the company pointed out discrepancies were more limited than the company initially thought. The 52-week high is $5.50. Shares of Epocrates, Inc. (NASDAQ: EPOC) are up 21.58% to $11.70 on trading volume of 3.5 million shares. AthenaHealth, Inc. (NASDAQ: ATHN) will buy the firm for $11.75 per share, or about $292 million. The 52-week high is $11.97 Biggest Loser Shares of ITT Educational Services Inc. (NYSE: ESI) are down 15.76% to $16.25 on trading volume of 3.2 million shares. The for-profit educator will pay Sallie Mae $46 million to settle litigation involving student loans. Before Monday, the 52-week low was $16.37. Follow Samuel on Twitter: SWeigley Samuel Weigley
# ###New Question:
# A company observes that its stock price follows a quadratic trend over time. The price \( P(t) \) is modeled by the equation \( P(t) = at^2 + bt + c \), where \( t \) is the time in days, and \( a \), \( b \), and \( c \) are constants. If the stock price was \$20 on day 0, \$25 on day 1, and \$30 on day 2, determine the values of \( a \), \( b \), and \( c \).
# ###Your task:
# ###document:
# {doc}
# ###important:
# 1. Do not reuse information from the original document for the new question.
# 2. The new question should be able to be answered without information from the documentation.
# 3. You should capture the difference and correlation between the document and the question in the examples I've provided.
# 4. Do not focusing too much on the question and the form of the question in the example.
# 5. Ensure that the new question you generate is of high quality.
# 6. Do not provide a solution or answer to the question.
# Your output should be as follows:
# ###New Question: Here is the new question.
# '''

# doc_diff_instruct = '''What do you think are the important attributes that make up the following document,  please change the attributes to generate a new question, where subtopic is an attribute that must exist and change.
# Before I give you the document, I'll give you two examples of documents and its important attributes:
# Example 1:
# ###document:
# Impact of network delays on Hyperledger Fabric. Blockchain has become one of the most attractive technologies for applications, with a large range of deployments such as production, economy, or banking. Under the hood, Blockchain technology is a type of distributed database that supports untrusted parties. In this paper we focus Hyperledger Fabric, the first blockchain in the market tailored for a private environment, allowing businesses to create a permissioned network. Hyperledger Fabric implements a PBFT consensus in order to maintain a non forking blockchain at the application level. We deployed this framework over an area network between France and Germany in order to evaluate its performance when potentially large network delays are observed. Overall we found that when network delay increases significantly (i.e. up to 3.5 seconds at network layer between two clouds), we observed that the blocks added to our blockchain had up to 134 seconds offset after 100 th block from one cloud to another. Thus by delaying block propagation, we demonstrated that Hyperledger Fabric does not provide sufficient consistency guaranties to be deployed in critical environments. Our work, is the fist to evidence the negative impact of network delays on a PBFT based blockchain.
# [Attributes]:
# Writing Style: Encouraging papers with different writing styles, such as technical, expository,
# theoretical, or empirical, can bring diversity to the presentation and appeal to a wider range of readers.
# Subtopics: Promoting papers that explore different subtopics within the broader topic can provide
# comprehensive coverage and delve into specific areas of interest.
# Techniques: Encouraging papers that employ different research methodologies, such as experimental,
# computational, or analytical, can bring diverse approaches to studying the topic.
# Data Sources: Promoting papers that utilize diverse data sources, such as surveys, simulations, 
# real-world datasets, or case studies, can offer different perspectives and insights into the topic.
# Interdisciplinary Perspectives: Encouraging papers that incorporate interdisciplinary perspectives,
# drawing insights from multiple fields or combining methodologies from different disciplines, can
# contribute to a richer understanding of the topic.
# [New Question]:
# How does the RBF-FD-inspired technique efficiently approximate definite integrals over the volume of a ball using arbitrarily scattered nodes without requiring uniformity?
# Example 2:
# ###document:
# Don't waste your time even just simply flipping through this magazine at the newstand. Trust me... there will be no worthwhile patterns (I mean... just look at what they choose to grace their cover!!!) I have stopped hoping for even a half way decent pattern to come along during the two years or so. I have seen litteraly only ONE knittable pattern in the last three years (December 2004 I believe it was... a lace cardigan with beaded trim). Even the articles are pointless. Save your time and money and get a subscription to Interweave Knits or Vogue Knitting. Or opt for a new magazine (not available at all newstands in the US) called Simply Knitting, which is imported from the UK. It amazes me that this magazine is even still in production with how horible it is!!
# [Attributes]:
# Product Type: Clearly mention the type of product you are reviewing, such as a smartphone, laptop, or fitness tracker. This helps readers understand the category and purpose of the product.
# Brand: Specify the brand of the product as it often influences quality, reputation, and customer support. Discuss the brand's overall credibility and whether it aligns with your expectations.
# User Experience: Evaluate the overall user experience of the product. Discuss its speed, accuracy, reliability, and efficiency in performing its intended tasks. Highlight any exceptional or lacking performance aspects.
# Quality and Durability: Assess the quality of the product, including the materials used, construction, and overall durability. Discuss whether it feels well-made, solid, and likely to withstand regular use over time.
# Features and Functionality: Describe the specific features and functions of the product. Highlight any unique or standout features that enhance its usability or set it apart from similar products in the market.
# [New Question]:
# How can Men's Health Magazine help men improve their overall lifestyle and address key health and wellness concerns?
# ###Your task:
# ###document:
# {doc}
# ###important:
# The attributes before and after the change should be independent of each other.
# You need to explain the reason for the original attributes and the changed attributes.
# Ensure that the new question you generate is of high quality.
# Don't provide a solution or answer to the question.
# Your output should be as follows:
# [Attributes]: Here are the important attributes that make up the following document.
# [New Question]: Here is the new question.
# [Reason]: Reason for the original attributes and the changed attributes.
# '''

persona_com_instruct_generate_rewrite_wo_persona_0 = '''Please generate a new, high quality, reasonable and more challenging version of the question based on the given question.
### Important:
1. You need to explain why the new question is more challenging.
2. Don't provide a solution or answer to the new question.
### Original Question:
{question}
Your output should be as follows:
### New Question:
Here is the new question.
### Reason:
Your reason for the new question.
'''

persona_com_instruct_generate_rewrite_wo_persona_w_reason = '''Please generate a new, high quality, reasonable and more challenging version of the given question.
### Important:
1. You need to explain why the new question is more challenging.
2. Don't provide a solution or answer to the new question.
### Original Question:
{question}
Your output should be as follows:
### New Question:
Here is the new question.
### Reason:
Your reason for the new question.
'''

persona_com_instruct_generate_rewrite_wo_persona = '''Please generate a new, high quality, reasonable and more challenging version of the given question.
### Important:
You only need to generate the new question, do not provide a solution or answer to the new question!
### Original Question:
{question}
Your output should be formatted as follows:
[New Question]: Here is the new question.'''

answer_generate = '''
Here is an instruction that describes a task, write a response that appropriately completes the request.
For this task you will generate a good length answer using your best helpfulness and wisdom, and No need to include verbose or extraneous information.

### Instruction:
{instruction}
### Response:
'''

reform_prompt='''Rewrite the following question as a prompt:
### question:
{question}
Your output should be as follows:
### prompt: Here is the new prompt.
'''