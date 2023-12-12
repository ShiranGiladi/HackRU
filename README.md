# HackRU

My team - Amitai Shmeeda, Ron Lebiush, Ron Shahar, Orian D, and I - participated in the HackRU hackathon hosted by Reichman University. We took up the Salesforce challenge and decided to focus on enhancing their Slack product. After brainstorming and consulting with mentors, we identified two common pain points customers faced while using Slack.

Firstly, discussions about certain products sometimes stretched longer than planned due to conflicts among team members. Secondly, lengthy chat correspondences made it challenging to keep track of all the important details. Inspired by these insights, we came up with the idea of integrating Slack with ChatGPT.

Our idea was simple yet powerful. By integrating ChatGPT into Slack channels, it would act as a "third party" with an objective opinion, helping to resolve conflicts, summarizing conversations for easier catch-up, and much more. Our implementation relied on Slack's TOKEN and OpenAI API, which we skillfully harnessed using Python code. This innovative interface allowed ChatGPT to access conversations in the channel and offer its expertise.

We have recently introduced an enhancement to our integration. Previously, users had to manually run the code to activate ChatGPT. However, we aimed to provide seamless access to ChatGPT directly from the Slack channel itself. Hence, we created a slash command: /askchatgpt. Now, you can easily "call" ChatGPT from the Slack channel as desired!

🛠️ The tools that we used for this project include:
- Flask app written in Python
- Render for deploying the Flask app
- Slack's TOKEN
- OpenAI API

📹 Check out the videos below to witness the integration in action.


Summarizing a conversation:

https://github.com/ShiranGiladi/TicTacToe/assets/105810206/c62418b7-f8ed-401a-acb0-8b3a9a4f5d97


Solving a conflict during a conversation:

https://github.com/ShiranGiladi/TicTacToe/assets/105810206/27e89a80-acdf-4f96-a267-89a5a98defe7


Gettig advice:

https://github.com/ShiranGiladi/TicTacToe/assets/105810206/83e02195-cefe-42ad-be8f-5cdb983e25ea
